# with open("file.txt", "r") as file:
#     contents = file.read()
#     print(contents)
#
# with open("file.txt", "a") as file:
#     file.write("\nyo-yo-yo")


with open("input/names.txt", "r") as names:
    for line in names.readlines():
        name, place = line.strip().split(", ")
        with open(f"output/{name}.txt", mode="w") as mail:
            with open("input/letter.txt", "r") as letter:
                txt = letter.read()
                txt = txt.replace("[name]", f"{name}").replace("[city]", f"{place}")
                mail.write(txt)
