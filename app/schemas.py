import importlib
import os

from app.database.base import Base

EXCLUDE_FOLDERS = ["__pycache__", "database"]

base_path = os.path.dirname(__file__)
package_name = os.path.basename(os.path.normpath(base_path))
for root, dirs, files in os.walk(base_path):
    for dir_item in dirs:
        if dir_item in EXCLUDE_FOLDERS:
            continue

        schemas_module_name = f"{package_name}.{root[len(base_path) + 1:].replace(os.path.sep, '.')}.{dir_item}.schemas"

        try:
            schemas_module = importlib.import_module(schemas_module_name)
        except ImportError as e:
            pass

__all__ = [Base]
