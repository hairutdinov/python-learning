# list = [1, 2, 3]
# print([n + 1 for n in list])
import pandas as pandas

# name = "Bulat"
# letters_list = [letter for letter in name]
# print(letters_list)

dict_1 = {"name": "Bulat", "age": 24}
list_1 = [1, 2]
# dict_2 = {item: "new_value" for item in list_1}
dict_2 = {key: "new_value" for (key, value) in dict_1.items() if key == "name"}
# print(dict_2)


student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

df = pandas.DataFrame(student_dict)
for (idx, row) in df.iterrows():
    print(idx)
    print(row.students)