# def spin_words(sentence):
#     return ' '.join([word if len(word) < 5 else word[::-1] for word in sentence.split()])
#
# print(spin_words('Hey fellow warriors'))


def to_jaden_case(string):
    return ' '.join([w.capitalize() for w in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
