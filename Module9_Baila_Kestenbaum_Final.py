"""
Pseudocode:
1.  Start the program.
2.  Set the folder and file paths for the original poem and the remixed poem.
3.  Define read():
      Open the original poem.
      Print each line normally so we can see the poem as it is.
4.  Define read_backwards():
      Open the original poem again.
      Put all lines into a list.
      Print the poem from the last line to the first line.
     Return all the reversed lines as one string so we can use it later.
5. Define write():
     Take the reversed poem from read_backwards().
     Write that reversed poem into the remix file.
6. Define replace():
     Open the remix file and read the whole text.
     Replace some words and punctuation to change the style a bit.
     Print the updated poem so we can see the changes.
     Save the edited version back into the remix file.
7. Define append():
     Add a blank line, my name, and a short explanation at the bottom of the remix file.
8. Define main():
     Call each function in the correct order so the whole process runs:
         read(), read_backwards(), write(), replace(), append()
9. Run main().
"""

"""
This program reads a poem from poem_original.txt, prints it normally,
prints it backwards, writes the reversed poem into poem_remix.txt,
and finally appends my name and a short explanation to the file.
"""

import os

DOCS_DIR = "docs"  # folder where all text files (the poem) are stored
PATH_IN = os.path.join(DOCS_DIR, "poem_original.txt")
PATH_OUT = os.path.join(DOCS_DIR, "poem_remix.txt")  # global variable that stores the current file path


def read():
    """
    Reads the poem from poem_original.txt and prints it line by line.
    """
    global PATH_IN
    print(PATH_IN)  # show which file is being opened
    try:
        with open(PATH_IN, "r") as f:
            for lines in f:
                print(lines.strip().replace("\n", ""))
    except FileNotFoundError as e:
        print(f"File not found, {e}.")


def read_backwards():
    """
    Reads the poem from poem_original.txt and returns the reversed text
    (last line to first line). Also prints the reversed lines.
    """
    global PATH_IN
    print(PATH_IN)  # print to show the file being opened

    try:
        with open(PATH_IN, "r") as f:
            lines = f.readlines()  # store lines in a list
    except FileNotFoundError as e:
        print(f"File not found, {e}.")
        return ""

    # print each line in reverse order
    for line in reversed(lines):
        print(line.strip())

    # return the reversed poem as one combined string
    return "".join(reversed(lines))


def write():
    """
    Writes the reversed poem into poem_remix.txt.
    """
    global PATH_OUT
    print(PATH_OUT)  # show where we're writing
    try:
        with open(PATH_OUT, "w") as f:
            f.write(read_backwards())  # write reversed poem into poem_remix.txt
    except FileNotFoundError as e:
        print(f"File not found, {e}.")


def replace():
    """
    Replaces some words and punctuation in poem_remix.txt.
    """
    global PATH_OUT
    print(PATH_OUT)
    try:
        with open(PATH_OUT, "r") as f:
            text = f.read()
    except FileNotFoundError as e:
        print(f"File not found, {e}.")
        return

    # replacements: repeated word, surprising change, punctuation
    replacements = [
        ("the", "THE"),
        ("And", "BUT"),
        (",", ";"),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    # print edited poem
    print("\n- Edited Poem -")
    print(text)

    try:
        with open(PATH_OUT, "w") as f:
            f.write(text)
    except FileNotFoundError as e:
        print(f"File not found, {e}.")


def append():
    """
    Appends my name and a message to the end of poem_remix.txt.
    """
    global PATH_OUT
    print(PATH_OUT)  # show which file is being opened
    try:
        with open(PATH_OUT, "a") as f:
            f.write("\n")  # blank line before extra text
            f.write("---\n")
            f.write("Remixed by: Baila Kestenbaum\n")  # add name
            f.write("I like this poem because it's funny and sweet 😊\n")  # add message
            f.write("I changed the word 'the' to 'THE' and reversed the lines.")
    except FileNotFoundError as e:
        print(f"File not found, {e}.")


def main():
    """
    Runs all program functions in order:
    1. Read poem normally
    2. Read poem backwards
    3. Write reversed poem to poem_remix.txt
    4. Replace words/punctuation
    5. Append name and message
    """
    read()        # print poem normally
    read_backwards()  # print poem in reverse
    write()       # write reversed poem to poem_remix.txt
    replace()     # replace words and punctuation
    append()      # add name/message


if __name__ == "__main__":
    main()
