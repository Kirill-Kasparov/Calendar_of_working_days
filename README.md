# Calendar_of_working_days
Считает количество рабочих дней

Предпосылки:
------------
В работе регулярно сталкиваюсь с необходимостью рассчитать среднесуточный оборот, чтобы сравнить отгрузки в динамике. Решение казалось бы простое, но количество нерабочих дней может отличаться, в зависимости от региона, поэтому готовые калькуляторы на просторах сети не нашел. Эту функцию написал при создании дашборда, который выводит kpi на текущую дату. Считаю её достаточно полезной, чтобы вынести отдельным проектом.

Описание
------------
Функция считает количество рабочих дней, исключая субботу и воскресенье. Все праздничные дни считываются из файла holidays.xlsx, календарь можно пополнять новыми годами и праздниками/нерабочими днями. 
Если рабочий день приходится на субботу или воскресенье, такую дату необходимо внести в колонку working_days в таблице holidays.xlsx

Например, если сегодня 27.04.2023
По результату выполнения, функция выводит 5 переменных текущего года и 5 переменных прошолого года:
1. Начало месяца: 2023-04-01 в прошлом году 2022-04-01
2. Отчетная дата: 2023-04-27 в прошлом году 2022-04-27
3. Конец месяца 2023-04-30 в прошлом году 2022-04-30
4. Рабочих дней сейчас 18 в прошлом году 18
5. Всего рабочих дней 20 в прошлом году 21

P.S.:
1. Текущий день за рабочий не учитывается. Чтобы включать текущий день, нужно добавить знак "<=" в выражение current_date < now_date
2. Чтобы вводить расчетную дату вручную, заменяем переменную ddf на ручной ввод:

now = input().split('.')
ddf = datetime.date(int(now[2]), int(now[1]), int(now[0]))
