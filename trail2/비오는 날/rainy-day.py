class day_weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

weathers = []
for _ in range(n):
    date, day, weather = input().split()
    weathers.append(day_weather(date, day, weather))

weathers.sort(key = lambda x : x.date)

for i in weathers:
    if i.weather == 'Rain':
        print(i.date, i.day, i.weather)
        break