
# File not found
#with open("file.txt") as file:
#        file.read()


# Key error
#a_dictionary = {"key": "value"}
#vaule = a_dictionary["non_exist_key"]


# Index error
#list = [0,1,2]
#item = list[3]

# Type error
# text = "abc"
# print(text + 5)


"""

--- Catching exceptions ---

try: Här skriver man den kod som kan orsaka ett fel.

except: Här fångar man felet och bestämmer vad som ska hända om ett fel uppstår.

else: Denna kod körs om inget fel inträffade i try.

finally: Denna kod körs alltid, oavsett om ett fel uppstod eller inte.

raise: skapa error -> Avbryter programflödet genom att utlösa ett specifikt exception,
antingen ett eget eller ett befintligt, för att tala om att något är fel.





try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    #print(a_dictionary["non_exist_key"])


except FileNotFoundError:
    print("File error")
    file = open("file.txt", mode="w")
    file.write("hej hej")

except KeyError as error_message:
    print("Key error", error_message)

else:
    content = file.read()
    print(content)

finally:
    file.close()
    raise TypeError("error som jag hittat på")




age = -5

if age < 0:
    raise ValueError("Ålder kan inte vara negativ")






"""












