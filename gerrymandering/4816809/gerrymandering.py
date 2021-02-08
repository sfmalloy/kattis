[p, d] = map(int, input().split())

def init_dist_dict(d):
    v = {}
    for i in range(1, d + 1):
        v[i] = 0
    return v

va = init_dist_dict(d)
vb = init_dist_dict(d)

for i in range(0, p):
    [curr_d, a, b] = map(int, input().split())
    va[curr_d] += a
    vb[curr_d] += b

wa = wb = total = 0
for dist in range(1, d + 1):
    winner = 'A' if va[dist] > vb[dist] else 'B'
    needed = ((va[dist] + vb[dist]) // 2) + 1
    wa_curr = wb_curr = 0
    
    if (winner == 'A'):
        wb_curr += vb[dist]
        wa_curr += abs(va[dist] - needed)
    else:
        wa_curr += va[dist]
        wb_curr += abs(vb[dist] - needed)
    
    wa += wa_curr
    wb += wb_curr
    total += va[dist] + vb[dist]

    print(winner, wa_curr, wb_curr)

print(abs(wa - wb) / total)
