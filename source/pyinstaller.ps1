python -m PyInstaller --onefile --hide-console hide-early --icon=xmb.ico --distpath "../../release" --name=xmb.exe --add-data "static/:static/" manage.py

python -m PyInstaller --noconsole --onefile --icon=icon_config.ico --distpath "../../../release" --name=config_xmb.exe config_xmb.py

python -m PyInstaller --noconsole --onefile --icon=icon_config.ico --distpath "../../../release" --name=config_pc_games.exe config_pc_games.py