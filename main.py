import email
import random
import string
import time
import os
output = []
randomLeghnt = 5




def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def prefixgen(exportAmount, Email):
    for i in range(exportAmount):
        ranID = get_random_string(5)
        Emailcore = Email.replace("@gmail.com", "")
        final = "{}+{}@gmail.com".format(Emailcore, ranID)
        output.append(final)
    print(output)
    input("Press Enter to continue...")
    mainmenu()

def exportprefix(exportdir):
    try:
        Directory = r'{}\Output.txt'.format(exportdir)
        print("file location: " + Directory)
        with open(Directory, 'w') as fp:
            for item in output:
                fp.write("%s\n" % item)
            
            print('\033[32m' + "suffix are exported in selected directory" + '\033[0m')
            input("Press Enter to continue...")
            mainmenu()
    except:
        print('\033[31m' + "Directory not found or no generated suffix found" + '\033[0m')
        input("Press Enter to continue...")
        mainmenu()




def mainmenu():
    os.system('cls')
    print('\033[35m' + """  

    





""" + '\033[0m')
    print('\033[35m' + """ 

    E-MAIL BOT by: marcell_marcell
    [1] generate suffix
    [2] export suffix
    [3] close program                                                                                                  

""" + '\033[0m')
    answer = input()
    if answer == "1" :
        email
        genAmount = int(input("How many suffix do you want to generate?         "))
        emailinput = input("give the gmail acc u wanna use                        ")
        prefixgen(genAmount, emailinput)
        

    elif answer == "2":
        exportpath = input("Where do you want to save the file? ")
        exportprefix(exportpath)


    elif answer == "3":
        print("")
    else:
        print('\033[31m' + "This is not a valid answer" + '\033[0m')

mainmenu()