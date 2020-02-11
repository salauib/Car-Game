#A very simple car game using while loop
#
#Declear variable(s)
command = ""
started = False

#Program starts
while True:
    command = input("Start to control your car please:  ").lower()
    if command == "start":
        #Check if car is alredy started
        if started:
            print("Car is already started, common just drive!")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        #Check if car is alredy stopped
        if not started:
            print("Car is already stopped, just please shut the doors!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command == "quit":
        print("Car game ends")
        break
    else:
        print("Sorry, i don't understand that.")

#End game properly        
input("Press enter key to end car game...")