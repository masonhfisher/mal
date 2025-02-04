def read_(source: str) -> str:
    return source

def eval_(ast: str) -> str:
    return ast

def print_(form: str) -> str:
    return form

def rep(source: str) -> str:
    return print_(eval_(read_(source)))

while True:
    try:
        print(rep(input("user> ")))
    except (EOFError, KeyboardInterrupt):
        break
