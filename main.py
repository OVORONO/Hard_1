import os

print("введите слово")
a = input()

with open('synonyms2.txt','r+') as f:

    for i in iter(f):
        if a in i:
            print(i)

f = open('synonyms2.txt','r+')
if a in f.read():
    print(f.readline())
else:
    print ("слова в списке нет")
    exit()

sin = 0
lol = input("Нравится синоним?:  ")
if lol == 'нет':
    sin = sin + 1
elif lol == 'да':
    sin = sin - 1

if sin > 0:
    print("сейчас добавим")
    slovo = input()
    f.seek(0, os.SEEK_END)
    f.write("\n" + a + " - " + slovo)
    f.write = slovo
elif sin < 0:
    print("круто")
else:
    print("введите да или нет")

