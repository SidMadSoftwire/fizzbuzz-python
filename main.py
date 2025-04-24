
def fizzbuzz():
    for i in range(1,300):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Bang"
        if i % 11 == 0:
            word = "Bong"
        if i % 13 == 0:
            b_loc = word.find("B")
            if b_loc != -1:
                word = f"{word[:b_loc]}Fezz{word[b_loc:]}"
            else:
                word += "Fezz"
        if word == "":
            print(i)
        else:
            print(word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
