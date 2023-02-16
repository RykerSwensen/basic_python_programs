print('Welcome to Pirates Curse! This game is very difficult, you may die many times before choosing the correct route to beat the game. Just like Dark Souls.')
print('Please do not forget to check your inputs to make sure they match the correct options or you may die!')
print()

first_name = input('Hello, what is your first name!? ')
print()
print(f'Hello {first_name}! Welcome to Pirates Curse!')
print()

print(f'{first_name} and their buisness partner Juan discuss there plans on gathering a crew to hunt for a rumored treasure in Africa.')
print('The risk is high, the travels are far and the chance of the treasure being there is slim.')
print('Jauns alternative option is to seek for an abandoned crypto currency mining site. There would be tons of graphics cards we could sell at a markup.')
print()

quest_line = input(f'{first_name}, do you choose: AFRICA, CRYPTO, or REFUSE? ')

if quest_line.lower() == ('refuse'):
    print(f'Congratulations {first_name}, you won the game! You avoided the pirates curse by not participating!')
elif quest_line.lower() == ('africa'):
    print('Africa it is, we will head out first thing in the morning...')
    print()
    print('The next morning you meet juan at your shared run down boat.')
    print('You bring your friend Taylor, and Juan brings a dozen of his henchmen.')
    print(f'Everyone looks unsure of the journey, but you {first_name} have already decided everyones fate.')
    print('Everyone boards the sketchy boat.')
    print()
    print('The wind looks good to set sail for now, but in a few hours it will pick up and you could get lost in sea?')
    print()
    africa_first_decision = input(f'{first_name}, do you want to: WAIT or GO ')
    if africa_first_decision.lower() == ('wait'):
        print('The henchmen sigh in relif, they were starting to look seasick, although we havent left the dock.')
        print()
        print('You waited to long, one of the henchmen got drunk and killed you mistaking you for an alien. Try again.')
    elif africa_first_decision.lower() == ('go'):
        print('You set off to sail the waters!')
        print()
        print('After a few hours the wind starts to show.')
        africa_water_first_decision = input(f'{first_name}, do you want to: ROTATE THE SAIL AROUND THE MAST or POWER THROUGH THE WIND? ')
        if africa_water_first_decision.lower() == ('rotate the sail around the mast'):
            print('You safely get through the wind')
            print()
            print('After weeks of slow and safely traveling, you and Jaun make it to Africa. However, Taylor and the henchmen were not so lucky. They died.')
            print('As you and Juan dock what is left of your ship on the border of where the treasure is rumored to be...')
            print('You see Nathan Drake running from gun fire holding a golden treasure.')
            print()
            africa_water_second_decison = input(f'{first_name}, do you want to: CHASE NATHAN DRAKE or RETURN HOME? ')
            if africa_water_second_decison.lower() == ('chase nathan drake'):
                print('The chase begins!')
                print()
                africa_water_third_decision = input('Nathan starts climbing to get to the rooftops of this small african town. do you: CLIMB or CHASE FROM BELOW? ')
                if africa_water_third_decision.lower() == ('climb'):
                    print()
                    print('You grab onto a water line and start to climb. Nathan glaces down, and sees you underneath him.')
                    print('He kicks you in the face, and you fall to the ground.')
                    print()
                    print('Juan runs over to you, in anger he kills you for letting the treasure get away. Try again.')
                    print()
                elif africa_water_third_decision.lower() == ('chase from below'):
                    print('You chase him from below')
                    print('Although he has a speed advantage, you manage to keep him in your sight.')
                    print('Until...')
                    print()
                    print('Juan accidently trips behind you, making you fall over too. In anger for losing Nathan Drake, you attempt to fight Juan. You die. Try again.')
            elif africa_water_second_decison.lower() == ('return home'):
                print('You and Jaun board what remains of your ship.')
                print('You and Juan were never to be seen again. Try again.')
            else:
                print('After all you have been through, you think Juan is going to put up with you not picking one of the two options? He kills you, try again.')
        elif africa_water_first_decision.lower() == ('power through the wind'):
            print(f'{first_name}, and company were no match for the wind. Everyone died. Try again.')
        else:
            print('No, that was neither of the two options. The crew killed you for your mistake. Try again.')
    else:
        print('The henchmen kill you for not choosing one of the two options, try again.')
elif quest_line.lower() == ('crypto'):
    print('Ahh finally someone with some sense, we shall set out plans first thing in the morning.')
    print()
    print('The next morning Juan meets you at your apartment.')
    print('He begins to tell you about two potential cytpto mines.')
    print('There is an old abondoned crypto mine here in Rexburg, but I dont think they were using high end GPUs to mine.')
    print('There is an old abondoned crypto mine in Jackson Hole that was using NVIDIA 3090s, it would be like hitting a goldmine.')
    print()
    crypto_location = input(f'{first_name}, do you want to go to: REXBURG or JACKSON HOLE? ')
    if crypto_location.lower() == ('rexburg'):
        print('Alright, lets get in Juans car and head over to the crypto mine.')
        print()
        print('A few minutes later you arive at the old abondoned crypto mine.')
        print()
        crypto_door = input(f'Who opens the door: JUAN or {first_name}? ')
        if crypto_door.lower() == ('juan'):
            print('Juan is tired of your weakness. He kills you for making him open the door. Try again.')
        elif crypto_door.lower() == (f'{first_name.lower()}'):
            print('You open the door')
            print('As soon as your eyes adjust to the dark abondoned crypto mine you feel a cold steel barrell against your chest.')
            print('You see a typical unfriendly Rexburg local as your life flashes before your eyes.')
            print('The Rexburg local says no trespassing right before killing you. Try again.')
            print()
        else:
            print(f'{first_name}, you are starting to annoy me. I am making you restart. Please choose one of the given options.')
    elif crypto_location.lower() == ('jackson hole'):
        print('Alright, but youre driving... I hate driving over the pass')
        print()
        print()
        print('As you arrive to the pass, a semi loses control and runs into your car. You die. Try again.')
    else:
        print('Juan loses patience with you and kills you for not choosing one of the given options. Try again.')
else:
    print('Juan looks at you with dissapointment. It appears you have wasted his time by not choosing one of the three given options. Juan kills you for wasting his time. Try again.')