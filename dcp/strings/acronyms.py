def create_acronym(text):
    a = " "
    for i in text:
        a = a + str(i[0]).upper()
    return a


if __name__ == "__main__":
    user_input = str(input("Enter a Phrase: "))
    text = user_input.split()
    print(create_acronym(text))
