stuck = int(input())
tree = {}

not_root = set()
possible_root = set()

line = list(map(int, input().split()))
while line[0] != -1:
  tree[line[0]] = line[1:]
  for b in tree[line[0]]:
    not_root.add(b)
  possible_root.add(line[0])
  line = list(map(int, input().split()))

root = 0
for r in possible_root:
  if r not in not_root:
    root = r
    break

def find_path(a, p):
  if a == stuck:
    return p
  path = []
  if a in possible_root:
    for b in tree[a]:
      path += find_path(b, [b] + p.copy())
  return path

[print(p, end=' ') for p in (find_path(root, []) + [root])]
print()