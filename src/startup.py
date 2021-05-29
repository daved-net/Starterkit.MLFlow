import os
from dotenv import load_dotenv


class Startup:
    def __init__(self):
        print(os.environ['PROJECT_DIR'])