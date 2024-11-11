import pickle

from typing import Set
from entity.libro import Libro


def serialize(data: Set[Libro]):
    with open('biblioteca.pkl', 'wb+') as f:
        pickle.dump(data, f)
