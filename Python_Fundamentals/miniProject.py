# Project 1: Travel Suggestion Program

miles = float(input("How far would you like to travel in miles? "))

# Suggest mode of transport based on the distance
if miles < 3:
    print("I suggest Bicycle to your destination")
elif miles < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# Project 2: Server Hosting Cost Calculator

# Cost per hour in dollars
cost_per_hour = 0.51

# Calculate costs
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30  
budget = 918
days_with_budget = budget / cost_per_day

# Print results
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for approximately {days_with_budget:.2f} days.")