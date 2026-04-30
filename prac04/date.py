from datetime import datetime, date, timedelta

# 1 Subtract five days from current date
def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return current_date, new_date


# 2️ Print yesterday, today, tomorrow
def yesterday_today_tomorrow():
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow


# 3️ Drop microseconds from datetime
def drop_microseconds():
    now = datetime.now()
    without_microseconds = now.replace(microsecond=0)
    return now, without_microseconds


# 4️ Calculate difference between two dates in seconds
def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    return difference.total_seconds()


# Test block
if __name__ == "__main__":

    # Task 1
    current, minus_five = subtract_five_days()
    print("Current datetime:", current)
    print("Five days earlier:", minus_five)

    print("\n--------------------")

    # Task 2
    yest, tod, tom = yesterday_today_tomorrow()
    print("Yesterday:", yest)
    print("Today:", tod)
    print("Tomorrow:", tom)

    print("\n--------------------")

    # Task 3
    original, no_micro = drop_microseconds()
    print("Original datetime:", original)
    print("Without microseconds:", no_micro)

    print("\n--------------------")

    # Task 4
    d1 = datetime(2024, 1, 1, 12, 0, 0)
    d2 = datetime(2024, 1, 2, 12, 0, 0)
    seconds = date_difference_in_seconds(d1, d2)
    print("Difference in seconds:", seconds)