
#Just the bare necessities for the Menu
#User inputs their name and chooses what game they would like to play


BLACKJACK_CHOICE = 1
TETRIS_CHOICE = 2
PONG_CHOICE = 3
#GAME_CHOICE = 4
QUIT_CHOICE = 5


def main():
    print("Welcome! What is your name?")
    name = input("Name: ")
    print("Hello,", name,"! Please choose a game you would like to play.")
    choice = 0
    while choice != QUIT_CHOICE:
        showMenu()
        choice = int(input("Enter selection: "))
        if choice == BLACKJACK_CHOICE:
            playBlackJack()
            
        elif choice == TETRIS_CHOICE:
            playTetris()
            
        elif choice == PONG_CHOICE:
            playPong()
        #elif choice == GAME_CHOICE:
    
    
  

def showMenu():

    print(" MENU          " )
    print("1.) BlackJack  " )
    print("2.) Tetris     " )
    print("3.) PONG       " )
    print("4.) Game 4     " )
    print("5.)  Quit      " )


main()
