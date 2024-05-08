# PS3's XMB Styled Game launcher
Windows game launcher interface done in HTML5 and JS, Backend in [Django](https://www.djangoproject.com). [Chromium](https://www.chromium.org) is used as the display interface.

Config utilities are in [wxPython](http://xpython.org) and compiled with [PyInstaller](https://pyinstaller.org). [NSIS](https://nsis.sourceforge.io) to make the installer.
[Skraper](https://www.skraper.net) is used to provide ROMs media.

Video:
[![Using Skraper](https://img.youtube.com/vi/dTEJ7UbyBCg/0.jpg)](https://www.youtube.com/watch?v=dTEJ7UbyBCg)

[Live Demo](https://addison-io.github.io/xmb-example/)

# How to Install

Download [XMB_Setup.exe](https://github.com/addison-io/xmb-webkit/releases/download/Release-0.01/XMB_Setup.exe) and run the installer.

# ROMs Directory
Your ROMs directory needs to have its layout in the following way for XMB to work correctly. 
```
roms/
├── gc/
│   └── example.iso
├── n64/
│   └── example.n64
├── nes/
│   └── example.nes
├── pc/
├── ps1/
│   └── example.iso
├── ps2/
│   └── example.iso
└── snes/
    └── example.smc
```


# User Skraper to Download ROMs Data

[Download Skraper](https://www.skraper.net) and scan your roms directory and scrape the media. 

How to video:
[![Using Skraper](https://img.youtube.com/vi/UdcOxOfyheY/0.jpg)](https://www.youtube.com/watch?v=UdcOxOfyheY)

### After adding PC Games media and running scraper on your roms directory, the file structure needs to be like this:
```
roms/
├── gc/
│   ├── media/
│   │   ├── box2dfront/
│   │   │   └── example.png
│   │   └── videos/
│   │       └── example.mp4
│   ├── Gamecube.dat
│   └── example.iso
├── n64/
│   ├── media/
│   │   ├── box2dfront/
│   │   │   └── example.png
│   │   └── videos/
│   │       └── example.mp4
│   ├── Nintendo 64.dat
│   └── example.n64
├── nes/
│   ├── media/
│   │   ├── box2dfront/
│   │   │   └── example.png
│   │   └── videos/
│   │       └── example.mp4
│   ├── Family Computer.dat
│   └── example.nes
├── pc/
│   └── media/
│       ├── box2dfront/
│       │   └── example.png
│       └── videos/
│           └── example.mp4
├── ps1/
│   ├── media/
│   │   ├── box2dfront/
│   │   │   └── example.png
│   │   └── videos/
│   │       └── example.mp4
│   ├── Playstation.dat
│   └── example.iso
├── ps2/
│   ├── media/
│   │   ├── box2dfront/
│   │   │   └── example.png
│   │   └── videos/
│   │       └── example.mp4
│   ├── Playstation 2.dat
│   └── example.iso
└── snes/
    ├── media/
    │   ├── box2dfront/
    │   │   └── example.png
    │   └── videos/
    │       └── example.mp4
    ├── Super Famicom.dat
    └── example.smc
```

# Configure XMB

Use XMB Configure to set your ROMs directory and set the path to your emulators executable. You can set arguments to pass on to the executable on the right.

Video:
[![Configuring XMB](https://img.youtube.com/vi/rUlmV8uYinU/0.jpg)](https://www.youtube.com/watch?v=rUlmV8uYinU)

# Configure PC Games

Use Configure PC Games to set up your PC games. The grid has the title, description, year of manufacture, and the path to the game executable or link. Your media files must have the same title as the name set in Configure PC Games. Double-click in the path field and select browse to bring up the file browser to select the path for your game. After seeing the path of the game, you must click in another cell before clicking set; Otherwise, it will not save the path. I will fix this issue in a later release.

Video:
[![Using Skraper](https://img.youtube.com/vi/7lVO8vWfmXc/0.jpg)](https://www.youtube.com/watch?v=7lVO8vWfmXc)