from deserializer.object_deserializer import deserialize
from entity.libro import Libro
from typing import Set

from serializer.object_serializer import serialize


class LibroRepository:

    def get_libros(self) -> Set[Libro]:
        return deserialize()

    def get_autores(self):
        autores = set()

        libros = deserialize()
        for libro in libros:
            for autor in libro.autores:
                autores.add(autor.title())

        return autores

    def existe_libro(self, libro: Libro):
        libros = self.get_libros()
        return libro in libros

    def crear_libro(self, libro: Libro):
        libros = self.get_libros()
        libros.add(libro)
        serialize(data=libros)

    def editar_libro(self, libros: Set[Libro]):
        serialize(data=libros)

    def borrar_libro(self, isbn: str):
        libros = self.get_libros()
        libros = {libro for libro in libros if libro.isbn != isbn}
        serialize(data=libros)