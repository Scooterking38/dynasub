import re
import inspect
import importlib.util

frame = inspect.stack()[1]
module_name = frame[0].f_globals['__name__']
source = importlib.util.get_source(module_name)
lines = source.splitlines(keepends=True)

new_lines = []
for line in lines[1:]:
    if re.search(r'\$\{(\w+)\}', line):
        indent = line[:len(line) - len(line.lstrip())]  # preserve indentation
        inner = line.strip().strip('"').strip("'")
        inner = re.sub(r'\$\{(\w+)\}', r'{\1}', inner)
        new_lines.append(f"{indent}exec(f{repr(inner)}, globals())\n")
    else:
        new_lines.append(line)

exec(''.join(new_lines))
