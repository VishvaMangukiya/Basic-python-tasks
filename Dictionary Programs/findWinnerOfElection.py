from collections import Counter

votes = ['Jay', 'Dax', 'Ronit', 'Isha', 'Jensi']

vote_count = Counter(votes)

winner = max(vote_count, key=vote_count.get)

print("Winner: ", winner)