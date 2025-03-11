with open("start.txt", 'r') as file:
    contents = file.readlines()

with open("end.html", 'w') as file:
    for row in contents:
        indent_level = 1
        while row[:2] == "  ":
            indent_level += 1
            row = row[2:]
        file.write(f"<h{indent_level}>{row.strip()}</h{indent_level}>\n")
