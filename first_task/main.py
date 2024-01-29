from datetime import datetime, timedelta


def schedule(a):
    expanded_list = []

    for start_date, end_date in a:
        current_date = start_date
        while current_date <= end_date:
            expanded_list.append(current_date)
            current_date += timedelta(days=1)

    return expanded_list

s = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

expanded_dates = schedule(s)

for date in expanded_dates:
    print(date)
