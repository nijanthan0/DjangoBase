from __future__ import unicode_literals

from os.path import dirname, join, abspath

import dotenv


def load_env():
    """Get the path to the .env file and load it."""
    project_dir = abspath(join(dirname(__file__), '../..', '..', '..'))
    dotenv.read_dotenv(join(project_dir, 'nijanthan/practise/base_pro/.env'))
