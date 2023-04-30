import pandas as pd    # by Kirill Kasparov, 2023
import datetime
import calendar


def workind_days():
    # Получаем дату из любого источника. В примере берем текущую
    ddf = datetime.datetime.now()

    # Список праздничных дней
    holidays = pd.read_excel('holidays.xlsx')
    # Конвертируем дату из Excel формата в datetime формат
    for col in holidays.columns:
        holidays[col] = pd.to_datetime(holidays[col]).dt.date

    # Начальная и конечная дата текущего месяца
    start_date = datetime.date(int(ddf.strftime('%Y')), int(ddf.strftime('%m')), 1)
    now_date = datetime.date(int(ddf.strftime('%Y')), int(ddf.strftime('%m')), int(ddf.strftime('%d')))
    end_date = datetime.date(int(ddf.strftime('%Y')), int(ddf.strftime('%m')),
                             calendar.monthrange(now_date.year, now_date.month)[1])

    # Вычисляем количество рабочих дней
    now_working_days = 0
    end_working_days = 0

    current_date = start_date
    while current_date <= end_date:
        # Если текущий день не является выходным или праздничным, увеличиваем счетчик рабочих дней
        if current_date in list(holidays['working_days']):  # рабочие дни исключения
            now_working_days += 1
            end_working_days += 1
        elif current_date.weekday() < 5 and current_date not in list(holidays[int(ddf.strftime('%Y'))]):
            if current_date < now_date:
                now_working_days += 1
            end_working_days += 1
        current_date += datetime.timedelta(days=1)

    # Получаем данные прошлого года
    start_date_2 = datetime.date(int(ddf.strftime('%Y')) - 1, int(ddf.strftime('%m')), 1)
    now_date_2 = datetime.date(int(ddf.strftime('%Y')) - 1, int(ddf.strftime('%m')), int(ddf.strftime('%d')))
    end_date_2 = datetime.date(int(ddf.strftime('%Y')) - 1, int(ddf.strftime('%m')),
                               calendar.monthrange(now_date_2.year, now_date_2.month)[1])
    now_working_days_2 = 0
    end_working_days_2 = 0

    current_date = start_date_2
    while current_date <= end_date_2:
        # Если текущий день не является выходным или праздничным, увеличиваем счетчик рабочих дней
        if current_date in list(holidays['working_days']):  # рабочие дни исключения
            now_working_days_2 += 1
            end_working_days_2 += 1
        elif current_date.weekday() < 5 and current_date not in list(holidays[int(ddf.strftime('%Y'))]):
            if current_date < now_date_2:
                now_working_days_2 += 1
            end_working_days_2 += 1
        current_date += datetime.timedelta(days=1)
    date_lst = [start_date, start_date_2, now_date, now_date_2, end_date, end_date_2, now_working_days, now_working_days_2, end_working_days, end_working_days_2]
    return date_lst


start_date, start_date_2, now_date, now_date_2, end_date, end_date_2, now_working_days, now_working_days_2, end_working_days, end_working_days_2 = workind_days()
print('Начало месяца:', start_date, 'в прошлом году', start_date_2)
print('Отчетная дата:', now_date, 'в прошлом году', now_date_2)
print('Конец месяца', end_date, 'в прошлом году', end_date_2)
print('Рабочих дней сейчас', now_working_days, 'в прошлом году', now_working_days_2)
print('Всего рабочих дней', end_working_days, 'в прошлом году', end_working_days_2)

