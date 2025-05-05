#Выполнение 100 000 операций имитационного моделирования, для реализации займет много Вывод сообщений о каждых
# 10 000 операций обратная связь демонстрирует пользователю программа не зависла
import datetime, random
from calendar import month
from http.cookiejar import MONTHS


#Возвращение списка объектов дат дней рождения
def getBrithdays(number0fBirthdays):
    birthday = []
    for i in range(number0fBirthdays):
        #Год в иматации роли не играет, лишь бы в объектах дней рождений он был одинаков
        start0Year = datatime.data(2025, 1, 1)
        #Получаем случайный день года
        number0fBirthdays = datatime.timedelta(random.randit(0, 364))
        birthday = start0Year + randomNumber0fDays
        birthday.append(birthday)
    return birthday
#для возвращения объектов даты для рождения, в котором встречаются несколько раз в спике дней рождений
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA
#MAIN
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    response = int(input("Сколько дней рождения будем создавать? Макс 100:"))
    if response > 0 and response <= 100:
        numBDays = response
        break
print()
birthday = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(",",end='')
    monthName = MONTHS[birthday.month -1]
    dateText = f"{monthName, birthday.day}"
    print(dateText)
print()
print()
math = getMatch(birthdays)
print("Результаты симуляции:", end='')
if math != None:
    monthName = MONTHS[math.moth - 1]
    dateText = f"[monthName, math.day"
    print(f"Люди имеющие такую дату: {dateText}")
else:
    print("Не удалось найти людей с такой датой")
print()
print("Начинается проверка 100 000 вариаций")
input("Нажмите Enter, чтобы начать...")
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'Симуляция идет...')
    birthday = getBrithdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("Симуляция успешно закончена!")
print(f"Дней рождений: {numBDays}")
print(f"Кол-во совпадений: {simMatch}")


