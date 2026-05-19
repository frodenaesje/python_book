import sys
path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        print(f"{i:03}: {line.rstrip()}")
