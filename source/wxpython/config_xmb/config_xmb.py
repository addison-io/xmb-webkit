#!/usr/bin/env python
"""
Config XMB.
"""

import configparser
import wx
import os


class ConfigXMBFrame(wx.Frame):
    """
    A Frame that says Config XMB
    """
    def __init__(self, *args, **kw):
        super(ConfigXMBFrame, self).__init__(*args, **kw)
        self.SetIcon(wx.Icon(os.path.join(os.path.abspath("."), "icon_config.ico")))
        
        self.__config = configparser.ConfigParser()

        self.__roms_path = ''
        self.__gc_path = ''
        self.__gc_param = ''
        self.__n64_path = ''
        self.__n64_param = ''
        self.__nes_path = ''
        self.__nes_param = ''
        self.__ps1_path = ''
        self.__ps1_param = ''
        self.__ps2_path = ''
        self.__ps2_param = ''
        self.__snes_path = ''
        self.__snes_param = ''

        self.__config.read('./config.ini')
        if 'PATH' in self.__config:
            if 'roms_path' in self.__config['PATH']:
                self.__roms_path = self.__config['PATH']['roms_path']
        if 'ROM_EXE_PATH' in self.__config:
            if 'gc' in self.__config['ROM_EXE_PATH']:
                gc_path = self.__config['ROM_EXE_PATH']['gc'].split()
                if len(gc_path):
                    self.__gc_path = gc_path[0]
                    if len(gc_path) > 1:
                        self.__gc_param = gc_path[1]
            if 'n64' in self.__config['ROM_EXE_PATH']:
                n64_path = self.__config['ROM_EXE_PATH']['n64'].split()
                if len(n64_path):
                    self.__n64_path = n64_path[0]
                    if len(n64_path) > 1:
                        self.__n64_param = n64_path[1]
            if 'nes' in self.__config['ROM_EXE_PATH']:
                nes_path = self.__config['ROM_EXE_PATH']['nes'].split()
                if len(nes_path):
                    self.__nes_path = nes_path[0]
                    if len(nes_path) > 1:
                        self.__nes_param = nes_path[1]
            if 'ps1' in self.__config['ROM_EXE_PATH']:
                ps1_path = self.__config['ROM_EXE_PATH']['ps1'].split()
                if len(ps1_path):
                    self.__ps1_path = ps1_path[0]
                    if len(ps1_path) > 1:
                        self.__ps1_param = ps1_path[1]
            if 'ps2' in self.__config['ROM_EXE_PATH']:
                ps2_path = self.__config['ROM_EXE_PATH']['ps2'].split()
                if len(ps2_path):
                    self.__ps2_path = ps2_path[0]
                    if len(ps2_path) > 1:
                        self.__ps2_param = ps2_path[1]
            if 'snes' in self.__config['ROM_EXE_PATH']:
                snes_path = self.__config['ROM_EXE_PATH']['snes'].split()
                if len(snes_path):
                    self.__snes_path = snes_path[0]
                    if len(snes_path) > 1:
                        self.__snes_param = snes_path[1]

        panel = wx.Panel(self)

        # ROMS Path
        romsLabel = wx.StaticText(panel, label="ROMS Path:", pos = (10, 10))
        font = romsLabel.GetFont()
        font = font.Bold()
        romsLabel.SetFont(font)

        romsFolder = wx.DirPickerCtrl(panel, wx.ID_ANY, pos = (10, 25), path = self.__roms_path, style= wx.DIRP_DEFAULT_STYLE, size = (450, 30))
        romsFolder.Bind(wx.EVT_DIRPICKER_CHANGED, self.changeRoms)
        
        # GC
        gcLabel = wx.StaticText(panel, label="GC:", pos = (10, 60))
        font = romsLabel.GetFont()
        font = font.Bold()
        gcLabel.SetFont(font)

        gcPath = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 75), path = self.__gc_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        gcPath.Bind(wx.EVT_FILEPICKER_CHANGED, self.changeGCPath)
        
        self.gc_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__gc_param, pos = (465, 80), size = (100, 20))
        self.gc_param.Bind(wx.EVT_TEXT, self.changeGCParam)
        
        # N64
        n64Label = wx.StaticText(panel, label="N64:", pos = (10, 110))
        font = romsLabel.GetFont()
        font = font.Bold()
        n64Label.SetFont(font)

        n64Path = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 125), path = self.__n64_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        n64Path.Bind(wx.EVT_FILEPICKER_CHANGED, self.changeN64Path)
        
        self.n64_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__n64_param, pos = (465, 130), size = (100, 20))
        self.n64_param.Bind(wx.EVT_TEXT, self.changeN64Param)
        
        # NES
        nesLabel = wx.StaticText(panel, label="NES:", pos = (10, 160))
        font = romsLabel.GetFont()
        font = font.Bold()
        nesLabel.SetFont(font)

        nesPath = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 175), path = self.__nes_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        nesPath.Bind(wx.EVT_FILEPICKER_CHANGED, self.changeNESPath)
        
        self.nes_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__nes_param, pos = (465, 180), size = (100, 20))
        self.nes_param.Bind(wx.EVT_TEXT, self.changeNESParam)
        
        # PS1
        ps1Label = wx.StaticText(panel, label="PS1:", pos = (10, 210))
        font = romsLabel.GetFont()
        font = font.Bold()
        ps1Label.SetFont(font)

        ps1Path = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 225), path = self.__ps1_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        ps1Path.Bind(wx.EVT_FILEPICKER_CHANGED, self.changePS1Path)
        
        self.ps1_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__ps1_param, pos = (465, 230), size = (100, 20))
        self.ps1_param.Bind(wx.EVT_TEXT, self.changePS1Param)
        
        # PS2
        ps2Label = wx.StaticText(panel, label="PS2:", pos = (10, 260))
        font = romsLabel.GetFont()
        font = font.Bold()
        ps2Label.SetFont(font)

        ps2Path = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 275), path = self.__ps2_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        ps2Path.Bind(wx.EVT_FILEPICKER_CHANGED, self.changePS2Path)
        
        self.ps2_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__ps2_param, pos = (465, 280), size = (100, 20))
        self.ps2_param.Bind(wx.EVT_TEXT, self.changePS2Param)
        
        # SNES
        snesLabel = wx.StaticText(panel, label="SNES:", pos = (10, 310))
        font = romsLabel.GetFont()
        font = font.Bold()
        snesLabel.SetFont(font)

        snesPath = wx.FilePickerCtrl(panel, wx.ID_ANY, pos = (10, 325), path = self.__snes_path, style= wx.FLP_DEFAULT_STYLE, size = (450, 30))
        snesPath.Bind(wx.EVT_FILEPICKER_CHANGED, self.changeSNESPath)
        
        self.snes_param = wx.TextCtrl(panel, wx.ID_ANY, value = self.__snes_param, pos = (465, 330), size = (100, 20))
        self.snes_param.Bind(wx.EVT_TEXT, self.changeSNESParam)

        # Set Button
        setButton = wx.Button(panel, wx.ID_ANY, 'Set', (110, 370))
        setButton.Bind(wx.EVT_BUTTON, self.onSetButton)

        # Cancel Button
        cancelButton = wx.Button(panel, wx.ID_ANY, 'Cancel', (385, 370))
        cancelButton.Bind(wx.EVT_BUTTON, self.onCancelButton)

        # Frame
        self.Centre()
        self.Show()


    def changeRoms(self, event):
        self.__roms_path = event.GetPath()


    def changeGCPath(self, event):
        self.__gc_path = event.GetPath()


    def changeGCParam(self, event):
        self.__gc_param = self.gc_param.GetValue()


    def changeN64Path(self, event):
        self.__n64_path = event.GetPath()


    def changeN64Param(self, event):
        self.__n64_param = self.n64_param.GetValue()


    def changeNESPath(self, event):
        self.__nes_path = event.GetPath()


    def changeNESParam(self, event):
        self.__nes_param = self.nes_param.GetValue()


    def changePS1Path(self, event):
        self.__ps1_path = event.GetPath()


    def changePS1Param(self, event):
        self.__ps1_param = self.ps1_param.GetValue()


    def changePS2Path(self, event):
        self.__ps2_path = event.GetPath()


    def changePS2Param(self, event):
        self.__ps2_param = self.ps2_param.GetValue()


    def changeSNESPath(self, event):
        self.__snes_path = event.GetPath()


    def changeSNESParam(self, event):
        self.__snes_param = self.snes_param.GetValue()
        

    def onSetButton(self, event):
        self.__config['PATH'] = {
            'roms_path': self.__roms_path
        }
        self.__config['ROM_EXE_PATH'] = {
            'gc': self.__gc_path + ' ' + self.__gc_param,
            'n64': self.__n64_path + ' ' + self.__n64_param,
            'nes': self.__nes_path + ' ' + self.__nes_param,
            'ps1': self.__ps1_path + ' ' + self.__ps1_param,
            'ps2': self.__ps2_path + ' ' + self.__ps2_param,
            'snes': self.__snes_path + ' ' + self.__snes_param,
        }
        
        with open('./config.ini', 'w') as configfile:
            self.__config.write(configfile)


    def onCancelButton(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frm = ConfigXMBFrame(None, title='Config XMB', size = (590, 450))
    frm.Show()
    app.MainLoop()