from re import search

from Lab3.RedBlackTree import RedBlackTree

Tree = RedBlackTree()

def appendInFile(word):
    with open('dictionary.txt', "a") as file:
        file.write(word + "\n")

def load_from_file():
    try:
        with open('Dictionary.txt', 'r') as f:
            for line in f:
                word = line.strip()
                if word:  # ignore empty lines
                    Tree.insert(word)
                    print(f"Inserted: {word}")
    except FileNotFoundError:
        print("Dictionary.txt file not found.")

def insertWord():
    word = input("Insert word: ")
    if Tree.search(word)==None:
        Tree.insert(word)
        appendInFile(word)
        Tree.print_tree_size()
        Tree.print_tree_height()
        Tree.print_black_height()
        print(f"Inserted: {word}")
    else:
        print(f"Word {word} already exists.")


def lookupWord():
    word = input("Insert word: ")
    if Tree.search(word)==None:
        print("No")
    else:
        print("Yes")


load_from_file()
while True:
    print("Enter 1 for insertion, 2 for Lookup, 3 for Exit")
    key = input()
    if key == "1":
        insertWord()
    if key == "2":
        lookupWord()
    if key == "3":
        print("Exiting...")
        exit()