print("You wake up in a dark room. There is a door and a window.")
choice1 = input("Do you go to the 'door' or 'window'? ").lower()

if choice1 == "door":
    print("The door is locked. You hear something behind it... creepy.")
elif choice1 == "window":
    print("You open the window and escape! You win! 🎉")
else:
    print("You just stand there doing nothing... game over. 💀")
