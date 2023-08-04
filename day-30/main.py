# try:
#     file = open("data.json")
#     dict = {"key": "value"}
#     print(dict["non_existing_key"])
# except FileNotFoundError:
#     file = open("data.json", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # raise TypeError("This is an error that I made up")
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")

bmi = weight / height ** 2
print(bmi)