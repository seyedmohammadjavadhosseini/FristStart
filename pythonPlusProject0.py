import pyautogui as pa
import random 
typeGameList=['p1 vs p2','p1 vs pc1','pc1 vs pc2']
pc1NameList=['jorge','martin','carlos','anna']
pc2NameList=['robot','iran','korosh','messi']
objectList=['Rock','sc','paper']
a=0
b=0
c=0
d=0
i=0
j=0
gameTypeChoice=pa.prompt(f'enter your choice from {typeGameList}')
if gameTypeChoice=='p1 vs p2':
    pa.alert(text=f'welcome to {gameTypeChoice}',title='message',button='hi')
    p1=pa.prompt('enter your name p1:')
    p2=pa.prompt('enter your name p2:')
    gameNumber=int(pa.prompt('enter number of game:'))
    while i<=gameNumber:
        choiceP1=pa.prompt(f'enter your choice {p1} from {objectList}')
        choiceP2=pa.prompt(f'enter your choice {p2} from {objectList}')
        for item in objectList:
            if choiceP1 or choiceP2 != item:
                break
        pa.write('input is incorrect')
        if choiceP1==choiceP2:
            a+=1
            b+=1
            pa.write(f'number of game is {i}')
            i+=1
            pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
            pa.write(f'game is drow , {p1} score is {a} , {p2} score is {b}')
            if i==gameNumber:
                pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                if a>b:
                    pa.write(f'{p1} is the winner')
                elif a<b:
                    pa.write(f'{p2} is the winner')
                else:
                    pa.write('game is drow')
                pa.write('---------------------------------------------------------------------------------------------')
            elif choiceP1=='Rock':
                if choiceP2=='sc':
                    a+=2
                    pa.write(f'number of game is {i}')    
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p1} is the winner , {p1} score is {a}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                            pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow') 
                    pa.write('---------------------------------------------------------------------------------------------')
                
                elif choiceP2=='paper':   
                    b+=2   
                    pa.write(f'number of bame is {i}')  
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p2} is the winner , {p2} score is {b}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                             pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow')
                    pa.write('---------------------------------------------------------------------------------------------') 
            elif choiceP1=='paper':
                if choiceP2=='Rock':
                    a+=2
                    pa.write(f'number of game is {i}')    
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p1} is the winner , {p1} score is {a}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                             pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow')
                    pa.write('---------------------------------------------------------------------------------------------')
                elif choiceP2=='sc':
                    b+=2
                    pa.write(f'number of game is {i}')
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p2} is the winner , {p2} score is {b}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                             pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow')
                    pa.write('---------------------------------------------------------------------------------------------')
            elif choiceP1=='sc':
                if choiceP2=='paper':
                    a+=2
                    pa.write(f'number of game is {i}')
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p1} is the winner , {p1} score is {a}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                            pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow')
                    pa.write('---------------------------------------------------------------------------------------------')
                elif choiceP2=='Rock':
                    b+=2
                    pa.write(f'number of game is {i}')
                    i+=1
                    pa.write(f'{p1} choice is {choiceP1},{p2} choice is {choiceP2}')
                    pa.write(f'{p2} is the winner , {p2} score is {b}')
                    if i==gameNumber:
                        pa.write(f'the final score {p1} is {a}, the final score {p2} is {b}')
                        if a>b:
                            pa.write(f'{p1} is the winner')
                        elif a<b:
                            pa.write(f'{p2} is the winner')
                        else:
                            pa.write('game is drow')
                    pa.write('---------------------------------------------------------------------------------------------')
            else: 
            
            
                
                            












            
















                       

                
                

            
                