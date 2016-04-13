from os import getenv
import pymssql
import xlsxwriter
import getpass

def sql_import_by_area():
    # Задаем реквизиты подключения к серверу БД
    server = '192.168.5.1'#input('Адрес сервера: ')
    user = 'sa'#input('Логин SQL: ')
    password = 'Admin01'#getpass.getpass('Пароль SQL: ')

    #Подключаемся к серверу
    connect = pymssql.connect(server, user, password, 'ST-MATIX')
    cursor = connect.cursor(as_dict = True)

    cursor.execute('select AreaID, Describtion from [dbo].[AreaDescr]')
    print('Список областей')
    areas = []
    for area_desc in cursor:
        if area_desc['AreaID'] >= 0:
            print(area_desc['Describtion'], ' : ', area_desc['AreaID'])
            areas.append(area_desc['AreaID'])

    #Выполняем Запрос
    while True:
        area = input('Введите ID области (по умолчанию 0) :')
        if int(area) in areas:
            break
        print('Зоны нет в списке')

    cursor.execute('''

    select dev.[DevNum]
          ,obj.[DefaultName]
          ,obj.[TechComment]
          ,convert(varchar, dateadd(hour, 3, coord.[NavTime])) as NavTime
    from [ST-MATIX].[dbo].[Objects] as obj
    join [ST-MATIX].[dbo].[DevicesOnObjects] as doo on obj.[ObjectId] = doo.[ObjectID]
    join [ST-MATIX].[dbo].[Devices] as dev on doo.[DeviceID] = dev.[DeviceID]
    left join [ST-MATIX].[dbo].[ObjectsCoords] as coord on obj.[ObjectID] = coord.[ObjectID]
    where (obj.AreaID = {}) and (coord.[NavTime] < convert(date, (getdate())) or coord.[NavTime] is NULL)
    order by [NavTime] desc

                '''.format(area))
    #Возвращаем список из строк выборки. Каждая строка - словарь, ключи - имена полей
    return list(cursor)


def write_to_excel(cursor):

    #Создаем файл и лист
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()
    #формат для жирного шрифта
    bold = workbook.add_format({'bold' : True})

    #Вытаскиваем имена полей
    fields_names = list(list(cursor)[0].keys())

    #Создаем заголовок таблицы
    for i, field in enumerate(fields_names):
        worksheet.write(0, i, field, bold)

    #Идем по каждой строке -> идем по каждому полю -> записываем значение поля в одноименный столбец
    for row, ts in enumerate(cursor, start = 1):
        print(ts)
        for col, field in enumerate(fields_names):
            worksheet.write(row,col,ts[field])

    workbook.close()


def main():
    a = sql_import_by_area()
    write_to_excel(a)


if __name__ == '__main__':
    main()
