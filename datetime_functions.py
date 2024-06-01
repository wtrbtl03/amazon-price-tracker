from datetime import datetime, timedelta

# ist_delta = timedelta(hours=5, minutes=30)
ist_delta = timedelta(hours=0, minutes=0)


def curr_time():
    curr_datetime = datetime.now()
    curr_time = (curr_datetime+ist_delta).strftime("%H:%M")
    return curr_time


def curr_timestamp():
    curr_datetime = datetime.now()
    curr_timestamp = (curr_datetime+ist_delta).strftime("%Y-%m-%d %H:%M:%S")
    return curr_timestamp
