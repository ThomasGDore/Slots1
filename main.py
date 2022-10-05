import random

slots_total = 60
pulls_per_second = 1/10
pulls_per_minute = slots_total * pulls_per_second * 60

pulls_per_day = pulls_per_minute * 60 * 24
pulls_total = int(pulls_per_day)
print("Pulls per day multiplied by 1 in a million odds", pulls_total/1000000)

random_roll = 0
total_wins = 0

for j in range(10):
  for i in range(pulls_total):
    random_roll = random.randrange(1,1000001)
    if random_roll == 727272:
      total_wins += 1


print("average of wins across days", total_wins/10)