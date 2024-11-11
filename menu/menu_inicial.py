from menu.menu_busqueda import MenuBusqueda
from service.libro_service import LibroService


class MenuInicial:

    def __init__(self, libro_service: LibroService, menu_busqueda: MenuBusqueda):
        self.libro_service = libro_service
        self.menu_busqueda = menu_busqueda
        self.acciones = {'1': self.libro_service.crear_libro, '2': self.libro_service.editar_libro,
                         '3': self.libro_service.borrar_libro, '4': self.menu_busqueda.mostrar_menu}

    def mostrar_menu(self):
        print('Bienvenido a la biblioteca')
        print('Qué desea hacer?')
        print('1. Crear nuevo libro')
        print('2. Editar libro')
        print('3. Borrar libro')
        print('4. Buscar libros')
        print('5. Salir')

        opcion = input()
        if opcion == '5':
            return

        accion = self.acciones.get(opcion)

        if accion is None:
            print('Seleccionó una acción inválida, por favor intente nuevamente')
            self.mostrar_menu()
        else:
            accion()
            self.mostrar_menu()
