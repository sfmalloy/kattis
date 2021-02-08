T = int(input())
for _ in range(T):
  n = int(input())
  total_votes = 0
  votes = []
  for _ in range(n):
    i = int(input())
    total_votes += i
    votes.append(i)
  winner_total = max(votes)
  if votes.count(winner_total) > 1:
    print('no winner')
  elif winner_total > total_votes // 2:
    print(f'majority winner {votes.index(winner_total)+1}')
  else:
    print(f'minority winner {votes.index(winner_total)+1}')