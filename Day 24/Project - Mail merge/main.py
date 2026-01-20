#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as name_list:

    list_of_names = name_list.readlines()


with open("Input/Letters/starting_letter.txt", "r") as letter:

    letter_template = letter.read()

    # Loopa igenom varje namn och skapa ett personligt brev
    for name in list_of_names:

        name = name.strip("\n")
        new_letter = letter_template.replace("[name]", name)

        # Spara det personliga brevet till en ny fil
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(new_letter)












