import main

global x_coordinate
global y_coordinate
global num_100s
global num_200s
global num_500s
global num_1000s
global bomb
global rob
global shield
global double
global mirror


num_200s = 5
num_500s = 2
num_1000s = 1

# If p1 hits these squares in p2
num_bombs = 1           # Bomb: reset points for p1
num_robs = 1            # Rob: p1 robs p2 points (and p2 resets)
num_shields = 1         # Shield: p1 keeps a shield that can use afterwards
num_doubles = 1         # Double: double p1 points
num_mirrors = 1         # Mirror: p1 keeps a mirror that can use afterwards


def print_grid(grid):
    for i in range(main.GRID_SIZE):
        print(grid[i])


def input_points(player):
    grid = player.grid
    print("%s:" %(player.name))

    input_point(grid, num_200s, "200")
    input_point(grid, num_500s, "500")
    input_point(grid, num_1000s, "1000")
    input_point(grid, num_bombs, "B")
    input_point(grid, num_robs, "R")
    input_point(grid, num_shields, "S")
    input_point(grid, num_doubles, "D")
    input_point(grid, num_mirrors, "M")
    assign_remaining_points(grid)


def input_point(grid, amount:int, value:str):
    for _ in range(amount):
        print("You are now inputting your %s" %(value))
        # Get appropiate target coords
        target_coords = assign_points(grid, value)

        # Assign value to target coords
        grid[target_coords[0]][target_coords[1]] = value
        print_grid(grid)

def assign_remaining_points(grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            grid[i][j] = "100" if (value == "-") else value

def assign_points(grid, points):
    x_coordinate = int(input("Enter x coordinate for your %s - " %(points)))
    y_coordinate = int(input("Enter y coordinate for your %s - " %(points)))

    if space_taken_input(grid, x_coordinate, y_coordinate):
        return assign_points(grid, points)
    else:
        return (x_coordinate, y_coordinate)

def space_taken_input(grid, x, y):
    if x > (main.GRID_SIZE-1) or y > (main.GRID_SIZE-1):
        print("Error - this space is out of bounds")
        return True

    if grid[x][y] != "-":
        print("Error - this space is taken choose another square")
        return True



def take_turn(playerAttacking, targetPlayer):
    print("It is %s's turn to attack!" %(playerAttacking.name))

    target_grid = targetPlayer.grid
    target_hidden_grid = targetPlayer.hidden_grid
    target_square = attack_square(target_grid)

    square_value = target_grid[target_square[0]][target_square[1]]

    #Evaluate square value
    evaluate_square_value(square_value, playerAttacking, targetPlayer)

    # Set square to "X"
    target_grid[target_square[0]][target_square[1]] = "X"
    target_hidden_grid[target_square[0]][target_square[1]] = "X"


def evaluate_square_value(value, playerAttacker, targetPlayer):
    if value == "100": 
        playerAttacker.points += 100
        print("%s has gained 100 points!" %playerAttacker.name)

    elif value == "200": 
        playerAttacker.points += 200
        print("%s has gained 200 points!" %playerAttacker.name)

    elif value == "500": 
        playerAttacker.points += 500
        print("%s has gained 500 points!" %playerAttacker.name)

    elif value == "1000": 
        playerAttacker.points += 1000
        print("%s has gained 1000 points!" %playerAttacker.name)

    elif value == "M": 
        playerAttacker.mirror = True
        print("%s has now a mirror!" %playerAttacker.name)

    elif value == "S": 
        playerAttacker.shield = True
        print("%s has now a shield!" %playerAttacker.name)

    elif value == "D": 
        playerAttacker.points *= 2
        print("%s's points have been duplicated!" %playerAttacker.name)

    elif value == "B": 

        print("%s has hit a bomb!" %playerAttacker.name)

        # If player1 has shield and uses it
        if playerAttacker.shield == True and use_wildcard(playerAttacker, "shield"):
            playerAttacker.shield = False
            return
        
        # If player1 has mirror and uses it
        if playerAttacker.mirror == True and use_wildcard(playerAttacker, "mirror"):
            targetPlayer.points = 0  
            playerAttacker.mirror = False
            return

        # If player1 doesn't have shield/mirror or if it is not used
        playerAttacker.points = 0
        print("%s's points have exploded!" %playerAttacker.name)

    elif value == "R":

        print("%s has hit a rob wildcard!" %playerAttacker.name)

        # If player2 has shield and uses it
        if targetPlayer.shield == True and use_wildcard(targetPlayer, "shield"):
            targetPlayer.shield = False
            return
        
        # If player2 has mirror and uses it
        if targetPlayer.mirror == True and use_wildcard(targetPlayer, "mirror"):
            targetPlayer.points += playerAttacker.points
            playerAttacker.points = 0  
            targetPlayer.mirror = False
            return

        # If player2 doesn't have shield/mirror or if it is not used
        playerAttacker.points += targetPlayer.points
        targetPlayer.points = 0
        print("%s's points have been robbed by %s!" %(targetPlayer.name, playerAttacker.name))

    else:
        print("Error: unexpected value for square")


def use_wildcard(player, wildcardName):
    answer = input("%s do you want to use the %s? (y/n) " %(player.name, wildcardName))
    if answer == "y":
        print("%s has used %s!"%(player.name, wildcardName))
        return True
    elif answer == "n":
        return False
    else:
        print("Error: unexpected input")
        return use_wildcard(player, wildcardName)


def attack_square(grid):
    x = int(input("Enter x coordinate you want to target: "))
    y = int(input("Enter y coordinate you want to target: "))

    if check_attack_space(grid, x, y):
        return attack_square(grid)
    else:
        return (x, y)

def check_attack_space(grid, x, y):
    if x > (main.GRID_SIZE-1) or y > (main.GRID_SIZE-1):
        print("Error - this space is out of bounds")
        return True

    if grid[x][y] == "X":
        print("Error - this space has already been attacked choose another square")
        return True