import cherrypy

from .pages.homepage import HomePage
from .pages.testpage import TestPage
from .pages.data_access import DataAccess

#
#  Главный класс приложения
#
class Application:

    # Статический метод, который создаёт приложение
    @staticmethod
    def create_app():
        app = HomePage()
        app.testpage = TestPage()
        app.data = DataAccess()
        return app
