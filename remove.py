import os
import glob

# Define the path to your project
project_dir = 'path_to_your_project'

# Find all migration files
for migration_file in glob.glob(os.path.join(project_dir, '**/migrations/*.py'), recursive=True):
    if not os.path.basename(migration_file) == '__init__.py':
        os.remove(migration_file)
        print(f"Deleted: {migration_file}")

for migration_file in glob.glob(os.path.join(project_dir, '**/migrations/*.pyc'), recursive=True):
    os.remove(migration_file)
    print(f"Deleted: {migration_file}")
