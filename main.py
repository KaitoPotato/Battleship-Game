import actions as a
import objects as obj

global p1_grid
global p2_grid

GRID_SIZE = 5

player1 = obj.Player("Player 1", GRID_SIZE)
player2 = obj.Player("Player 2", GRID_SIZE)



def main():

    turn = 0       # Turn 0 is for preparation, and turns 1 to (2*GRID_SIZE*GRID_SIZE) are playing turns

    # Prepare for game
    a.print_grid(player1.grid)
    a.input_points(player1)
    a.print_grid(player1.grid)

    a.print_grid(player2.grid)
    a.input_points(player2)
    a.print_grid(player2.grid)

    turn += 1

    # Start game
    while turn != ((2*GRID_SIZE*GRID_SIZE)+1):

        print("---------------------------------------------")
        print("Scoreboard:")
        print("%s: %s points" %(player1.name, player1.points))
        print("%s: %s points" %(player2.name, player2.points))
        print("---------------------------------------------")

        if turn%2 == 1:     # Odd number of turn => Player 1
            print("It is %s's turn. Choose a square from %s's grid:" %(player1.name,player2.name))
            a.print_grid(player2.hidden_grid)
            a.take_turn(player1, player2)

        else:               # Even number of turn => Player 2
            print("It is %s's turn. Choose a square from %s's grid:" %(player2.name,player1.name))
            a.print_grid(player1.hidden_grid)
            a.take_turn(player2, player1)

        turn += 1

    # End game
    if player1.points > player2.points:
        print("%s wins!" %(player1.name))
    elif player1.points < player2.points:
        print("%s wins!" %(player2.name))
    else:
        print("Draw!")


if __name__ == "__main__":
    main()