import os
from pick import pick
from tabulate import tabulate
from pyfiglet import figlet_format
import copy
import platform

# determining type of the system in order to change clear command between OSs

operatingSystem = platform.uname().system                
if operatingSystem == 'Windows':
    clearVariable = 'cls'
elif operatingSystem == 'Linux':
    clearVariable = 'clear'


os.system(clearVariable)

print(figlet_format('C  E   T \n'))
print(figlet_format('Civil Engineering Tools \n', font='digital'))

#zone IDs
zoneIDs = [str(x) for x in input('Enter zone IDs with a space.\n').split()]
for i in range(len(zoneIDs)):
    zoneIDs[i] = zoneIDs[i].upper()
a = len(zoneIDs)

print('\n')

#population numbers Np
populationNumber = [int(y) for y in input('Enter population numbers seperating with a space. (Np)\n').split()]
b = len(populationNumber)

print('\n')

#Floor Area Af
floorArea = [int(z) for z in input('Enter floor areas with a space. (Af) \n').split()]
c = len(floorArea)

print('\n')

#Employment number Ne
employmentNumber = [int(t) for t in input('Enter employment number with a space. (Ne)\n').split()]
d = len(employmentNumber)

print('\n')

if a == b == c == d:

    ########################################################################################################################
    ################################################ CALCULATIONS ##########################################################
    ############################################ PHASE 1 CALCULATIONS ######################################################
    ########################################################################################################################
    
    #production number Pi
    productionNumber = [(3*x)-500 for x in populationNumber]
    
    #attraction number Ai
    attractionNumber1 = [(3*x)+400 for x in employmentNumber]
    attractionNumber2 = [(75*x) for x in floorArea]
    attractionNumber = [sum(i) for i in zip(attractionNumber1, attractionNumber2)]
    
    ########################################################################################################################
    ############################################ PHASE 2 CALCULATIONS ######################################################
    ########################################################################################################################

    # getting minutes input from user
    counter = 0
    minutesList=[]
    while counter<len(zoneIDs):
        pointName = zoneIDs[counter]
        
        minutes = [int(o) for o in input(f'\nPlease enter the minutes needed to go from point {pointName} to others with a single space.\nKeep in mind that the order of the numbers are important, enter the numbers as same order as the Zone IDs.\n').split()]
        
        
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
    
    
    # calculating Fij
    Fij = copy.deepcopy(minutesList)                # copying minutes from original list to Fij list in order to keep minutesList as it is.    
    for i in range(len(Fij)):
        for j in range(len(Fij[i])):
            if isinstance(Fij[i][j], int or float):          # checking if the selected element has a type of int
                Fij[i][j] **= -2

   
   # this code calculates Fij * Pi
   
    
    myFijList = copy.deepcopy(Fij)       # copying Fij list in order to make calculations without changing any Fij value
    
    def multiplyLists(list1, list2):
        result = []
        
        for i in range(len(list1)):
            row=[]
            for j in range(len(list1[i])):
                if isinstance(list1[i][j], (int, float)):
                # if matrix[i][j] is int or float:
                    element = list1[i][j] * list2[j]
                    roundedElement = round(element, 3)            
                    row.append(roundedElement)                                     # adding the result to our result list
                    #print('if worked')
                    
                else:
                    row.append(list1[i][j])                                # this code runs if code finds any '-' while doing calculation
                    #print('else worked')
            result.append(row)
    
        return result
    
    result = multiplyLists(myFijList, productionNumber)
    
    
    # calculating sigma(Pi*Fij)
    
    # defining function to calculate sum
    def sum_lists(lists):
        sums = []
        for l in lists:
            sum = 0
            for elem in l:
                if isinstance(elem, (int, float)):  # Check if the element is a number
                    sum += elem
                    roundedSum = round(sum, 3)
            sums.append(roundedSum)
        return sums

    # using the function
    sumListRaw = copy.deepcopy(result)
    sumList = sum_lists(sumListRaw)
    

    # calculating Pi*Fij / sigma(Pi*Fij)
    myResult = []

    for i in range(len(result)):
        row = []
        for j in range(len(result[i])):
            if result[i][j] == '-':
                row.append('-')
            else:
                division = result[i][j] / sumList[i]
                roundedDivision = round(division, 2)
                row.append(roundedDivision)
        myResult.append(row)
 
    
    # calculating the sum of the division above
    divideAndSum = sum_lists(myResult)
    
    # rounding all the numbers in order to check our calculations are correct or not
    roundedDivideAndSum = [int(number) for number in divideAndSum]

    if all(number == 1 for number in roundedDivideAndSum):
        os.system(clearVariable)
        print("calculations are correct \n")
    else:
        os.system(clearVariable)
        print("calculations are not correct \n ")
    
    
    # calculating Ai * ((Pi * Fij) / sigma(Pi * Fij))
    aPF = multiplyLists(myResult, attractionNumber)
    
    # calculating the sum of the list above
    aPFSumList = sum_lists(aPF)
    
    title = 'Would you like to save tables as .txt file?'
    options = ['Yes', 'No']

    option, index = pick(options, title, indicator='=>', default_index=0)
    if option == 'Yes':
        tablo = open('phase_2 - tables.txt', 'w')
        
    
        # printing results                       
        for i in range(len(minutesList)):
            
            # creating a new list only for creating table
            tableMinutesList = minutesList[i]
            tableFijList = Fij[i] 
            tablePiFijList = result[i]                 
            tableDivideList = myResult[i]
            tableAPFList = aPF[i]
            
            output = tabulate({'Zone #': zoneIDs, 'Np': populationNumber, 'Af': floorArea, 'Ne': employmentNumber, 'Pi (3*Np - 500)': productionNumber, 'Ai (3*Ne + 75*Af + 400)': attractionNumber, 'C [minutes]': tableMinutesList, 'Fij (C^-2)': tableFijList, 'Pi * Fij': tablePiFijList, 'Pi * Fij / sigma(Pi * Fij)': tableDivideList, 'Ai * ((Pi * Fij) / sigma(Pi * Fij))': tableAPFList}, headers='keys', numalign='center', stralign='center', tablefmt='outline')   
            
            tablo.write(f'{output} \n \n')
            tablo.close
                
            print(f'Tables for Phase 2 are saved in the file "phase_2 - tables.txt" ')
    else:
        # printing results                       
        for i in range(len(minutesList)):
            
            # creating a new list only for creating table
            tableMinutesList = minutesList[i]
            tableFijList = Fij[i] 
            tablePiFijList = result[i]                 
            tableDivideList = myResult[i]
            tableAPFList = aPF[i]
            
            output = tabulate({'Zone #': zoneIDs, 'Np': populationNumber, 'Af': floorArea, 'Ne': employmentNumber, 'Pi (3*Np - 500)': productionNumber, 'Ai (3*Ne + 75*Af + 400)': attractionNumber, 'C [minutes]': tableMinutesList, 'Fij (C^-2)': tableFijList, 'Pi * Fij': tablePiFijList, 'Pi * Fij / sigma(Pi * Fij)': tableDivideList, 'Ai * ((Pi * Fij) / sigma(Pi * Fij))': tableAPFList}, headers='keys', numalign='center', stralign='center', tablefmt='outline')   
                
            print(f'For zone {zoneIDs[i]} \n')
            print(output)
            print('\n')
            print(f'Sum for Pi*Fij at point {zoneIDs[i]}: {sumList[i]}')
            print(f'Sum for Ai * ((Pi * Fij) / sigma(Pi * Fij)): {aPFSumList[i]}')
            print('\n'*2)

    
    
        


