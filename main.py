
def fizzbuzz():
    for i in range(1,101):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Bang"
        if word == "":
            print(i)
        else:
            print(word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
