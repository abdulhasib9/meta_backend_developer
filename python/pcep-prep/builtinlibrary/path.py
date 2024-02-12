from pathlib import Path

print(Path.home())
path = Path("builtinlibrary/path.py")
print(path.exists())
print(path.suffix)
print(path.stem)
print(path.absolute())