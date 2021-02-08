N, M, K = map(int, input().split())

plot_sizes = sorted(list(map(int, input().split())))
circle_houses = sorted(list(map(int, input().split())), reverse=True)
square_houses = sorted(list(map(int, input().split())), reverse=True)


def cs(plot_sizes):
  total = 0
  for c in circle_houses:
    for r in plot_sizes:
      if c < r:
        total += 1
        plot_sizes.remove(r)
        break

  for s in square_houses:
    for r in plot_sizes:
      if s**2 < 2*(r**2):
        total += 1
        plot_sizes.remove(r)
        break
  return total

def sc(plot_sizes):
  total = 0
  for s in square_houses:
    for r in plot_sizes:
      if s**2 < 2*(r**2):
        total += 1
        plot_sizes.remove(r)
        break

  for c in circle_houses:
    for r in plot_sizes:
      if c < r:
        total += 1
        plot_sizes.remove(r)
        break
  return total

print(max(cs(plot_sizes.copy()), sc(plot_sizes.copy())))