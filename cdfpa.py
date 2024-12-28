import scipy.stats as stats 

days = int(input("enter expect value"))

prob1 = stats.poisson.pmf(days,10)

print(prob1)

day1 = int(input("enter expect value"))
day2 = int(input("enter expect value"))
day3 = int(input("enter expect value"))

prob2 = stats.poisson.pmf(day1,10)+stats.poisson.pmf(day2,10)+stats.poisson.pmf(day3,10)

print(prob2)