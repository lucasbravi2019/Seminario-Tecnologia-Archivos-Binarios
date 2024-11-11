from service.libro_service import LibroService


class MenuBusqueda:

    def __init__(self, libro_service: LibroService):
        self.libro_service = libro_service
        self.acciones = {'1': self.libro_service.listar_autores_existentes, '2': self.libro_service.mostrar_libros,
                         '3': self.libro_service.listar_libros_por_genero, '4': self.libro_service.listar_libros_por_autor,
                         '5': self.libro_service.listar_libros_por_editorial, '6': self.libro_service.listar_libros_por_editorial_edicion,
                         '7': self.libro_service.listar_autores_editorial, '8': self.libro_service.listar_libros_editados,
                         '9': self.libro_service.listar_libros_inicial_autor, '10': self.libro_service.listar_libros_titulo}

    def mostrar_menu(self):
        print('1. Listar autores existentes')
        print('2. Listar libros existentes')
        print('3. Consultar libro por género')
        print('4. Listar libros por autor')
        print('5. Listar libros por editorial')
        print('6. Listar libros por editorial en rangos de años de edición')
        print('7. Listar autores según editorial')
        print('8. Listar libros editados según año')
        print('9. Listar libros según letra inicial de autor')
        print('10. Listar libros según palabra en título')
        print('11. Salir')

        opcion = input()

        if opcion == '11':
            return

        accion = self.acciones.get(opcion)

        if accion is None:
            print('Seleccionó una acción inválida, por favor intente nuevamente')
            self.mostrar_menu()
        else:
            accion()
            self.mostrar_menu()