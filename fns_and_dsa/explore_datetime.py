from datetime import datetime,deltatime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    def calculate_future_date():
        future_date = current_date + datetime.timedelta(days = number_of_days)
        print(f"future date: {future_date}")
    calculate_future_date()

display_current_datetime()
