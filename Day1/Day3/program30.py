dict1 = {m for m in dir(dict) if not m.startswith('_')}
print(dict1)