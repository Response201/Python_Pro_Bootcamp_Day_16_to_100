
"""

Vid manuell öppning av en fil måste man också komma ihåg att stänga den,
annars kan programmet använda mer minne än nödvändigt.

file = open("my_file.txt")
content = file.read()
print(content)
file.close()




Ett bättre och säkrare sätt att läsa filer är att använda "with".
Då stängs filen automatiskt när blocket är klart

with open("my_file.txt") as file:
    content = file.read()




Skriva om innehåll i en fil. Lägg till mode="w" för write, default är read.

with open("my_file.txt", mode="w") as file:
    content = file.write("World Hello")




Lägga till innehåll i en fil. Lägg till mode="a" för add.

with open("my_file.txt", mode="a") as file:
    content = file.write("\nHello World")
    print(content)




Om man öppnar en fil i skrivläge ("w") som inte finns,
kommer systemet att skapa filen automatiskt.
Detta fungerar endast i skrivläge (mode="w").

with open("new_file.txt", mode="w") as file:
    content = file.write("\nHello World")
    print(content)

"""