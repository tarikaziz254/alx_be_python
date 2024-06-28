task=input("Enter your task:")
priority=input("priority (high/medium/low)")
time_bound=input("Is it time-bound? (yes/no):")
match priority:
    case 'high':
        if time_bound == 'yes':
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        if time_bound == 'no':
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == 'yes':
            print("Reminder: 'Finish project report' is a medium priority task that requires immediate attention today!")
        if time_bound == 'no':
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'yes':
            print("Reminder: 'Finish project report' is a low priority task but it has a time bound that requires immediate attention today!")
        if time_bound == 'no':
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
