import os
from nicegui import ui
from dotenv import load_dotenv
from pages import login, home


load_dotenv()


ui.run(title='REGISTRATOR', port=8001, storage_secret=os.getenv('STORAGE_SECRET'))