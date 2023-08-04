def add(*args):
    return sum(args)


print(add(1, 2, 3))

def calculate(**kwargs):
    print(kwargs)

calculate(add=2, multiply=2)

dict = {"name": "Bulat"}
print(dict.get("name"))
print(dict.get("age"))