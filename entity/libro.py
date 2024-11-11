from typing import List

class Libro:

    titulo: str
    autores: List[str]
    paginas: int
    isbn: str
    año_edicion: int
    editorial: str
    genero: str

    def __init__(self, titulo: str, autores: List[str], paginas: int, isbn: str, año_edicion: int, editorial: str,
                 genero: str):
        self.titulo = titulo
        self.autores = autores
        self.paginas = paginas
        self.isbn = isbn
        self.año_edicion = año_edicion
        self.editorial = editorial
        self.genero = genero

    def __eq__(self, other):
        if isinstance(other, Libro):
            if self.isbn == other.isbn:
                return True

        return False

    def __hash__(self):
        return hash(self.isbn)

    def __str__(self):
        return (f'\nTítulo: {self.titulo}\n'
                f'Autores: {', '.join(self.autores)}\n'
                f'Páginas: {self.paginas}\n'
                f'ISBN: {self.isbn}\n'
                f'Año de edición: {self.año_edicion}\n'
                f'Editorial: {self.editorial}\n'
                f'Género: {self.genero}')

    def to_dict(self):
        return {'titulo': self.titulo, 'autores': self.autores, 'paginas': self.paginas, 'isbn': self.isbn,
                'anio_edicion': self.año_edicion, 'editorial': self.editorial, 'genero': self.genero}

