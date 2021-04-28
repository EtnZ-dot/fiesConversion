# Customizable Text-Based GUI by EtnZ
# Version 0.0 (Private Access)

import textwrap

border = ["+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+", "| ", " |"]
width = len(border[0]) - len(border[1]) - len(border[2])
confirms = [("[1] Yes" + " " * int(width / 4) + "[2] No"), ("[1] Yes" + " " * width + "[2] No")]
inputPrompt = "> "
inputInvalid = "Invalid input, please try again!"


def width_check():
    global width
    width = len(border[0]) - len(border[1]) - len(border[2])


def window(string, num=0, align="left"):
    width_check()
    stringList = textwrap.wrap(string, width)
    if num != 1 and num != 2:
        print(border[0])
    if align.lower() == "left":
        for i in range(len(stringList)):
            spacing = width - len(stringList[i])
            print(border[1] + stringList[i] + " " * spacing + border[2])
    if align.lower() == "center":
        for i in range(len(stringList)):
            print(border[1] + stringList[i].center(int(width)) + border[2])
    if align.lower() == "right":
        for i in range(len(stringList)):
            spacing = width - len(stringList[i])
            print(border[1] + " " * spacing + stringList[i] + border[2])
    if num != 2:
        print(border[0])


def choice(num):
    while True:
        userInput = input(inputPrompt)
        try:
            userInput = int(userInput)
        except:
            userInput = 0
        if num >= userInput > 0:
            return userInput
        else:
            print(inputInvalid)


def is_it_a_number():
    while True:
        userInput = input(inputPrompt)
        is_num = True
        try:
            userInput = float(userInput)
        except:
            is_num = False
        if is_num:
            return userInput
        else:
            print(inputInvalid)


def confirm(string, num=0):
    window(string, 0, "center")
    window(confirms[num], 1, "center")
    if choice(2) == 1:
        return True
    else:
        return False
