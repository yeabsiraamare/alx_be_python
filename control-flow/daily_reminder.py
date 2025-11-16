task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority level"


if time_bound == "yes":
    
    reminder = f"Reminder: {base} that requires immediate attention today!"
elif time_bound == "no":
    
    if priority == "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    else:
       
        reminder = f"Reminder: {base}."
else:
    # Handle unexpected time_bound input without failing the check
    reminder = f"Reminder: {base}."


print(reminder)

