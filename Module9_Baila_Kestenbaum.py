"""
This program reads a poem from poem.txt, prints it normally,
prints it backwards, writes the reversed poem into poem2.txt,
and finally appends my name and a short explanation to the file.
"""

import os

DOCS_DIR = "docs"  # folder where all text files (the poem) are stored
PATH = ""  # global variable that stores the current file path


def read():
    """
    Reads the poem from poem.txt and prints it line by line.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem.txt")  # set PATH to poem.txt
    print(PATH)  # show which file is being opened

    with open(PATH, "r") as f:
        # loop through every line in the file
        for lines in f:
            # strip whitespace and print the clean line
            print(lines.strip().replace("\n", ""))


def read_backwards():
    """
    Reads the poem from poem.txt and returns the reversed text
    (last line to first line). Also prints the reversed lines.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem.txt")
    print(PATH)  # print to show the file being opened

    # open poem.txt and read all lines at once
    with open(PATH, "r") as f:
        lines = f.readlines()  # store lines in a list

    # print each line in reverse order
    for line in reversed(lines):
        print(line.strip())

    # return the reversed poem as one combined string
    return "".join(reversed(lines))


def write():
    """
    Writes the reversed poem into poem2.txt.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem2.txt")  # switch PATH to poem2.txt
    print(PATH)  # show where we're writing

    # open poem2.txt for writing (this overwrites the file)
    with open(PATH, "w") as f:
        f.write(read_backwards())  # write reversed poem into poem2.txt


def append():
    """
    Appends my name and a message to the end of poem2.txt.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem2.txt")  # set PATH to poem2.txt
    print(PATH)  # show which file is being opened

    # open poem2.txt in append mode (adds text to the end)
    with open(PATH, "a") as f:
        f.write("\n")  # blank line before extra text
        f.write("Name: Baila Kestenbaum\n")  # add name
        f.write("I like this poem because it's funny and sweet 😊")  # add message


def main():
    """
    Runs all program functions in order:
    1. Read poem normally
    2. Read poem backwards
    3. Write reversed poem to poem2.txt
    4. Append name and message
    """
    read()            # print poem normally
    read_backwards()  # print poem in reverse
    write()           # write reversed poem to poem2.txt
    append()          # add name/message to poem2.txt



if __name__ == "__main__":
    main()
