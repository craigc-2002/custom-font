file_text = ""

with open("assets/font-file.txt") as f:
    for line in f:
        file_text += line

dic = eval(file_text)
