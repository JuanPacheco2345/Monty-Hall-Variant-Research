import random


# In this program, we are simulating the Monty Hall (without considering the variant). The program
# will take a number of doors(3,6,9,20,100), and it will be simulated for a specific number of
# iterations(100,1000,10000,100000). As we run the program, there is a variable that will keep
# track of the number of wins, for when the contestant switch and does not switch door choices.
# Once completed the number of iterations, we will use the total of wins for when the contestant
# switch and does not switch after the host reveals one of the doors to calculate the probability for
# each case. This will be done by dividing the number of wins by the number of iterations, which
# will then get printed out according to the specific event(switch and no switch)(Licensed).

def Simulate_MontyHall_With_3Doors(trails):
    # Number Of Doors
    numberOfDoors = 3
    # Iterations
    numberOfIterations = int(trails)
    # Contestant switches
    # and contestant doesn't switch
    for assertSwitch in [True, False]:
        # Track wins when Contestant switches and
        # doesn't switch
        recordWins = 0
        # Simulate the Monty Hall game
        # for defined number of iterations
        # and Record wins
        for i in range(numberOfIterations):
            # Simulates the monty hall game show
            if (MontyHallSimulation(assertSwitch, numberOfDoors)):
                # contestant won(increment)
                recordWins += 1
        # Print the probability of winning after
        # completing the number of iterations
        if(assertSwitch == True):

            print("Probability of Winning the Car is ", (recordWins /
                  numberOfIterations) * 100, "if contestant switches")
        if(assertSwitch == False):
            print("Probability of Winning the Car is ", (recordWins / numberOfIterations)
                  * 100, "if contestant stick with orginal selection")


def Simulate_MontyHall_With_6Doors(trails):
    # Number Of Doors
    numberOfDoors = 6
    # Iterations
    numberOfIterations = int(trails)
    # Contestant switches
    # and contestant doesn't switch
    for assertSwitch in [True, False]:
        # Track wins when Contestant switches and
        # doesn't switch
        recordWins = 0
        # Simulate the Monty Hall game
        # for defined number of iterations
        # and Record wins
        for i in range(numberOfIterations):
            # Simulates the monty hall game show
            if (MontyHallSimulation(assertSwitch, numberOfDoors)):
                # contestant won(increment)
                recordWins += 1
        # Print the probability of winning after
        # completing the number of iterations
        if(assertSwitch == True):

            print("Probability of Winning the Car is ", (recordWins /
                  numberOfIterations) * 100, "if contestant switches")
        if(assertSwitch == False):
            print("Probability of Winning the Car is ", (recordWins / numberOfIterations)
                  * 100, "if contestant stick with orginal selection")


def Simulate_MontyHall_With_9Doors(trails):
    # Number Of Doors
    numberOfDoors = 9
    # Iterations
    numberOfIterations = int(trails)

    # Contestant switches
    # and contestant doesn't switch
    for assertSwitch in [True, False]:
        # Track wins when Contestant switches and
        # doesn't switch
        recordWins = 0
        # Simulate the Monty Hall game
        # for defined number of iterations
        # and Record wins
        for i in range(numberOfIterations):
            # Simulates the monty hall game show
            if (MontyHallSimulation(assertSwitch, numberOfDoors)):
                # contestant won(increment)
                recordWins += 1
        # Print the probability of winning after
        # completing the number of iterations
        if(assertSwitch == True):

            print("Probability of Winning the Car is ", (recordWins /
                  numberOfIterations) * 100, "if contestant switches")
        if(assertSwitch == False):
            print("Probability of Winning the Car is ", (recordWins / numberOfIterations)
                  * 100, "if contestant stick with orginal selection")


def Simulate_MontyHall_With_20Doors(trails):
    # Number Of Doors
    numberOfDoors = 20
    # Iterations
    numberOfIterations = int(trails)
    # Contestant switches
    # and contestant doesn't switch
    for assertSwitch in [True, False]:
        # Track wins when Contestant switches and
        # doesn't switch
        recordWins = 0
        # Simulate the Monty Hall game
        # for defined number of iterations
        # and Record wins
        for i in range(numberOfIterations):
            # Simulates the monty hall game show
            if (MontyHallSimulation(assertSwitch, numberOfDoors)):
                # contestant won(increment)
                recordWins += 1
        if(assertSwitch == True):
            # Print the probability of winning after
            # completing the number of iterations
            print("Probability of Winning the Car is ", (recordWins /
                  numberOfIterations) * 100, "if contestant switches")
        if(assertSwitch == False):
            print("Probability of Winning the Car is ", (recordWins / numberOfIterations)
                  * 100, "if contestant stick with orginal selection")


def Simulate_MontyHall_With_100Doors(trails):
    # Number Of Doors
    numberOfDoors = 100
    # Iterations
    numberOfIterations = int(trails)
    # Contestant switches
    # and contestant doesn't switch
    for assertSwitch in [True, False]:
        # Track wins when Contestant switches and
        # doesn't switch
        recordWins = 0
        # Simulate the Monty Hall game
        # for defined number of iterations
        # and Record wins
        for i in range(numberOfIterations):
            # Simulates the monty hall game show
            if (MontyHallSimulation(assertSwitch, numberOfDoors)):
                # contestant won(increment)
                recordWins += 1
        # Print the probability of winning after
        # completing the number of iterations
        if(assertSwitch == True):

            print("Probability of Winning the Car is ", (recordWins /
                  numberOfIterations) * 100, "if contestant switches")
        if(assertSwitch == False):
            print("Probability of Winning the Car is ", (recordWins / numberOfIterations)
                  * 100, "if contestant stick with orginal selection")

# 2 parameter
# First is a boolean paramter wheter contestent switches or not
# Then second parameter is the number of doors in the simulation(Monty Hall)


def MontyHallSimulation(assertSwitch, numberOfDoors):
    # Randomly select a door for the car, out of the number of doors presented
    selectedCarDoor = random.randrange(0, numberOfDoors)
    # First event, contestant selects first choice
    contestant_first_choice = random.randrange(0, numberOfDoors)
    # Host reveals a specific goat door, which is revealed to contestant, second event
    host_reveals_door = ([x for x in range(0, numberOfDoors)
                          if x != contestant_first_choice and x != selectedCarDoor])

    # Reveal all door expect the contestant first chioce and other door
    if contestant_first_choice == selectedCarDoor:
        host_reveals_door = host_reveals_door[:-1]
    # Contestent want to switch door choice after host revealing some of the doors
    if assertSwitch:
        originalSelectionDoor = contestant_first_choice
        while(contestant_first_choice == originalSelectionDoor or contestant_first_choice in host_reveals_door):
            # Contestant now has selected one of the other doors left
            contestant_first_choice = random.randrange(0, numberOfDoors)
    # Return boolean if the contestant door choice was the car door based on if
    # he switch or stayed with orginal selection
    return (contestant_first_choice == selectedCarDoor)


# Run simulations with desired number of iterations
# should print the probabilty of winnning for each policy
# for n number of doors
numberOfTrails = 1000
Simulate_MontyHall_With_3Doors(numberOfTrails)
print()
Simulate_MontyHall_With_6Doors(numberOfTrails)
print()
Simulate_MontyHall_With_9Doors(numberOfTrails)
print()
Simulate_MontyHall_With_20Doors(numberOfTrails)
print()
Simulate_MontyHall_With_100Doors(numberOfTrails)
print()

# Should have displayed all probabilites
print("End of simulation")
