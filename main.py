from bs4 import BeautifulSoup
import requests, sqlite3, datetime

# month_dict = {
#     'Январь': 1,
#     'Февраль': 2,
#     'Март': 3,
#     'Апрель': 4,
#     'Май': 5,
#     'Июнь': 6,
#     'Июль': 7,
#     'Август': 8,
#     'Сентябрь': 9,
#     'Октябрь': 10,
#     'Ноябрь': 11,
#     'Декабрь': 12
# }
#
#
# def get_max_id() -> int:
#     try:
#         sqlite_connection = sqlite3.connect('sqlite.db')
#         cursor = sqlite_connection.cursor()
#         T = cursor.execute("select max(id) from holidays").fetchall()
#         if T is not None:
#             return int(T[0][0]) + 1
#         else:
#             return 1
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#         return 0
#
#
# def add_holiday(month: str, day: int, name_of_holiday) -> bool:
#     try:
#         sqlite_connection = sqlite3.connect('sqlite.db')
#         cursor = sqlite_connection.cursor()
#         cursor.execute("INSERT INTO holidays VALUES({}, '{}.{}', '{}')".format(get_max_id(), day, month_dict[month], name_of_holiday))
#         sqlite_connection.commit()
#         return True
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#         return False
#
#
# get_max_id()
# url = 'https://my-calend.ru/holidays/2022'
# page = requests.get(url)
# print(page.status_code)
# soup = BeautifulSoup(page.text, "html.parser")
#
# allmonth = soup.findAll('section')
#
# for i in allmonth:
#     if i.div is not None:
#         print(i.div.text)
#         alltr = i.findAll('tr')
#         for j in alltr:
#             print(j.span.text.split(" ")[0])
#             alldiv = j.findAll('div')
#             for k in alldiv:
#                 if k.text:
#                     add_holiday(i.div.text, int(j.span.text.split(" ")[0]), k.text)

def get_holi() -> list:
    dt_obj = datetime.datetime.now()
    month = dt_obj.strftime("%m")
    day = dt_obj.strftime("%d")

    try:
         sqlite_connection = sqlite3.connect('sqlite.db')
         cursor = sqlite_connection.cursor()
         T = cursor.execute("select * from holidays where holiday = '{}.{}'".format(int(day), int(month))).fetchall()
         return T
    except sqlite3.Error as error:
         print("Ошибка при работе с SQLite", error)
         return []
