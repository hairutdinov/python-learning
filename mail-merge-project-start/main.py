PLACEHOLDER = "[name]"
names_list = []

with open("./Input/Names/invited_names.txt") as invited_names_file:
    names_list.extend(map(lambda n: n.strip(), invited_names_file.readlines()))

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    letter_content = starting_letter_file.read()
    for name in names_list:
        letter = letter_content.replace(PLACEHOLDER, name)
        file_name = "letter_for_" + name.replace(' ', '_') + ".txt"
        with open(f"./Output/ReadyToSend/{file_name}", "w") as letter_file:
            letter_file.write(letter)

