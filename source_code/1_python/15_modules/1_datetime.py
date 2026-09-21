from datetime import datetime, timedelta

now = datetime.now()

print(now)  # 2026-09-21 21:51:35.764124

tomorrow = now + timedelta(days=1) # timedelta: represents a difference in time


# strftime() formats a date/time as a string
# | Code | Meaning           | Example     |
# | ---- | ----------------- | ----------- |
# | `%Y` | 4-digit year      | `2026`      |
# | `%m` | Month number      | `09`        |
# | `%d` | Day               | `21`        |
# | `%B` | Full month name   | `September` |
# | `%A` | Full weekday name | `Monday`    |
# | `%H` | Hour (24-hour)    | `21`        |
# | `%M` | Minute            | `50`        |
# | `%S` | Second            | `01`        |


print(tomorrow.strftime("%Y-%m-%d"))  # 2026-09-22

print(now.strftime("%B %d, %Y"))  # September 21, 2026