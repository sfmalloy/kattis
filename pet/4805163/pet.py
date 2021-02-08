m_score = 0
m_player = 0
for i in range(0, 5):
    curr = sum(list(map(int, input().split())))
    if (curr > m_score):
        m_score = curr
        m_player = i + 1

print(m_player, m_score)
