import calendar
from datetime import datetime
def get_all_mondays(year):
    _list = []

    for m in range(1, 13):
        dm = calendar.monthrange(year, m)[1]
        flag = 0
        for d in range(1, dm+1):
            if calendar.weekday(int(year), m, d) == 3:
                flag += 1
                if flag == 3:
                    _list.append(datetime(int(year), m, d).strftime('%d.%m.%Y'))

    return _list

print(*get_all_mondays(2021), sep="\n")




