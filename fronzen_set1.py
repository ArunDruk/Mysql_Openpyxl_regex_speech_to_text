week_days=["Mon","Tue","Wed","Thu","Fri","sat","sun"]
print("Actual weekdays",week_days)

week_days[5]="week-off"

fixed_days=frozenset(week_days)
print("After modification",week_days)
print(type(fixed_days))

fixed_days[6]="week-off"
#frozenset(week_days)
print(week_days)

