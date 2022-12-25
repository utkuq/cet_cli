import os
from pick import pick
from tabulate import tabulate
from pyfiglet import figlet_format
import copy

os.system('cls')

print(figlet_format('C  E   T \n'))
print(figlet_format('Civil Engineering Tool \n', font='digital'))

#zone IDs
zoneIDs = [str(x) for x in input('Enter zone IDs with a space.\n').split()]
for i in range(len(zoneIDs)):
    zoneIDs[i] = zoneIDs[i].upper()
a = len(zoneIDs)

os.system("cls")

#population numbers Np
populationNumber = [int(y) for y in input('Enter population numbers seperating with a space. (Np)\n').split()]
b = len(populationNumber)

os.system("cls")

#Floor Area Af
floorArea = [int(z) for z in input('Enter floor areas with a space. (Af) \n').split()]
c = len(floorArea)

os.system("cls")

#Employment number Ne
employmentNumber = [int(t) for t in input('Enter employment number with a space. (Ne)\n').split()]
d = len(employmentNumber)

os.system('cls')

if a == b == c == d:
    os.system("cls")
    print('GIVEN VALUES')
    print('-'*50 +'\n')
    print(f'Entered zone IDs: \n {zoneIDs} \n ')
    print(f'Entered population numbers (Np): \n {populationNumber} \n')
    print(f'Entered floor areas (Af): \n {floorArea} \n')
    print(f'Entered employment numbers (Ne): \n {employmentNumber} \n')
    print('\n'+ '-'*50 + '\n')
    
    ################################################ CALCULATIONS ##########################################################
    ############################################ PHASE 1 CALCULATIONS ######################################################
    
    #production number Pi
    productionNumber = [(3*x)-500 for x in populationNumber]
    
    #attraction number Ai
    attractionNumber1 = [(3*x)+400 for x in employmentNumber]
    attractionNumber2 = [(75*x) for x in floorArea]
    attractionNumber = [sum(i) for i in zip(attractionNumber1, attractionNumber2)]
    
    ############################################ PHASE 2 CALCULATIONS ######################################################
    print('\n')
    counter = 0
    minutesList=[]

    while counter<len(zoneIDs):
        pointName = zoneIDs[counter]
        os.system('cls')
        minutes = [int(o) for o in input(f'Please enter the minutes needed to go from point {pointName} to others with a single space. \nKeep in mind that the order of the numbers are important, enter the numbers as same order as the Zone IDs. \n').split()]
        os.system('cls')
        if len(minutes) == len(zoneIDs)-1:
            minutesList.append(minutes)
            #print(minutesList)
            counter+=1
        else:
            print('Please enter the right amount of numbers!')
            minutes=[]
            counter = 0
    for i in range(len(minutesList)):
        minutesList[i].insert(i,'-')
    
    Fij = copy.deepcopy(minutesList)                # copying minutes from original list to Fij list in order to keep minutesList as it is.  
    for i in range(len(Fij)):
        for j in range(len(Fij[i])):
            if isinstance(Fij[i][j], int):          # checking if the selected element has a type of int
                Fij[i][j] **= -2                    # calculating Fij values
                           
    for i in range(len(minutesList)):
        tableMinutesList = minutesList[i]           # creating a new list only for creating table
        tableFijList = Fij[i]                       # creating a new list only for creating table
        print(f'For zone {zoneIDs[i]} \n')
        print(tabulate({'Zone #': zoneIDs, 'Np': populationNumber, 'Af': floorArea, 'Ne': employmentNumber, 'Pi (3*Np - 500)': productionNumber, 'Ai (3*Ne + 75*Af + 400)': attractionNumber, 'C [minutes]': tableMinutesList, 'Fij (C^-2)': tableFijList}, headers='keys'))
        print('\n'*2)