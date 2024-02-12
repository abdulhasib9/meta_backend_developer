from pathlib import Path

print(Path.home())
path = Path("/Users/thebeast/Documents/meta_backend_developer/builtinlibrary/path.py")
# print(path.exists())
# print(path.suffix)
# print(path.stem)
# print(path.absolute())
print(path.stat())
