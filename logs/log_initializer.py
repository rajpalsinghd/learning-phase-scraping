import os
import logging
import pathlib

_here=os.path.dirname(os.path.abspath('app.py'))+pathlib.os.sep+"logs"+pathlib.os.sep+"logs.log"
logging.basicConfig(filename=_here, level=logging.ERROR)