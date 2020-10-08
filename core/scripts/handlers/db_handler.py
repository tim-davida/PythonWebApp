import mysql.connector

#
#  Класс обработчика обращений к базе данных
#
class DBHandler:

	# Данные для подключения к БД
    db_host   = "127.0.0.1"
    db_port   = "55555"
    db_user   = "root"
    db_passwd = ""
    db_name   = "HardwareListDB"

    # Инициализация обработчика и подключение к БД
    def __init__(self):
        self.connect = mysql.connector.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                passwd=self.db_passwd,
                database=self.db_name
            )
        self.cursor = self.connect.cursor()

    # Метод для обработки SQL запросов к БД
    def query(self, query, params=None):
        # Если параметров не указанно, что выполняем простой запрос
        if params is None:
            self.cursor.execute(query)
        # Если указан список параметров, то выполняем один большой запрос
        elif params is list:
            self.cursor.executemany(query, params)
        # Если параметр указан один, то выполняем запрос с ним
        else:
            self.cursor.execute(query, params)

        # Возвращаем полученный результат
        try:
            return self.cursor.fetchall()
        except:
            return None
