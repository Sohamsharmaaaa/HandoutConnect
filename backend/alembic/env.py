import sys
import os

# Add backend directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.database import Base  # Now this will work

# Alembic config
from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool

# Load config file
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for Alembic
target_metadata = Base.metadata
