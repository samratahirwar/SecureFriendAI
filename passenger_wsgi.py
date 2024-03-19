import os
import sys
from app.wsgi import application as app

sys.path.insert(0, os.path.dirname(__file__))


application= app
