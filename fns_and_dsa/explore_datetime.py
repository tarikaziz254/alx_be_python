from datetime import datetime,deltatime
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    def calculate_future_date():
        future_date = current_date + timedelta(days = number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%s")
        print(f"future date: {formatted_future_date}")
    calculate_future_date()

display_current_datetime()
