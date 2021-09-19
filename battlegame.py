wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

orc = "Orc"
orc_hp = 100
orc_damage = 100

dragon_hp = 300
dragon_damage = 50

user_choice = 0
character = ""
while True:
# First Loop
    while user_choice > 3 or user_choice < 1:
        print("Wizard")
        print("Elf")
        print("Human")
        print("Orc")
    
        user_choice = int(input("Choose your character: "))
        if user_choice == 4:
            print("Your character is: Orc\nHealth:" + str(orc_hp) + "\nDamage: " + str(orc_damage))
            character = "Orc"
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif user_choice == 3:
            print("Your character is: Wizard\nHealth:" + str(human_hp) + "\nDamage: " + str(human_damage))
            character = "Human"
            my_hp = human_hp
            my_damage = human_damage
            break
        elif user_choice == 2:
            print("Your character is: Elf\nHealth: " + str(elf_hp) + "\nDamage: " + str(elf_damage))
            character = "Elf"
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif user_choice == 1:
            print("Your character is: Wizard\nHealth: " + str(wizard_hp) + "\nDamage: " + str(wizard_damage))
            character = "Wizard"
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        else:
            print("Unknown character")
            continue

    print("Your character is", character)
    print("Your Health is", my_hp)
    print("Your Damage is", my_damage)
    print("")

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The ", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        print("")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break
    
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at", character)
        print("The", character + "'s hitpoints are now:", my_hp)
        print("")
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            break
    play_again = input("Would you like to play again? ")
    if play_again == 1 or play_again == "yes":
        pass
    else:
        break
