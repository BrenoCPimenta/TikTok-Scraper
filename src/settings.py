import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load sensible data
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Set paths
os.environ['PROJECT_DIR'] = os.path.dirname(os.path.abspath(__file__))
# ------------------------------------DRIVERS-----------------------------------
os.environ['CHROME'] = os.getenv('PROJECT_DIR') + '/../resources/drivers/chromedriver'
os.environ['FIREFOX'] = os.getenv('PROJECT_DIR') + '/../resources/drivers/geckodriver'
