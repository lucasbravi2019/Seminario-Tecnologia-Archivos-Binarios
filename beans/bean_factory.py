from menu.menu_busqueda import MenuBusqueda
from menu.menu_inicial import MenuInicial
from repository.libro_repository import LibroRepository
from service.libro_service import LibroService


class BeanFactory:

    def __init__(self):
        self.libro_repository = LibroRepository()
        self.libro_service = LibroService(self.libro_repository)
        self.menu_busqueda = MenuBusqueda(self.libro_service)
        self.menu_inicial = MenuInicial(self.libro_service, self.menu_busqueda)

    def get_menu_inicial(self):
        return self.menu_inicial