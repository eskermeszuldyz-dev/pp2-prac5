import os
from pathlib import Path

# Create nested directories
Path("parent/child/grandchild").mkdir(parents=True, exist_ok=True)

# Current directory
print("Current directory:", os.getcwd())

# List contents
print("Directory contents:")
for item in Path(".").iterdir():
    print(item.name)

# Find .py files
py_files = list(Path(".").glob("*.py"))
print("Python files:", [f.name for f in py_files])
