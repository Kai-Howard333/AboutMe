letterTrue = False
def play():
    userList = []       #this is an empty list

    userList.append(input("Put an Adjective here please: "))                                # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Adjective here please: "))                                # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Adjective here please: "))                               # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Animal here please (plural form): "))                    # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Noun here please (plural form): "))                       # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Part of the body here please: "))                         # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Adjective here please: "))                               # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Creepy Crawly here please: "))                           # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Color here please: "))                                   # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Adjective here please: "))                             # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Noun here please: "))                                    # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a School Subject here please: ").title())                  # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put a Vehicle here please: "))                                 # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put the name of someone in the room here please: ").title())   # user gets to put a word of their choice into the MadLib userList
    userList.append(input("Put an Action Verb here please: "))                             # user gets to put a word of their choice into the MadLib userList



    for i in userList:                          #This tells if what the user types is not letters only then make them retype it
        if i.isalpha():                     #   else print Madlibs
            global letterTrue
            letterTrue = True
        elif i.isalpha() == False:
            letterTrue = False
            print("Use words Dumy")
            break
    if letterTrue == True:                      #prints the Madlibs with the users inputs
        print('''
        My school is pretty {} for most of the year, except in late October. {} Cobwebs appear in the hallway, with really {} {} 
        hanging from them. The lunch-room has orange and black {} everywhere, and they serve roasted {} for lunch. Someone told me 
        that a giant {} {} took over the principal’s office. All of the teachers look different; one is a zombie with {} hair, 
        another is a {} {}, and I think my {} teacher is a {} now. Tombstones line the hallways, and one said, 
        ”Here lies {}, who died of {}”.'''.format(userList[0],userList[1],userList[2],userList[3],userList[4],userList[5],userList[6],
        userList[7],userList[8],userList[9],userList[10],userList[11],userList[12],userList[13],userList[14]))
play()

plAgn = input("Do you want to make another one (y or n): ").lower()         #Once the Madlibs is printed it will give the user an option to redo it 
while(plAgn == "y" or "yes"):
    play()
    plAgn = input("Do you want to make another one (y or n): ").lower()

print("\n   Thanks for playing... Go away now")