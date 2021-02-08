n = int(input())

candidates = {}
for _ in range(n):
  name = input()
  party = input()
  candidates[name] = party

votes = {c:0 for c in candidates}
m = int(input())
for _ in range(m):
  name = input()
  if name in votes:
    votes[name] += 1

vote_amts = [votes[c] for c in votes]

if vote_amts.count(max(vote_amts)) != 1:
  print('tie')
else:
  print(candidates[max(votes, key=lambda s:votes[s])])
