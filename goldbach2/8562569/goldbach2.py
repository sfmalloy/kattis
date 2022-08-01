from collections import defaultdict

def get_primes(mx):
    primes = [True for _ in range(mx+1)]
    primes[0] = primes[1] = False
    p = 2
    while p * p <= mx:
        for i in range(p*p, mx+1, p):
            primes[i] = False
        p += 2 if p != 2 else 1
        while p <= mx and not primes[p]:
            p += 2
    return primes

def main():
    n = int(input())
    nums = set(int(input()) for _ in range(n))
    is_prime = get_primes(max(nums))

    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    d = defaultdict(list)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            s = primes[i] + primes[j]
            if s in nums:
                d[s].append((primes[i], primes[j]))

    for g in nums:
        print(f'{g} has {len(d[g])} representation(s)')
        for p in d[g]:
            print(f'{p[0]}+{p[1]}')
        print()

if __name__ == '__main__':
    main()
