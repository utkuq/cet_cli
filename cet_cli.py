import os
from pick import pick
from tabulate import tabulate
os.system("cls")

title = 'Select your language: / Dilinizi seçiniz: '
options = ['English', 'Türkçe']

option, index = pick(options, title, indicator='=>', default_index=0)

#english
if(option=='English'):
    ################################################ INPUT ##########################################################
    while True:
        #zone IDs
        zoneIDs = [str(x) for x in input('Enter zone IDs with a space.\n').split()]
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
        
        counter = 0
        minutesList=[]
        
        
        while counter<len(zoneIDs):
            pointName = zoneIDs[counter]
            minutes = [int(o) for o in input(f'Please enter the minutes needed to go from point {pointName} to others with a single space. \n Keep in mind that the order of the numbers are important, enter the numbers as same order as the Zone IDs. \n').split()]
            if len(minutes) == len(zoneIDs)-1:
                #minutes.insert(0,pointName)
                #minutesList.append(minutes)
                #counter+=1
                ######
                lst ={zoneIDs[counter]:minutes}
                minutesList.append(lst)
                print(minutesList)
                counter+=1
            else:
                print('Please enter the right amount of numbers!')
                minutes=[]
                counter = 0
                
            
            
        
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
            print(minutesList)
            print('\n')
            ################################################## RESULTS #############################################################
            print('CALCULATED VALUES')
            print(f'Your production numbers (Pi): \n {productionNumber} \n')
            print(f'Your attraction numbers (Ai): \n {attractionNumber} \n')
            print('\n \n')
            
            #PHASE 1 DIAGRAM!!!
            print(tabulate({'Zone #': zoneIDs, 'Np': populationNumber, 'Af': floorArea, 'Ne': employmentNumber, 'Pi': productionNumber, 'Ai': attractionNumber}, headers='keys'))
            
            
            break
            
        else:
            print('Number of each values are not equal, try again?')
            tryAgainTitle = 'Number of each values are not equal, try again?'
            tryAgain = ['Yes', 'No']
            myOption, index = pick(tryAgain, tryAgainTitle, indicator='=>', default_index=0)
            if myOption == 'No':
                break
            
    
    
    
    
    
    



#türkçe
else:
    zoneIDs = [str(x) for x in input('Bölge isimlerini aralarında boşluk bırakarak giriniz.\n').split()]
    
    os.system("cls")
    
    populationNumber = [int(y) for y in input('Popülasyon sayısını aralarında boşluk bırakarak giriniz.\n').split()]
    
    os.system("cls")
    
    print(zoneIDs)
    print(populationNumber)