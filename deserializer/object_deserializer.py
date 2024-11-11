import pickle

def deserialize():
    try:
        with open('biblioteca.pkl', 'rb+') as file:
            try:
                return pickle.load(file)
            except EOFError:
                return set()
    except FileNotFoundError:
        with open('biblioteca.pkl', 'wb+') as _:
            return set()