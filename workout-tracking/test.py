from pprint import pprint

D = {"a": 1, "c": 3, "b": 2}

# for key in sorted(D):
#     print(D[key])

T = 'spam', 3.0, [11, 22, 33]
# print(T[1])

# f = open('data.txt', 'w')
# f.write('Hello\n')
# f.write('world\n')
# f.close()

# f = open('data.txt')
# text = f.read()
# print(text)
# # pprint(dir(f))
# f.close()

# for line in open('data.txt'):
#     print(line)

X = set('spam')
Y = {'h', 'a', 'm'}
# print(X, Y)
# print(X & Y) # пересечение
# print(X | Y) # объединение
# print(X - Y) # разность

# print({1, 2, 3} == {2, 1, 3})

L = [1, 2, 3]
# print(isinstance(L, str))


# print(4 // 3)

print(list({letter: None for letter in 'acknowledge'}.keys()))

"""
L1, L2 = [1, 3, 5], [5, 1, 3]
print(set(L1) == set(L2))
"""

menu = (
    "spam\n"  # comments here will be ignored
    "eggs"
)

print(menu)

for c in range(48, 58):
    print(chr(c))

print('That is %d %s bird!' % (1, 'dead'))
print('That is {0} {1} bird!'.format(1, 'dead'))

print('hello'.count('l'))
