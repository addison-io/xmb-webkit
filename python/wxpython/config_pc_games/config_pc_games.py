#!/usr/bin/env python
"""
Config PC Games.
"""

import os
import configparser
import re
import wx
import wx.grid


class FilePickerCellEditor(wx.grid.GridCellEditor):
    def __init__(self, path):
        self.path = path
        wx.grid.GridCellEditor.__init__(self)


    def Create(self, parent, id, evtHandler):
        self.__fpc = wx.FilePickerCtrl(parent, wx.ID_ANY, path = self.path, style= wx.FLP_DEFAULT_STYLE)
        self.SetControl(self.__fpc)
        if evtHandler:
            self.__fpc.PushEventHandler(evtHandler)


    def EndEdit(self, row, col, grid, oldVal):
        grid.SetCellValue(row, col, self.__fpc.GetPath())
        pass


    def BeginEdit(self, row, col, grid):
        self.__fpc.SetFocus()


    def Reset(self):
        pass


    def Clone(self):
        pass
    

class ConfigPCGamesFrame(wx.Frame):
    """
    A Frame that says Config PC Games
    """
    def __init__(self, *args, **kw):
        super(ConfigPCGamesFrame, self).__init__(*args, **kw)
        self.SetIcon(wx.Icon(os.path.join(os.path.abspath("."), "icon_config.ico")))

        self.__grid_rows = 100

        self.__bold_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.__config = configparser.ConfigParser(interpolation=None)

        panel = wx.Panel(self)

        # Create a wxGrid object
        self.__grid = wx.grid.Grid(panel, wx.ID_ANY, (10, 10), (590, 410))

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        self.__grid.CreateGrid(self.__grid_rows, 5)

        # We can set the sizes of individual rows and columns in pixels
        self.__grid.SetColSize(0, 100)
        self.__grid.SetColSize(1, 150)
        self.__grid.SetColSize(2, 50)
        self.__grid.SetColSize(3, 90)
        self.__grid.SetColSize(4, 100)
        
        self.__grid.SetCellValue(0, 0, 'Name')
        self.__grid.SetReadOnly(0, 0)
        self.__grid.SetCellFont(0, 0, self.__bold_font)
        self.__grid.SetCellValue(0, 1, 'Description')
        self.__grid.SetReadOnly(0, 1)
        self.__grid.SetCellFont(0, 1, self.__bold_font)
        self.__grid.SetCellValue(0, 2, 'Year')
        self.__grid.SetReadOnly(0, 2)
        self.__grid.SetCellFont(0, 2, self.__bold_font)
        self.__grid.SetCellValue(0, 3, 'Manufacturer')
        self.__grid.SetReadOnly(0, 3)
        self.__grid.SetCellFont(0, 3, self.__bold_font)
        self.__grid.SetCellValue(0, 4, 'Command')
        self.__grid.SetReadOnly(0, 4)
        self.__grid.SetCellFont(0, 4, self.__bold_font)
        
   
        self.__config.read('./pc_games.ini', encoding='utf-8')
        game_number = 1
        game_loop = True
        while game_number < self.__grid_rows:
            cell_path = ''
            if 'PC_GAME_' + str(game_number) in self.__config:
                self.__grid.SetCellValue(game_number, 0, re.sub(r'^"""', '', re.sub(r'"""$', '', self.__config.get('PC_GAME_' + str(game_number), 'name', raw=True))))
                self.__grid.SetCellValue(game_number, 1, re.sub(r'^"""', '', re.sub(r'"""$', '', self.__config.get('PC_GAME_' + str(game_number), 'description', raw=True))))
                self.__grid.SetCellValue(game_number, 2, self.__config.get('PC_GAME_' + str(game_number), 'year', raw=True))
                self.__grid.SetCellValue(game_number, 3, re.sub(r'^"""', '', re.sub(r'"""$', '', self.__config.get('PC_GAME_' + str(game_number), 'manufacturer', raw=True))))
                cell_path = re.sub(r'^"""', '', re.sub(r'"""$', '', self.__config.get('PC_GAME_' + str(game_number), 'run_cmd', raw=True)))
                self.__grid.SetCellValue(game_number, 4, cell_path)
                
            self.__grid.SetCellEditor(game_number, 4, FilePickerCellEditor(cell_path))
            game_number = game_number + 1

        # Set Button
        setButton = wx.Button(panel, wx.ID_ANY, 'Set', (110, 430))
        setButton.Bind(wx.EVT_BUTTON, self.onSetButton)

        # Cancel Button
        cancelButton = wx.Button(panel, wx.ID_ANY, 'Cancel', (385, 430))
        cancelButton.Bind(wx.EVT_BUTTON, self.onCancelButton)

        # Frame
        self.Centre()
        self.Show()
        

    def onSetButton(self, event):
        if not self.__config.has_section('INFO'):
            self.__config.add_section('INFO')
        self.__config.set('INFO', 'title', 'title')
        self.__config.set('INFO', 'description', 'description')
        self.__config.set('INFO', 'author', 'author')
        
        row_number = 1
        game_number = 1
        while row_number < self.__grid_rows:
            game_name = self.__grid.GetCellValue(row_number, 0)
            game_description = self.__grid.GetCellValue(row_number, 1)
            game_year = self.__grid.GetCellValue(row_number, 2)
            game_manufacturer = self.__grid.GetCellValue(row_number, 3)
            game_run_cmd = self.__grid.GetCellValue(row_number, 4)

            if game_name:
                if not self.__config.has_section('PC_GAME_' + str(game_number)):
                    self.__config.add_section('PC_GAME_' + str(game_number))
                self.__config.set('PC_GAME_' + str(game_number), 'name', '"""' + game_name + '"""')
                self.__config.set('PC_GAME_' + str(game_number), 'description', '"""' + game_description + '"""')
                self.__config.set('PC_GAME_' + str(game_number), 'year', game_year)
                self.__config.set('PC_GAME_' + str(game_number), 'manufacturer', '"""' + game_manufacturer + '"""')
                self.__config.set('PC_GAME_' + str(game_number), 'run_cmd', '"""' + game_run_cmd + '"""')
                
                game_number = game_number + 1
            else:
                if self.__config.has_section('PC_GAME_' + str(row_number)):
                    self.__config.remove_section('PC_GAME_' + str(row_number))
            
            row_number = row_number + 1

        with open('./pc_games.ini', 'w', encoding='utf-8') as configfile:
            self.__config.write(configfile)


    def onCancelButton(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frm = ConfigPCGamesFrame(None, title='Config PC Games', size = (625, 500))
    frm.Show()
    app.MainLoop()