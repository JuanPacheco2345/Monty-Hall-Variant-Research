# Monty Hall with Variant
import random
# Number of iterations
simulation = 10000


# Monty Hall with variant, the host slips on a banana and accidentally pushes open another door
# in this case we ignore the case where the host slips and open the door with car, which ends the game automatically.
# Therefore we make sure the host choices a together other then the first, so that hosts conintues to open a door accidentally and at random
def MonteCarlo_MontyHall_Varient(hostDoor, contestant_door, numDoors):
    # Make sure that contestent doesn't choice the door that host has opened accidentally
    switchDoor = random.choice([num for num in range(2, numDoors + 1)
                                if num != contestant_door and num != hostDoor])
    return switchDoor


# Simulating the monty hall considering variant, with a specfic number of n door and for a specfic
# number of iterations
def VariantWith3Door(trails):
    # Set number of doors
    doorsToDisplay = [3]
    # Set variables to keep track of win based on event choice
    switchSelectionDoorWin = 0
    orginalSelectionDoorWin = 0
    # Simulate the monty hall with variant for the number of iterations
    # while following the policies
    numDoors1 = 1
    for numDoors in doorsToDisplay:
        for i in range(trails):
            # initialize the doors for host and door with car
            hostDoor = random.randint(1, numDoors1)
            prizeDoor = random.randint(1, numDoors)
            playerDoor = random.randint(1, numDoors)
            # Record number of wins based on switch or no switch
            if playerDoor == prizeDoor:
                orginalSelectionDoorWin += 1
            elif MonteCarlo_MontyHall_Varient(hostDoor, playerDoor, numDoors) == prizeDoor:
                switchSelectionDoorWin += 1
    # Prints the values
    print(f'''For {numDoors} doors\n
    Probability of winning by switching door:  {switchSelectionDoorWin / trails * 100}\n
    Probability of winning with original selection:  {orginalSelectionDoorWin / trails * 100 }\n\n'''
          )


# Simulating the monty hall considering variant, with a specfic number of n door and for a specfic
# number of iterations
def VariantWith6Door(trails):
    # Set number of doors
    doorsToDisplay = [6]
    # Set variables to keep track of win based on event choice
    switchSelectionDoorWin = 0
    orginalSelectionDoorWin = 0
    # Simulate the monty hall with variant for the number of iterations
    # while following the policies
    numDoors1 = 1
    for numDoors in doorsToDisplay:
        for i in range(trails):
            # initialize the doors for host and door with car
            hostDoor = random.randint(1, numDoors1)
            prizeDoor = random.randint(2, numDoors)
            playerDoor = random.randint(2, numDoors)
            # Record number of wins based on switch or no switch
            if playerDoor == prizeDoor:
                orginalSelectionDoorWin += 1
            elif MonteCarlo_MontyHall_Varient(hostDoor, playerDoor, numDoors) == prizeDoor:
                switchSelectionDoorWin += 1
    # Prints the values
    print(f'''For {numDoors} doors\n
    Probability of winning by switching door:  {switchSelectionDoorWin / trails * 100}\n
    Probability of winning with original selection:  {orginalSelectionDoorWin / trails * 100 }\n\n'''
          )

# Simulating the monty hall considering variant, with a specfic number of n door and for a specfic
# number of iterations


def VariantWith9Door(trails):
    # Set number of doors
    doorsToDisplay = [9]
    # Set variables to keep track of win based on event choice
    switchSelectionDoorWin = 0
    orginalSelectionDoorWin = 0
    # Simulate the monty hall with variant for the number of iterations
    # while following the policies
    numDoors1 = 1
    for numDoors in doorsToDisplay:
        for i in range(trails):
            # initialize the doors for host and door with car
            hostDoor = random.randint(1, numDoors1)
            prizeDoor = random.randint(2, numDoors)
            playerDoor = random.randint(2, numDoors)
            # Record number of wins based on switch or no switch
            if playerDoor == prizeDoor:
                orginalSelectionDoorWin += 1
            elif MonteCarlo_MontyHall_Varient(hostDoor, playerDoor, numDoors) == prizeDoor:
                switchSelectionDoorWin += 1
    # Prints the values
    print(f'''For {numDoors} doors\n
    Probability of winning by switching door:  {switchSelectionDoorWin / trails * 100}\n
    Probability of winning with original selection:  {orginalSelectionDoorWin / trails * 100 }\n\n'''
          )


# Simulating the monty hall considering variant, with a specfic number of n door and for a specfic
# number of iterations
def VariantWith20Door(trails):
    # Set number of doors
    doorsToDisplay = [20]
    # Set variables to keep track of win based on event choice
    switchSelectionDoorWin = 0
    orginalSelectionDoorWin = 0
    # Simulate the monty hall with variant for the number of iterations
    # while following the policies
    numDoors1 = 1
    for numDoors in doorsToDisplay:
        for i in range(trails):
            # initialize the doors for host and door with car
            hostDoor = random.randint(1, numDoors1)
            prizeDoor = random.randint(2, numDoors)
            playerDoor = random.randint(2, numDoors)
            # Record number of wins based on switch or no switch
            if playerDoor == prizeDoor:
                orginalSelectionDoorWin += 1
            elif MonteCarlo_MontyHall_Varient(hostDoor, playerDoor, numDoors) == prizeDoor:
                switchSelectionDoorWin += 1
    # Prints the values
    print(f'''For {numDoors} doors\n
    Probability of winning by switching door:  {switchSelectionDoorWin / trails * 100}\n
    Probability of winning with original selection:  {orginalSelectionDoorWin / trails * 100 }\n\n'''
          )

# Simulating the monty hall considering variant, with a specfic number of n door and for a specfic
# number of iterations


def VariantWith100Door(trails):
    # Set number of doors
    doorsToDisplay = [100]
    # Set variables to keep track of win based on event choice
    switchSelectionDoorWin = 0
    orginalSelectionDoorWin = 0
    # Simulate the monty hall with variant for the number of iterations
    # while following the policies
    numDoors1 = 1
    for numDoors in doorsToDisplay:
        for i in range(trails):
            # initialize the doors for host and door with car
            hostDoor = random.randint(1, numDoors1)
            prizeDoor = random.randint(2, numDoors)
            playerDoor = random.randint(2, numDoors)
            # Record number of wins based on switch or no switch
            if playerDoor == prizeDoor:
                orginalSelectionDoorWin += 1
            elif MonteCarlo_MontyHall_Varient(hostDoor, playerDoor, numDoors) == prizeDoor:
                switchSelectionDoorWin += 1
    # Prints the values
    print(f'''For {numDoors} doors\n
    Probability of winning by switching door:  {switchSelectionDoorWin / trails * 100}\n
    Probability of winning with original selection:  {orginalSelectionDoorWin / trails * 100 }\n\n'''
          )


# Print the probabilities after number of iterations
print("Monty Hall with Variant")
VariantWith3Door(simulation)
print()
print("Monty Hall with Variant")
VariantWith6Door(simulation)
print()
print("Monty Hall with Variant")
VariantWith9Door(simulation)
print()
print("Monty Hall with Variant")
VariantWith20Door(simulation)
print()
print("Monty Hall with Variant")
VariantWith100Door(simulation)
print()
