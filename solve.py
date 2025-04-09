import json
from Cube import Pyraminx

json_object = None
with open('Combinations.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

def solveIt(state):
    cube = Pyraminx(state=state)
    
    print("Solving Moves : ",end = " ")
    
    if cube.rotateNumber == 1:
        print("rotate",end=" ")
    elif cube.rotateNumber == 2:
        print("rotate`",end=" ")

    if cube.cube[0][0] == cube.cube[2][2]:
        print('u',end=" ")
        temp = cube.cube[0][0]
        cube.cube[0][0] = cube.cube[1][0]
        cube.cube[1][0] = cube.cube[2][0]
        cube.cube[2][0] = temp

    elif cube.cube[0][0] == cube.cube[1][2]:
        print('u`',end=" ")
        temp = cube.cube[0][0]
        cube.cube[0][0] = cube.cube[2][0]
        cube.cube[2][0] = cube.cube[1][0]
        cube.cube[1][0] = temp


    if cube.cube[0][8] == cube.cube[1][5]:
        print('r',end=" ")
        temp = cube.cube[0][8]
        cube.cube[0][8] = cube.cube[3][8]
        cube.cube[3][8] = cube.cube[1][4]
        cube.cube[1][4] = temp

    elif cube.cube[0][8] == cube.cube[3][7]:
        print('r`',end=" ")
        temp = cube.cube[0][8]
        cube.cube[0][8] = cube.cube[1][4]
        cube.cube[1][4] = cube.cube[3][8] 
        cube.cube[3][8] = temp
        

    if cube.cube[0][4] == cube.cube[3][5]:
        print('l',end=" ")
        temp = cube.cube[0][4]
        cube.cube[0][4] = cube.cube[2][8]
        cube.cube[2][8] = cube.cube[3][4]
        cube.cube[3][4] = temp

    elif cube.cube[0][4] == cube.cube[2][7]:
        print('l`',end=" ")
        temp = cube.cube[0][4]
        cube.cube[0][4] = cube.cube[3][4]
        cube.cube[3][4] = cube.cube[2][8]
        cube.cube[2][8] = temp
        

    if cube.cube[3][0] == cube.cube[1][7]:
        print('b',end=" ")
        temp = cube.cube[3][0]
        cube.cube[3][0] = cube.cube[2][4]
        cube.cube[2][4] = cube.cube[1][8]
        cube.cube[1][8] = temp

    elif cube.cube[3][0] == cube.cube[2][5]:
        print('b`',end=" ")
        temp = cube.cube[3][0]
        cube.cube[3][0] = cube.cube[1][8]
        cube.cube[1][8] = cube.cube[2][4]
        cube.cube[2][4] = temp

    while not cube.solved():
        move = json_object[cube.stringify()]
        if move[-1] == '`':
            move = move[0]
        else:
            move+='`'
               
        if move[0] == 'U':
            cube = cube.up(0 if move[-1] == '`' else 1)
        elif move[0] == 'R':
            cube = cube.right(0 if move[-1] == '`' else 1)
        elif move[0] == 'L':
            cube = cube.left(0 if move[-1] == '`' else 1)
        elif move[0] == 'B':
            cube = cube.back(0 if move[-1] == '`' else 1)
        
        print(move,end=" ")



    if cube.cube[1][4] == "r":
        print('r',end=" ")
    elif cube.cube[3][8] == "r":
        print('r`',end=" ")
    cube.cube[0][8] = "r"
    cube.cube[1][4] = "y"
    cube.cube[3][8] = "b"

    if cube.cube[2][8] == "r":
        print('l',end=" ")
    elif cube.cube[3][4] == "r":
        print('l`',end=" ")
    cube.cube[0][4] = "r"
    cube.cube[1][8] = "g"
    cube.cube[3][4] = "b"

    if cube.cube[2][4] == "b":
        print('b',end=" ")
    elif cube.cube[1][8] == "b":
        print('b`',end=" ")
    cube.cube[1][8] = "r"
    cube.cube[2][4] = "y"
    cube.cube[3][0] = "b"
    print(" ")
