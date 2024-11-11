from entity.libro import Libro
from repository.libro_repository import LibroRepository


class LibroService:
    libro_repository: LibroRepository

    def __init__(self, libro_repository: LibroRepository):
        self.libro_repository = libro_repository

    def mostrar_libros(self):
        libros = self.libro_repository.get_libros()

        if len(libros) == 0:
            print('No hay libros')

        for libro in libros:
            print(libro)

    def mostrar_autores(self):
        autores = self.libro_repository.get_autores()

        if len(autores) == 0:
            print('No hay autores')
            return

        print('Autores')
        for autor in autores:
            print(autor)

    def crear_libro(self):
        titulo = self.validate_str('Ingrese el título del libro\n')
        autores = self.validate_autores('Ingrese los autores separados por coma (,). '
                                    'La primer palabra será considerada el nombre del autor y la segunda palabra '
                                    'como el apellido. En caso de sólo ingresar una, será considerada como el apellido\n')
        paginas = self.validate_int('Ingrese la cantidad de páginas del libro\n')
        isbn = self.validate_str('Ingrese el isbn del libro\n')
        año_edicion = self.validate_int('Ingrese el año de edición del libro\n')
        editorial = self.validate_str('Ingrese la editorial del libro\n')
        genero = self.validate_str('Ingrese el género del libro\n')

        libro = Libro(titulo, autores.split(','), paginas, isbn, año_edicion, editorial, genero)
        existe = self.libro_repository.existe_libro(libro)

        if existe:
            print('El libro ya existe en la biblioteca')
        else:
            self.libro_repository.crear_libro(libro)
            print('El libro fue creado con éxito')

    def editar_libro(self):
        libros = self.libro_repository.get_libros()

        if len(libros) == 0:
            print('No hay libros existentes')
            return

        print('Libros')
        for libro in libros:
            print(f'ISBN: {libro.isbn}, Título: {libro.titulo}')

        isbn = self.validate_str('Qué libro desea editar? Ingrese ISBN\n')
        if isbn not in [libro.isbn for libro in libros]:
            print('Ingresó un ISBN incorrecto, por favor intente nuevamente')
            self.editar_libro()
        else:
            titulo = self.validate_str('Ingrese el título del libro\n')
            autores = self.validate_autores('Ingrese los autores separados por coma (,)\n')
            paginas = self.validate_int('Ingrese la cantidad de páginas del libro\n')
            año_edicion = self.validate_int('Ingrese el año de edición del libro\n')
            editorial = self.validate_str('Ingrese la editorial del libro\n')
            genero = self.validate_str('Ingrese el género del libro\n')

            for libro in libros:
                if libro.isbn == isbn:
                    libro.titulo = titulo
                    libro.autores = autores.split(',')
                    libro.paginas = paginas
                    libro.año_edicion = año_edicion
                    libro.editorial = editorial
                    libro.genero = genero
                    self.libro_repository.editar_libro(libros)
                    print('El libro fue editado con éxito')
                    return

        print('No se encontró el libro para editar')

    def borrar_libro(self):
        libros = self.libro_repository.get_libros()

        if len(libros) == 0:
            print('No hay libros existentes')
            return

        print('Libros')
        for libro in libros:
            print(f'ISBN: {libro.isbn}, Título: {libro.titulo}')

        isbn = self.validate_str('Qué libro desea borrar? Ingrese ISBN\n')
        if isbn not in [libro.isbn for libro in libros]:
            print('Ingresó un ISBN incorrecto, por favor intente nuevamente')
            self.borrar_libro()
        else:
            self.libro_repository.borrar_libro(isbn)
            print('El libro fue borrado con éxito')

    def listar_autores_existentes(self):
        libros = self.libro_repository.get_libros()
        autores = {autor for libro in libros for autor in libro.autores}

        if len(autores) == 0:
            print('No hay autores existentes')
            return

        for autor in autores:
            print(autor)

    def listar_libros_por_genero(self):
        genero = self.validate_str('Ingrese qué género de libros quiere buscar\n').lower()
        libros = self.libro_repository.get_libros()

        libros = {libro for libro in libros if libro.genero.lower() == genero}
        if len(libros) == 0:
            print(f'No hay libros para el género: {genero.title()}')
            return

        for libro in libros:
            print(libro)


    def listar_libros_por_autor(self):
        autor = self.validate_str('Ingrese qué autor de libros quiere buscar\n').lower()
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros for autor_libro in libro.autores if autor_libro.lower() == autor}

        if len(libros) == 0:
            print(f'No hay libros para el autor: {autor.title()}')
            return

        for libro in libros:
            print(libro)

    def listar_libros_por_editorial(self):
        editorial = self.validate_str('Ingrese qué editorial de libros quiere buscar\n').lower()
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros if libro.editorial.strip().lower() == editorial}

        if len(libros) == 0:
            print(f'No hay libros para la editorial: {editorial.title()}')
            return

        for libro in libros:
            print(libro)

    def listar_libros_por_editorial_edicion(self):
        editorial = self.validate_str('Ingrese qué editorial de libros quiere buscar\n').lower()
        minimo = self.validate_int('Ingrese el año desde el que quiere buscar\n')
        maximo = self.validate_int('Ingrese el año hasta el que quiere buscar\n')
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros if libro.editorial.strip().lower() == editorial
                  and minimo <= libro.año_edicion <= maximo}

        if len(libros) == 0:
            print(f'No hay libros para la editorial o para las fechas pedidas: {editorial.title()}, {minimo} - {maximo}')
            return

        for libro in libros:
            print(libro)

    def listar_autores_editorial(self):
        editorial = self.validate_str('Ingrese qué editorial de libros quiere buscar\n').lower()
        libros = self.libro_repository.get_libros()
        autores = {autor for libro in libros for autor in libro.autores if libro.editorial.strip().lower() == editorial}

        if len(autores) == 0:
            print(f'No hay autores para la editorial seleccionada: {editorial.title()}')
            return

        for autor in autores:
            print(autor)

    def listar_libros_editados(self):
        año_edicion = self.validate_int('Ingrese el año de edición de los libros a buscar\n')
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros if libro.año_edicion == año_edicion}

        if len(libros) == 0:
            print(f'No hay libros para el año de edición seleccionado: {año_edicion}')
            return

        for libro in libros:
            print(libro)

    def listar_libros_inicial_autor(self):
        inicial = self.validate_str('Ingrese la inicial del apellido del autor a buscar\n').lower()
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros for autor in libro.autores if len(autor.split()) == 1 and autor[0].lower() == inicial
                  or len(autor.split()) == 2 and autor.split()[1].lower()[0] == inicial}

        if len(libros) == 0:
            print(f'No hay libros para la inicial seleccionada: {inicial}')
            return

        for libro in libros:
            print(libro)

    def listar_libros_titulo(self):
        palabra = self.validate_str('Ingrese la palabra que debe contener el título\n').lower()
        libros = self.libro_repository.get_libros()
        libros = {libro for libro in libros if palabra in libro.titulo.lower().split()}

        if len(libros) == 0:
            print(f'No hay libros para la palabra seleccionada: {palabra}')
            return

        for libro in libros:
            print(libro)

    def validate_str(self, text):
        value = input(text)
        if len(value) == 0:
            print('El valor ingresado está vacío, por favor intente nuevamente')
            return self.validate_str(text)
        else:
            return value

    def validate_int(self, text):
        try:
            return int(input(text))
        except ValueError:
            print('El valor ingresado no es un entero, por favor intente nuevamente')
            return self.validate_int(text)

    def validate_autores(self, text):
        autores = self.validate_str(text)
        lista_autores = autores.split(',')

        if len(lista_autores) > 3:
            print('Ingresó más de 3 autores. El límite es de 3 autores por libro.')
            autores = self.validate_autores(text)
        else:
            for autor in lista_autores:
                nombre_apellido = autor.split()

                if len(nombre_apellido) > 2:
                    print('Ingresó más de 2 palabras. Ingrese apellido o nombre y apellido separados (max 2 palabras)')
                    autores = self.validate_autores(text)

        return autores