set PLAYWRIGHT_BROWSERS_PATH=0

python -m playwright install

python -m PyInstaller --noconfirm --noconsole --add-data ".env;_internal" --add-data "C:/Users/Tiago/Documents/GitHub/gerador_contratos/venv/Lib/site-packages/PyQt5/Qt5/plugins;PyQt5\Qt\plugins" --hidden-import babel.numbers --hidden-import PyQt5.QtWidgets --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui main.py -n Gerador_de_Contratos --collect-all "PyQt5" --collect-all "requests" --collect-all "playwright" --collect-all "bs4" --collect-all "psycopg2" --collect-all "python-docx"

pause