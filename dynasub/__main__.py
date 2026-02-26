import re, sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    if re.match(r'["\']#\$', stripped):
        indent = len(line) - len(line.lstrip())
        block = []
        while i < len(lines) and re.match(r'["\']#\$', lines[i].strip()):
            s = lines[i].strip()
            inner = re.sub(r'^["\']#\$\s?', '', s).rstrip('"\'')
            inner = re.sub(r'\$\{(\w+)\}', r'{\1}', inner)
            block.append(inner + '\n')
            i += 1
        block_str = repr(''.join(block))
        new_lines.append(f"{' ' * indent}exec(f{block_str}, globals())\n")
    else:
        new_lines.append(line)
        i += 1

exec(compile(''.join(new_lines), sys.argv[1], 'exec'))
