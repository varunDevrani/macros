from pathlib import Path
import shutil


root = Path("src")

for cache in root.rglob("__pycache__"):
	shutil.rmtree(cache)
	print(f"Removed: {cache}")