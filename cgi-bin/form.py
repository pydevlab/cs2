#!/usr/bin/env python3
import cgi
import re

def check_message(text):
    return bool(re.search('[0-9a-zа-я]', text))

form = cgi.FieldStorage()
message = form.getfirst("str_to_encode", "не задано")
key = form.getfirst("keydigit", "не задано")

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = message.lower()
check = check_message(message)
if check:
    pass
else:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Лаборатория шифрования PyDevLab</title>
            </head>
            <body>""")
    print("""<h3><p>Ошибка! Вы ввели неизвестные символы. Вернитесь <a href="../index.html">назад</a> и введите сообщение заново.</p></h3>""")
    print("""</body></html>""")
    exit()

key = int(key)

encrypted = ''
for letter in message:
    if letter in alphabet:
        t = alphabet.find(letter)
        new_key = (t + key) % len(alphabet)
        encrypted += alphabet[new_key]
    else:
        encrypted += letter

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Лаборатория шифрования PyDevLab</title>
        </head>
        <body>""")

print('<h3><p>Зашифрованное сообщение: </p></h3>', encrypted)

print("""</body></html>""")
