import re
import inspect
import importlib.util

# Get the caller's frame
frame = inspect.stack()[1]

# Get the module name from the caller's globals
module_name = frame[0].f_globals['__name__']

# Use importlib to get the source — works everywhere
source = importlib.util.get_source(module_name)
lines = source.splitlines(keepends=True)

env = {}
for line in lines[1:]:
    if re.search(r'\$\{(\w+)\}', line):
        line = re.sub(r'\$\{(\w+)\}', r'{\1}', line)
        line = f"exec(f{repr(line.strip())}, globals())\n"
    exec(line, env)
