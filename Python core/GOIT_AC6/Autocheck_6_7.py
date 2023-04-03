def sanitize_file(source, output):
    with open (source, "r") as file1:
        source = file1.read()
        cleared = ""
        for i in source:
            if i.isdigit():
                continue
            else:
                cleared += i
    with open (output, "w") as file2:
       file2.write(cleared)