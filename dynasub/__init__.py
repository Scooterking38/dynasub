import re, inspect

path = inspect.stack()[1].filename
with open(path) as f:
    lines = f.readlines()

env = {}
for line in lines[1:]:
    if re.search(r'\$\{(\w+)\}', line):
        line = re.sub(r'\$\{(\w+)\}', r'{\1}', line)
        line = f"exec(f{repr(line.strip())}, globals())\n"
    exec(line, env)
