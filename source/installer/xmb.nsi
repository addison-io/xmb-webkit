############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System                
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006               
############################################################################################

!define APP_NAME "XMB"
!define VERSION "00.01.00.00"
!define DESCRIPTION "XMB Game Launcher"
!define LICENSE_TXT ".\gplv3.txt"
!define INSTALLER_NAME ".\XMB_Setup.exe"
!define MAIN_APP_EXE "xmb.exe"
!define ICON ".\xmb.ico"
!define UNICON ".\xmb_del.ico"
!define BANNER ".\xmb_install.bmp"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

######################################################################

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$APPDATA\XMB"
RequestExecutionLevel user

######################################################################




!include "MUI2.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!define MUI_ICON "${ICON}"
!define MUI_UNICON "${UNICON}"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "${BANNER}" ; optional

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "XMB"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File ".\release\chromium.pid"
File ".\release\config.ini"
File ".\release\config_pc_games.exe"
File ".\release\config_xmb.exe"
File ".\release\db.sqlite3"
File ".\release\icon_config.ico"
File ".\release\index.html"
File ".\release\pc_games.ini"
File ".\release\xmb.exe"
File ".\release\xmb.ico"
SetOutPath "$INSTDIR\webassets\video"
File ".\release\webassets\video\main.mp4"
File ".\release\webassets\video\No Video.mp4"
SetOutPath "$INSTDIR\webassets\js"
File ".\release\webassets\js\script.js"
SetOutPath "$INSTDIR\webassets\img"
File ".\release\webassets\img\No Image.png"
SetOutPath "$INSTDIR\webassets\img\sys-icon"
File ".\release\webassets\img\sys-icon\gc.png"
File ".\release\webassets\img\sys-icon\n64.png"
File ".\release\webassets\img\sys-icon\nes.png"
File ".\release\webassets\img\sys-icon\pc.png"
File ".\release\webassets\img\sys-icon\ps1.png"
File ".\release\webassets\img\sys-icon\ps2.png"
File ".\release\webassets\img\sys-icon\snes.png"
SetOutPath "$INSTDIR\webassets\css"
File ".\release\webassets\css\main.css"
SetOutPath "$INSTDIR\webassets\audio"
File ".\release\webassets\audio\tick.mp3"
SetOutPath "$INSTDIR\chromium"
File ".\release\chromium\chrome.exe"
File ".\release\chromium\chrome_proxy.exe"
SetOutPath "$INSTDIR\chromium\124.0.6367.79"
File ".\release\chromium\124.0.6367.79\124.0.6367.79.manifest"
File ".\release\chromium\124.0.6367.79\chrome.dll"
File ".\release\chromium\124.0.6367.79\chrome_100_percent.pak"
File ".\release\chromium\124.0.6367.79\chrome_200_percent.pak"
File ".\release\chromium\124.0.6367.79\chrome_elf.dll"
File ".\release\chromium\124.0.6367.79\chrome_pwa_launcher.exe"
File ".\release\chromium\124.0.6367.79\chrome_wer.dll"
File ".\release\chromium\124.0.6367.79\d3dcompiler_47.dll"
File ".\release\chromium\124.0.6367.79\dxcompiler.dll"
File ".\release\chromium\124.0.6367.79\dxil.dll"
File ".\release\chromium\124.0.6367.79\eventlog_provider.dll"
File ".\release\chromium\124.0.6367.79\icudtl.dat"
File ".\release\chromium\124.0.6367.79\libEGL.dll"
File ".\release\chromium\124.0.6367.79\libGLESv2.dll"
File ".\release\chromium\124.0.6367.79\mojo_core.dll"
File ".\release\chromium\124.0.6367.79\notification_helper.exe"
File ".\release\chromium\124.0.6367.79\resources.pak"
File ".\release\chromium\124.0.6367.79\v8_context_snapshot.bin"
File ".\release\chromium\124.0.6367.79\vk_swiftshader.dll"
File ".\release\chromium\124.0.6367.79\vk_swiftshader_icd.json"
File ".\release\chromium\124.0.6367.79\vulkan-1.dll"
SetOutPath "$INSTDIR\chromium\124.0.6367.79\VisualElements"
File ".\release\chromium\124.0.6367.79\VisualElements\Logo.png"
File ".\release\chromium\124.0.6367.79\VisualElements\SmallLogo.png"
SetOutPath "$INSTDIR\chromium\124.0.6367.79\MEIPreload"
File ".\release\chromium\124.0.6367.79\MEIPreload\manifest.json"
File ".\release\chromium\124.0.6367.79\MEIPreload\preloaded_data.pb"
SetOutPath "$INSTDIR\chromium\124.0.6367.79\Locales"
File ".\release\chromium\124.0.6367.79\Locales\af.pak"
File ".\release\chromium\124.0.6367.79\Locales\am.pak"
File ".\release\chromium\124.0.6367.79\Locales\ar.pak"
File ".\release\chromium\124.0.6367.79\Locales\bg.pak"
File ".\release\chromium\124.0.6367.79\Locales\bn.pak"
File ".\release\chromium\124.0.6367.79\Locales\ca.pak"
File ".\release\chromium\124.0.6367.79\Locales\cs.pak"
File ".\release\chromium\124.0.6367.79\Locales\da.pak"
File ".\release\chromium\124.0.6367.79\Locales\de.pak"
File ".\release\chromium\124.0.6367.79\Locales\el.pak"
File ".\release\chromium\124.0.6367.79\Locales\en-GB.pak"
File ".\release\chromium\124.0.6367.79\Locales\en-US.pak"
File ".\release\chromium\124.0.6367.79\Locales\es-419.pak"
File ".\release\chromium\124.0.6367.79\Locales\es.pak"
File ".\release\chromium\124.0.6367.79\Locales\et.pak"
File ".\release\chromium\124.0.6367.79\Locales\fa.pak"
File ".\release\chromium\124.0.6367.79\Locales\fi.pak"
File ".\release\chromium\124.0.6367.79\Locales\fil.pak"
File ".\release\chromium\124.0.6367.79\Locales\fr.pak"
File ".\release\chromium\124.0.6367.79\Locales\gu.pak"
File ".\release\chromium\124.0.6367.79\Locales\he.pak"
File ".\release\chromium\124.0.6367.79\Locales\hi.pak"
File ".\release\chromium\124.0.6367.79\Locales\hr.pak"
File ".\release\chromium\124.0.6367.79\Locales\hu.pak"
File ".\release\chromium\124.0.6367.79\Locales\id.pak"
File ".\release\chromium\124.0.6367.79\Locales\it.pak"
File ".\release\chromium\124.0.6367.79\Locales\ja.pak"
File ".\release\chromium\124.0.6367.79\Locales\kn.pak"
File ".\release\chromium\124.0.6367.79\Locales\ko.pak"
File ".\release\chromium\124.0.6367.79\Locales\lt.pak"
File ".\release\chromium\124.0.6367.79\Locales\lv.pak"
File ".\release\chromium\124.0.6367.79\Locales\ml.pak"
File ".\release\chromium\124.0.6367.79\Locales\mr.pak"
File ".\release\chromium\124.0.6367.79\Locales\ms.pak"
File ".\release\chromium\124.0.6367.79\Locales\nb.pak"
File ".\release\chromium\124.0.6367.79\Locales\nl.pak"
File ".\release\chromium\124.0.6367.79\Locales\pl.pak"
File ".\release\chromium\124.0.6367.79\Locales\pt-BR.pak"
File ".\release\chromium\124.0.6367.79\Locales\pt-PT.pak"
File ".\release\chromium\124.0.6367.79\Locales\ro.pak"
File ".\release\chromium\124.0.6367.79\Locales\ru.pak"
File ".\release\chromium\124.0.6367.79\Locales\sk.pak"
File ".\release\chromium\124.0.6367.79\Locales\sl.pak"
File ".\release\chromium\124.0.6367.79\Locales\sr.pak"
File ".\release\chromium\124.0.6367.79\Locales\sv.pak"
File ".\release\chromium\124.0.6367.79\Locales\sw.pak"
File ".\release\chromium\124.0.6367.79\Locales\ta.pak"
File ".\release\chromium\124.0.6367.79\Locales\te.pak"
File ".\release\chromium\124.0.6367.79\Locales\th.pak"
File ".\release\chromium\124.0.6367.79\Locales\tr.pak"
File ".\release\chromium\124.0.6367.79\Locales\uk.pak"
File ".\release\chromium\124.0.6367.79\Locales\ur.pak"
File ".\release\chromium\124.0.6367.79\Locales\vi.pak"
File ".\release\chromium\124.0.6367.79\Locales\zh-CN.pak"
File ".\release\chromium\124.0.6367.79\Locales\zh-TW.pak"
SetOutPath "$INSTDIR\chromium\124.0.6367.79\Extensions"
File ".\release\chromium\124.0.6367.79\Extensions\external_extensions.json"
SectionEnd


######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Configure XMB.lnk" "$INSTDIR\config_xmb.exe"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Configure PC Games.lnk" "$INSTDIR\config_pc_games.exe"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\XMB"
CreateShortCut "$SMPROGRAMS\XMB\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\XMB\Configure XMB.lnk" "$INSTDIR\config_xmb.exe"
CreateShortCut "$SMPROGRAMS\XMB\Configure PC Games.lnk" "$INSTDIR\config_pc_games.exe"
CreateShortCut "$SMPROGRAMS\XMB\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"

SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}
Delete "$INSTDIR\chromium.pid"
Delete "$INSTDIR\config.ini"
Delete "$INSTDIR\config_pc_games.exe"
Delete "$INSTDIR\config_xmb.exe"
Delete "$INSTDIR\db.sqlite3"
Delete "$INSTDIR\icon_config.ico"
Delete "$INSTDIR\index.html"
Delete "$INSTDIR\pc_games.ini"
Delete "$INSTDIR\xmb.exe"
Delete "$INSTDIR\xmb.ico"
Delete "$INSTDIR\webassets\video\main.mp4"
Delete "$INSTDIR\webassets\video\No Video.mp4"
Delete "$INSTDIR\webassets\js\script.js"
Delete "$INSTDIR\webassets\img\No Image.png"
Delete "$INSTDIR\webassets\img\sys-icon\gc.png"
Delete "$INSTDIR\webassets\img\sys-icon\n64.png"
Delete "$INSTDIR\webassets\img\sys-icon\nes.png"
Delete "$INSTDIR\webassets\img\sys-icon\pc.png"
Delete "$INSTDIR\webassets\img\sys-icon\ps1.png"
Delete "$INSTDIR\webassets\img\sys-icon\ps2.png"
Delete "$INSTDIR\webassets\img\sys-icon\snes.png"
Delete "$INSTDIR\webassets\css\main.css"
Delete "$INSTDIR\webassets\audio\tick.mp3"
Delete "$INSTDIR\chromium\chrome.exe"
Delete "$INSTDIR\chromium\chrome_proxy.exe"
Delete "$INSTDIR\chromium\124.0.6367.79\124.0.6367.79.manifest"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome_100_percent.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome_200_percent.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome_elf.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome_pwa_launcher.exe"
Delete "$INSTDIR\chromium\124.0.6367.79\chrome_wer.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\d3dcompiler_47.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\dxcompiler.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\dxil.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\eventlog_provider.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\icudtl.dat"
Delete "$INSTDIR\chromium\124.0.6367.79\libEGL.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\libGLESv2.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\mojo_core.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\notification_helper.exe"
Delete "$INSTDIR\chromium\124.0.6367.79\resources.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\v8_context_snapshot.bin"
Delete "$INSTDIR\chromium\124.0.6367.79\vk_swiftshader.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\vk_swiftshader_icd.json"
Delete "$INSTDIR\chromium\124.0.6367.79\vulkan-1.dll"
Delete "$INSTDIR\chromium\124.0.6367.79\VisualElements\Logo.png"
Delete "$INSTDIR\chromium\124.0.6367.79\VisualElements\SmallLogo.png"
Delete "$INSTDIR\chromium\124.0.6367.79\MEIPreload\manifest.json"
Delete "$INSTDIR\chromium\124.0.6367.79\MEIPreload\preloaded_data.pb"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\af.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\am.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ar.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\bg.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\bn.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ca.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\cs.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\da.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\de.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\el.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\en-GB.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\en-US.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\es-419.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\es.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\et.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\fa.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\fi.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\fil.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\fr.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\gu.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\he.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\hi.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\hr.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\hu.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\id.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\it.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ja.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\kn.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ko.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\lt.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\lv.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ml.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\mr.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ms.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\nb.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\nl.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\pl.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\pt-BR.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\pt-PT.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ro.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ru.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\sk.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\sl.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\sr.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\sv.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\sw.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ta.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\te.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\th.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\tr.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\uk.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\ur.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\vi.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\zh-CN.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Locales\zh-TW.pak"
Delete "$INSTDIR\chromium\124.0.6367.79\Extensions\external_extensions.json"
 
RmDir "$INSTDIR\chromium\124.0.6367.79\Extensions"
RmDir "$INSTDIR\chromium\124.0.6367.79\Locales"
RmDir "$INSTDIR\chromium\124.0.6367.79\MEIPreload"
RmDir "$INSTDIR\chromium\124.0.6367.79\VisualElements"
RmDir "$INSTDIR\chromium\124.0.6367.79"
RmDir "$INSTDIR\chromium"
RmDir "$INSTDIR\webassets\audio"
RmDir "$INSTDIR\webassets\css"
RmDir "$INSTDIR\webassets\img\sys-icon"
RmDir "$INSTDIR\webassets\img"
RmDir "$INSTDIR\webassets\js"
RmDir "$INSTDIR\webassets\video"
 
Delete "$INSTDIR\uninstall.exe"


RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Configure XMB.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Configure PC Games.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\XMB\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\XMB\Uninstall ${APP_NAME}.lnk"
Delete "$SMPROGRAMS\XMB\Configure XMB.lnk"
Delete "$SMPROGRAMS\XMB\Configure PC Games.lnk"
RmDir "$SMPROGRAMS\XMB"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd

######################################################################

