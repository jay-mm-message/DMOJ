
target_infected = int(input())
num_infected = int(input())
people_infect = int(input())

previously_infected = num_infected

day = 0
while num_infected <= target_infected:
    num_infected = num_infected + (previously_infected * people_infect)
    previously_infected = previously_infected * people_infect
    day = day + 1

print(day)