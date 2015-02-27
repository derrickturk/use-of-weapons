# shorthand
# a crappy substitution system
# so i don't have to type as much

import sys
import re

mapping = [
    (re.compile(r"(?<!`)``(?!`)"), r'“'),
    (re.compile(r"(?<!')''(?!')"), r'”'),
    (re.compile(r'(?<!-)---(?!-)'), r'—'),
    (re.compile(r'(?<![!-])--(?![->])'), r'–'),
    ('(c)', '©'),
    ('(tm)', '™'),
    ('$FRAG$', '<!-- .element: class="fragment" -->')
]

def substitute(line):
    for orig, rep in mapping:
        if hasattr(orig, 'sub'):
            line = orig.sub(rep, line)
        else:
            line = line.replace(orig, rep)
    return line

def main(argv):
    if len(argv) > 2:
        print('Usage: {0} input-file'.format(argv[0]), file=sys.stderr)

    if len(argv) == 1:
        infile = sys.stdin
    else:
        infile = open(argv[1])

    for line in infile:
        sys.stdout.buffer.write(substitute(line).encode('utf-8'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
