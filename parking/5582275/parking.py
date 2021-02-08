class parked_truck:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.is_parked = False
    
    def __lt__(self, other):
        return self.stop < other.stop

    def __str__(self):
        return f'({self.start}, {self.stop}, {self.is_parked})'

rates = list(map(int, input().split()))
times = [(lambda a: parked_truck(a[0], a[1]))(list(map(int, input().split()))) for _ in range(3)]

start = min(truck.start for truck in times)
stop = max(truck.stop for truck in times)
cost = 0
for t in range(start, stop + 1):
    parked = 0
    # print(f't={t}: ', end='')
    for truck in times:
        if t == truck.stop:
            truck.is_parked = False
        
        if t == truck.start or truck.is_parked:
            parked += 1
            if t == truck.start:
                truck.is_parked = True
            # print(str(truck), end=' ')
    # print('')
    if parked > 0:
        cost += parked * rates[parked - 1]

print(cost)