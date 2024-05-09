import os
import sys
import subprocess
from django.urls import reverse
from django.apps import AppConfig
from django.conf import settings
from django.template.loader import render_to_string
from . import views


class RunStartup(AppConfig):
    name = 'playstation'


    def get_static_path(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            return os.path.join(os.path.abspath("."), settings.WEB_ASSETS_PATH)
        else:
            return os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("."))), 'release'), settings.WEB_ASSETS_PATH)

    
    def ready(self):
        roms = []
        sys_image_path = os.path.join(self.get_static_path(), settings.SYS_IMAGE_PATH)
        if os.path.exists(settings.ROMS_PATH):
            rom_entries = os.scandir(settings.ROMS_PATH)
            pc_exist = False

            for rom_entry in rom_entries:
                if rom_entry.is_dir():
                    if rom_entry.name == 'pc':
                        pc_exist = True
                    roms.append(views.get_games_in_rom(rom_entry.name))

            if not pc_exist:
                image = settings.NO_IMAGE_PATH
                if os.path.exists(sys_image_path):
                    xmb_image_entries = os.scandir(sys_image_path)
                    for xmb_image_entry in xmb_image_entries:
                        xmb_image_entry_name, xmb_image_entry_extension = os.path.splitext(xmb_image_entry.name)
                        if xmb_image_entry_name == 'pc':
                            image = xmb_image_entry.name

                roms.append({
                    'name': 'pc',
                    'image': image,
                    'title': '',
                    'description': '',
                    'author': '',
                    'games': []
                })
        
        tick_song_path = os.path.join(self.get_static_path(), settings.TICK_SONG_PATH)
        WINDOW_PLATFORM = (sys.platform == 'win32' or sys.platform == 'win64')
        if WINDOW_PLATFORM:
            tick_song_path = tick_song_path.replace("\\", "\\\\")
        index_file_html = render_to_string('render.html', {
            'no_image_path': settings.NO_IMAGE_PATH,
            'static_path': self.get_static_path(),
            'xmb_img_path': sys_image_path,
            'rom_path': settings.ROMS_PATH,
            'roms': roms,
            'run_rom_path': settings.BASE_URL + reverse('run'),
            'exit_path':  settings.BASE_URL + reverse('exit'),
            'tick_song_path': tick_song_path
        })

        with open('./index.html', 'w+', encoding="utf-8") as index_file:
            index_file.write(index_file_html)


        if os.path.exists(settings.CHROMIUM_PATH):
            chromium = subprocess.Popen(settings.CHROMIUM_PATH + ' --kiosk --enable-features=OverlayScrollbar,OverlayScrollbarFlashAfterAnyScrollUpdate,OverlayScrollbarFlashWhenMouseEnter --noerrdialogs --disable-session-crashed-bubble --disable-component-update --overscroll-history-navigation=0 --disable-features=Translate "' + os.path.join(os.path.abspath("."), 'index.html') + '"')
            with open('./chromium.pid', 'w+', encoding="utf-8") as chromium_file:
                chromium_file.write(str(chromium.pid))