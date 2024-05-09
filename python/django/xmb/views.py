from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import os
import sys
import re
import subprocess
import configparser
from operator import itemgetter
import xml.etree.ElementTree as ET


def get_games_in_rom(rom):
    games_config = configparser.ConfigParser(interpolation=None)
    games_config.read(os.path.join(os.path.abspath('.'), 'pc_games.ini'), encoding='utf-8')

    image = settings.NO_IMAGE_PATH
    title = ''
    description = ''
    author = ''
    games = []

    roms_path = os.path.join(settings.ROMS_PATH, rom)
    rom_media_path = os.path.join(roms_path, settings.ROMS_MEDIA_DIRECTORY)
    rom_img_path = os.path.join(rom_media_path, settings.ROMS_IMAGE_DIRECTORY)
    rom_3d_img_path = os.path.join(rom_media_path, settings.ROMS_3D_IMAGE_DIRECTORY)
    rom_video_path = os.path.join(rom_media_path, settings.ROMS_VIDEO_DIRECTORY)

    sys_image_path = os.path.join(settings.STATIC_PATH, settings.SYS_IMAGE_PATH)
    if os.path.exists(sys_image_path):
        xmb_image_entries = os.scandir(sys_image_path)
        for xmb_image_entry in xmb_image_entries:
            xmb_image_entry_name, xmb_image_entry_extension = os.path.splitext(xmb_image_entry.name)
            if xmb_image_entry_name == rom:
                image = xmb_image_entry.name

    if rom == 'pc':
        if games_config.has_section('INFO'):
            title = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config['INFO']['title']))
            description = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config['INFO']['description']))
            author = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config['INFO']['author']))

        game_number = 1
        game_loop = True
        while game_loop:
            if 'PC_GAME_' + str(game_number) in games_config:
                game_name = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config.get('PC_GAME_' + str(game_number), 'name', raw=True)))
                game_file_name = game_name.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
                game_image = settings.NO_IMAGE_PATH
                game_3d_image = settings.NO_IMAGE_PATH
                game_video = ''
                if os.path.exists(rom_img_path):
                    rom_image_entries = os.scandir(rom_img_path)
                    for rom_image_entry in rom_image_entries:
                        rom_image_entry_name, rom_image_entry_extension = os.path.splitext(rom_image_entry.name)
                        if game_file_name == rom_image_entry_name:
                            game_image = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_IMAGE_DIRECTORY), rom_image_entry.name)
                            game_3d_image = game_image
                if os.path.exists(rom_3d_img_path):
                    rom_3d_image_entries = os.scandir(rom_3d_img_path)
                    for rom_3d_image_entry in rom_3d_image_entries:
                        rom_3d_image_entry_name, rom_3d_image_entry_extension = os.path.splitext(rom_3d_image_entry.name)
                        if game_file_name == rom_3d_image_entry_name:
                            game_3d_image = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_3D_IMAGE_DIRECTORY), rom_3d_image_entry.name)
                if os.path.exists(rom_video_path):
                    rom_video_entries = os.scandir(rom_video_path)
                    for rom_video_entry in rom_video_entries:
                        rom_video_entry_name, rom_video_entry_extension = os.path.splitext(rom_video_entry.name)
                        if game_file_name == rom_video_entry_name:
                            game_video = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_VIDEO_DIRECTORY), rom_video_entry.name)

                games.append({
                    'name': game_name,
                    'description': re.sub(r'^"""', '', re.sub(r'"""$', '', games_config.get('PC_GAME_' + str(game_number), 'description', raw=True))),
                    'year': games_config.get('PC_GAME_' + str(game_number), 'year', raw=True),
                    'manufacturer': re.sub(r'^"""', '', re.sub(r'"""$', '', games_config.get('PC_GAME_' + str(game_number), 'manufacturer', raw=True))),
                    'image': game_image,
                    'image_3d': game_3d_image,
                    'video': game_video,
                })
                game_number = game_number + 1
            else:
                game_loop = False

    else:
        if os.path.exists(roms_path):
            rom_entries = os.scandir(roms_path)
            for rom_entry in rom_entries:
                if rom_entry.is_file():
                    rom_entry_name, rom_entry_extension = os.path.splitext(rom_entry.name)
                    if rom_entry_extension.lower() == '.dat':
                        rom_root = ET.parse(os.path.join(roms_path, rom_entry.name)).getroot()
                        if rom_root.tag == 'datafile':
                            for rom_tag in rom_root:
                                if rom_tag.tag == 'header':
                                    for rom_sub_tag in rom_tag:
                                        if rom_sub_tag.tag == 'name':
                                            title = rom_sub_tag.text
                                        elif rom_sub_tag.tag == 'description':
                                            description = rom_sub_tag.text
                                        elif rom_sub_tag.tag == 'author':
                                            author = rom_sub_tag.text
                                elif rom_tag.tag == 'game':
                                    if 'name' in rom_tag.attrib:
                                        game_name = rom_tag.attrib['name']
                                        game_description = ''
                                        game_year = ''
                                        game_manufacturer = ''
                                        game_image = settings.NO_IMAGE_PATH
                                        game_3d_image = settings.NO_IMAGE_PATH
                                        game_video = ''
                                        game_rom_name = ''
                                        game_rom_size = ''
                                        for rom_sub_tag in rom_tag:
                                            if rom_sub_tag.tag == 'description':
                                                game_description = rom_sub_tag.text
                                            elif rom_sub_tag.tag == 'year':
                                                game_year = rom_sub_tag.text
                                            elif rom_sub_tag.tag == 'manufacturer':
                                                game_manufacturer = rom_sub_tag.text
                                            elif rom_sub_tag.tag == 'rom':
                                                if 'name' in rom_sub_tag.attrib:
                                                    game_rom_name = rom_sub_tag.attrib['name']
                                                    game_rom_name_name, game_rom_name_extension = os.path.splitext(game_rom_name)                                                    
                                                    game_file_name = game_rom_name_name.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
                                                    if os.path.exists(rom_img_path):
                                                        rom_image_entries = os.scandir(rom_img_path)
                                                        for rom_image_entry in rom_image_entries:
                                                            rom_image_entry_name, rom_image_entry_extension = os.path.splitext(rom_image_entry.name)
                                                            if game_file_name == rom_image_entry_name:
                                                                game_image = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_IMAGE_DIRECTORY), rom_image_entry.name)
                                                                game_3d_image = game_image
                                                    if os.path.exists(rom_3d_img_path):
                                                        rom_3d_image_entries = os.scandir(rom_3d_img_path)
                                                        for rom_3d_image_entry in rom_3d_image_entries:
                                                            rom_3d_image_entry_name, rom_3d_image_entry_extension = os.path.splitext(rom_3d_image_entry.name)
                                                            if game_file_name == rom_3d_image_entry_name:
                                                                game_3d_image = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_3D_IMAGE_DIRECTORY), rom_3d_image_entry.name)
                                                    if os.path.exists(rom_video_path):
                                                        rom_video_entries = os.scandir(rom_video_path)
                                                        for rom_video_entry in rom_video_entries:
                                                            rom_video_entry_name, rom_video_entry_extension = os.path.splitext(rom_video_entry.name)
                                                            if game_file_name == rom_video_entry_name:
                                                                game_video = os.path.join(os.path.join(os.path.join(rom, settings.ROMS_MEDIA_DIRECTORY), settings.ROMS_VIDEO_DIRECTORY), rom_video_entry.name)
                                                if 'size' in rom_sub_tag.attrib:
                                                    game_rom_size = rom_sub_tag.attrib['size']
                                        games.append({
                                            'name': game_name,
                                            'description': game_description,
                                            'year': game_year,
                                            'manufacturer': game_manufacturer,
                                            'image': game_image,
                                            'image_3d': game_3d_image,
                                            'video': game_video,
                                            'rom': {
                                                'name': game_rom_name,
                                                'size': game_rom_size,
                                            }
                                        })
    
    games.sort(key=itemgetter('name'))
    return {
        'name': rom,
        'image': image,
        'title': title,
        'description': description,
        'author': author,
        'games': games
    }


def home(request):
    roms = []
    if os.path.exists(settings.ROMS_PATH):
        rom_entries = os.scandir(settings.ROMS_PATH)
        pc_exist = False

        for rom_entry in rom_entries:
            if rom_entry.is_dir():
                if rom_entry.name == 'pc':
                    pc_exist = True
                roms.append(get_games_in_rom(rom_entry.name))

        for rom in roms:
            rom['image'] = os.path.join(settings.SYS_IMAGE_PATH, rom['image'])

        if not pc_exist:
            image = settings.NO_IMAGE_PATH

            sys_image_path = os.path.join(settings.STATIC_PATH, settings.SYS_IMAGE_PATH)
            if os.path.exists(sys_image_path):
                xmb_image_entries = os.scandir(sys_image_path)
                for xmb_image_entry in xmb_image_entries:
                    xmb_image_entry_name, xmb_image_entry_extension = os.path.splitext(xmb_image_entry.name)
                    if xmb_image_entry_name == 'pc':
                        image = os.path.join(settings.SYS_IMAGE_PATH, xmb_image_entry.name)

            roms.append({
                'name': 'pc',
                'image': image,
                'title': '',
                'description': '',
                'author': '',
                'games': []
            })

    return render(request, 'index.html', {'roms': roms, 'tick_song': os.path.join(settings.STATIC_URL, settings.TICK_SONG_PATH).replace("\\", "/")})


def run(request):
    rom = request.GET.get("rom", "")
    iso = request.GET.get("iso", "")
    name = request.GET.get("name", "")
    
    games_config = configparser.ConfigParser(interpolation=None)
    games_config.read(os.path.join(os.path.abspath('.'), 'pc_games.ini'), encoding='utf-8')

    if rom in settings.ROM_EXEC_COMMANDS:
        os.system('start ' + settings.ROM_EXEC_COMMANDS[rom] + ' "' + os.path.join(os.path.join(settings.ROMS_PATH, rom), iso) + '"')
        return HttpResponse('start ' + settings.ROM_EXEC_COMMANDS[rom] + ' "' + os.path.join(os.path.join(settings.ROMS_PATH, rom), iso) + '"')
    else:
        if rom == 'pc':
            game_number = 1
            game_loop = True
            while game_loop:
                if 'PC_GAME_' + str(game_number) in games_config:
                    game_name = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config.get('PC_GAME_' + str(game_number), 'name', raw=True)))
                    if game_name == name:
                        game_cmd = re.sub(r'^"""', '', re.sub(r'"""$', '', games_config.get('PC_GAME_' + str(game_number), 'run_cmd', raw=True)))
                        os.system('"' + game_cmd + '"')
                        return HttpResponse('"' + game_cmd + '"')
                    game_number = game_number + 1
                else:
                    game_loop = False

    return HttpResponse(rom)


def exit(request):
    WINDOW_PLATFORM = (sys.platform == 'win32' or sys.platform == 'win64')
    if WINDOW_PLATFORM:
        chromium_file = open(os.path.join(os.path.abspath("."), 'chromium.pid'), 'r')
        chromium_lines = chromium_file.readlines()
        chromiumn_pid = ''
        for chromium_line in chromium_lines:
            if chromium_line:
                chromiumn_pid = str(chromium_line)
        os.system('taskkill /pid ' + chromiumn_pid + ' /F')
        chromium_file.close()

        os.system('taskkill /pid ' + str(os.getpid()) + ' /F')
    else:
        os.system('lsof -t -i tcp:8000 | xargs kill -9')
    
    return HttpResponse('Exit')