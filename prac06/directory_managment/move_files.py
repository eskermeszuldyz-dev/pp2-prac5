import shutil
from pathlib import Path

source = Path("sample.txt")
destination_dir = Path("parent/child")

destination_dir.mkdir(parents=True, exist_ok=True)

# Move file
if source.exists():
    shutil.move(str(source), str(destination_dir / source.name))
    print("File moved successfully.")