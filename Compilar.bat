set PLAYWRIGHT_BROWSERS_PATH=0

python -m playwright install

python -m PyInstaller --noconfirm --noconsole --add-data ".env;_internal" --add-data "Contratos_docx" --add-data "Tabelas" --hidden-import babel.numbers main.py -n Gerador_de_Contratos --collect-all "PyQt5" --collect-all "requests" --collect-all "playwright" --collect-all "bs4" --collect-all "psycopg2" --collect-all "python-docx"

pause