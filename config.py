# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI = 'postgresql://wuluoyu:password@localhost/backend'
DATABASE_CONNECT_OPTIONS = {}
