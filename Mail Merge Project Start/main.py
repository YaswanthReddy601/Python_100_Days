#TODO: Create a letter using starting_letter.txt
place = "[name]"

with open("./input/Names/invited_names.txt") as invite:
    names = invite.readlines()

with open("./input/Letters/starting_letter.txt") as letter:
    let = letter.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = let.replace(place, stripped_name)
        with open (f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as final:
            final.write(new_letter)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp