import re, codecs

_pat = re.compile(r'["\']#\$')
_sub = re.compile(r'\$\{(\w+)\}')

def transform(src):
    lines = src.splitlines(keepends=True)
    out, i = [], 0

    while i < len(lines):
        line = lines[i]

        if _pat.match(line.strip()):
            indent = len(line) - len(line.lstrip())
            block = []

            while i < len(lines) and _pat.match(lines[i].strip()):
                s = lines[i].strip()[3:].strip()
                s = _sub.sub(r'{\1}', s.rstrip('"\''))
                block.append(s + '\n')
                i += 1

            out.append(f"{' '*indent}exec(f{repr(''.join(block))}, globals())\n")
        else:
            out.append(line)
            i += 1

    return ''.join(out)

def decode(b, errors='strict'):
    return transform(b.decode('utf-8', errors)), len(b)

info = codecs.CodecInfo(
    name='dynasub',
    encode=codecs.lookup('utf-8').encode,
    decode=decode
)

def search(name):
    if name.replace('-', '_') == "dynasub":
        return info
    return None

codecs.register(search)
