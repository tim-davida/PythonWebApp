# Костыль для того, чтобы python подтягивал модули из текущей папки
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Импорт библиотеки веб-серванта
import cherrypy
# Импорт самого приложения
from scripts.application import Application

# Главная функция
def main():
    # Настройки сервера
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        },
        '/data/hardware': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/data/hardware_types': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    # Запуск сервера
    cherrypy.quickstart(Application.create_app(), config=conf)

if __name__ == '__main__':
    main()
