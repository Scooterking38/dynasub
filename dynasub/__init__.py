import re
import codecs

def transform(source):
    lines = source.splitlines(keepends=True)
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
    return ''.join(new_lines)

def decode(source_bytes, errors='strict'):
    return transform(source_bytes.decode('utf-8', errors)), len(source_bytes)

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, source_bytes, final=False):
        return transform(source_bytes.decode('utf-8', self.errors))

class StreamReader(codecs.StreamReader):
    def decode(self, source_bytes, errors='strict'):
        return decode(source_bytes, errors)

info = codecs.CodecInfo(
    name='dynasub',
    encode=codecs.lookup('utf-8').encode,
    decode=decode,
    incrementaldecoder=IncrementalDecoder,
    streamreader=StreamReader,
)

codecs.register(lambda name: info if name == 'dynasub' else None)
