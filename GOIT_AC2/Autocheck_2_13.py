message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if (ord(ch) > 64 and ord(ch) <91) or (ord(ch) > 96 and ord(ch) < 123):
        ch1 = 'A' if ord(ch) > 64 and ord(ch) <91 else 'a'  
        pos = ord(ch) - ord (ch1)
        pos = (pos + offset) % 26
        new_ch = chr(pos + ord(ch1))
        encoded_message += new_ch
    else:
        encoded_message += ch