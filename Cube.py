from copy import deepcopy

class Pyraminx:
    def __init__(self, colours=["r", "y", "g", "b"], state=None):
        #### fornt is RED bottom is Blue
        ## sequacne is red -> yellow -> green -> blue
        self.cube = [
            ["r" for i in range(9)],
            ["y" for i in range(9)],
            ["g" for i in range(9)],
            ["b" for i in range(9)],
        ]

        self.rotateNumber = 0
        
        if len(state) != 36:
            raise Exception("The length of state is incorrect")
        else:
            face, piece = 0, 0
            # r,g,b,y,y,g
            for s in state:
                self.cube[face][piece] = s
                piece += 1
                if piece % 9 == 0:
                    piece = 0
                    face += 1
                if face % 4 == 0:
                    face = 0
            if self.cube[0][7] != 'r' and self.cube[1][5] != 'r' and self.cube[3][7] != 'r':
                self.cube = self.rotate().cube
                self.cube = self.rotate().cube
                self.rotateNumber = 2
            elif self.cube[0][5] != 'r' and self.cube[2][7] != 'r' and self.cube[3][5] != 'r':
                self.cube = self.rotate().cube
                self.rotateNumber = 1
                
    def stringify(self):
        return "".join([piece for face in self.cube for piece in face])

    def solved(self):
        return self.cube == [
            ["r" for i in range(9)],
            ["y" for i in range(9)],
            ["g" for i in range(9)],
            ["b" for i in range(9)],
        ]

    def show(self):
        print(
            " " * 2
            + f"{self.cube[2][0]}"
            + " " * 6
            + f"{self.cube[0][0]}"
            + " " * 6
            + f"{self.cube[1][0]}"
        )
        print(
            " " * 1
            + "".join([self.cube[2][i] for i in range(1, 4)])
            + " " * 4
            + "".join([self.cube[0][i] for i in range(1, 4)])
            + " " * 4
            + "".join([self.cube[1][i] for i in range(1, 4)])
        )
        print(
            " " * 0
            + "".join([self.cube[2][i] for i in range(4, 9)])
            + " " * 2
            + "".join([self.cube[0][i] for i in range(4, 9)])
            + " " * 2
            + "".join([self.cube[1][i] for i in range(4, 9)])
        )
        print(" ")
        print(" " * 7 + "".join([self.cube[3][i] for i in range(4, 9)]))
        print(" " * 8 + "".join([self.cube[3][i] for i in range(1, 4)]))
        print(" " * 9 + "".join([self.cube[3][i] for i in range(0, 1)]))

    #### Move functions
    @staticmethod
    def rotateRight(x,y,z):
        temp = z
        z = x
        x = y
        y = temp
        return x,y,z
    
    @staticmethod
    def rotateLeft(x,y,z):
        temp = z
        z = y
        y = x
        x = temp
        return x,y,z
    
    def up(self,direction):## direction 0:counter clockwise , 1:clockwise
        newState = deepcopy(self)
        if not direction: # turn counter clockwise
            for i in range(4):
                newState.cube[0][i],\
                newState.cube[1][i],\
                newState.cube[2][i] = self.rotateLeft(newState.cube[0][i],\
                                                        newState.cube[1][i],\
                                                        newState.cube[2][i])
        else:
            for i in range(4):# turn clockwise
                newState.cube[0][i],\
                newState.cube[1][i],\
                newState.cube[2][i] = self.rotateRight(newState.cube[0][i],\
                                                        newState.cube[1][i],\
                                                        newState.cube[2][i])
        return newState
    
    def right(self,direction):
        newState = deepcopy(self)
        if not direction:# turn counter clockwise
            newState.cube[0][3],\
            newState.cube[3][6],\
            newState.cube[1][6] = self.rotateLeft(newState.cube[0][3],\
                                              newState.cube[3][6],\
                                              newState.cube[1][6])
            newState.cube[0][7],\
            newState.cube[3][7],\
            newState.cube[1][5] = self.rotateLeft(newState.cube[0][7],\
                                              newState.cube[3][7],\
                                              newState.cube[1][5])
            newState.cube[0][6],\
            newState.cube[3][3],\
            newState.cube[1][1] = self.rotateLeft(newState.cube[0][6],\
                                              newState.cube[3][3],\
                                              newState.cube[1][1])
            newState.cube[0][8],\
            newState.cube[3][8],\
            newState.cube[1][4] = self.rotateLeft(newState.cube[0][8],\
                                              newState.cube[3][8],\
                                              newState.cube[1][4])
        else:# turn clockwise
            newState.cube[0][3],\
            newState.cube[3][6],\
            newState.cube[1][6] = self.rotateRight(newState.cube[0][3],\
                                            newState.cube[3][6],\
                                            newState.cube[1][6])
            newState.cube[0][7],\
            newState.cube[3][7],\
            newState.cube[1][5] = self.rotateRight(newState.cube[0][7],\
                                            newState.cube[3][7],\
                                            newState.cube[1][5])
            newState.cube[0][6],\
            newState.cube[3][3],\
            newState.cube[1][1] = self.rotateRight(newState.cube[0][6],\
                                            newState.cube[3][3],\
                                            newState.cube[1][1])
            newState.cube[0][8],\
            newState.cube[3][8],\
            newState.cube[1][4] = self.rotateRight(newState.cube[0][8],\
                                            newState.cube[3][8],\
                                            newState.cube[1][4])
        return newState
    
    def left(self,direction):
        newState = deepcopy(self)
        if not direction:# turn counter clockwise
            newState.cube[0][1],\
            newState.cube[2][6],\
            newState.cube[3][6] = self.rotateLeft(newState.cube[0][1],\
                                              newState.cube[2][6],\
                                              newState.cube[3][6])
            newState.cube[0][5],\
            newState.cube[2][7],\
            newState.cube[3][5] = self.rotateLeft(newState.cube[0][5],\
                                              newState.cube[2][7],\
                                              newState.cube[3][5])
            newState.cube[0][6],\
            newState.cube[2][3],\
            newState.cube[3][1] = self.rotateLeft(newState.cube[0][6],\
                                              newState.cube[2][3],\
                                              newState.cube[3][1])
            newState.cube[0][4],\
            newState.cube[2][8],\
            newState.cube[3][4] = self.rotateLeft(newState.cube[0][4],\
                                              newState.cube[2][8],\
                                              newState.cube[3][4])
        else:# turn clockwise
            newState.cube[0][1],\
            newState.cube[2][6],\
            newState.cube[3][6] = self.rotateRight(newState.cube[0][1],\
                                              newState.cube[2][6],\
                                              newState.cube[3][6])
            newState.cube[0][5],\
            newState.cube[2][7],\
            newState.cube[3][5] = self.rotateRight(newState.cube[0][5],\
                                              newState.cube[2][7],\
                                              newState.cube[3][5])
            newState.cube[0][6],\
            newState.cube[2][3],\
            newState.cube[3][1] = self.rotateRight(newState.cube[0][6],\
                                              newState.cube[2][3],\
                                              newState.cube[3][1])
            newState.cube[0][4],\
            newState.cube[2][8],\
            newState.cube[3][4] = self.rotateRight(newState.cube[0][4],\
                                              newState.cube[2][8],\
                                              newState.cube[3][4])
        return newState
   
    def back(self,direction):
        newState = deepcopy(self)
        if not direction:# turn counter clockwise
            newState.cube[1][3],\
            newState.cube[3][3],\
            newState.cube[2][6] = self.rotateLeft(newState.cube[1][3],\
                                              newState.cube[3][3],\
                                              newState.cube[2][6])
            newState.cube[1][7],\
            newState.cube[3][2],\
            newState.cube[2][5] = self.rotateLeft(newState.cube[1][7],\
                                              newState.cube[3][2],\
                                              newState.cube[2][5])
            newState.cube[1][6],\
            newState.cube[3][1],\
            newState.cube[2][1] = self.rotateLeft(newState.cube[1][6],\
                                              newState.cube[3][1],\
                                              newState.cube[2][1])
            newState.cube[1][8],\
            newState.cube[3][0],\
            newState.cube[2][4] = self.rotateLeft(newState.cube[1][8],\
                                              newState.cube[3][0],\
                                              newState.cube[2][4])
        else:# turn clockwise
            newState.cube[1][3],\
            newState.cube[3][3],\
            newState.cube[2][6] = self.rotateRight(newState.cube[1][3],\
                                              newState.cube[3][3],\
                                              newState.cube[2][6])
            newState.cube[1][7],\
            newState.cube[3][2],\
            newState.cube[2][5] = self.rotateRight(newState.cube[1][7],\
                                              newState.cube[3][2],\
                                              newState.cube[2][5])
            newState.cube[1][6],\
            newState.cube[3][1],\
            newState.cube[2][1] = self.rotateRight(newState.cube[1][6],\
                                              newState.cube[3][1],\
                                              newState.cube[2][1])
            newState.cube[1][8],\
            newState.cube[3][0],\
            newState.cube[2][4] = self.rotateRight(newState.cube[1][8],\
                                              newState.cube[3][0],\
                                              newState.cube[2][4])
        return newState
    
    def rotate(self):
        # 3 Upper faces rotate
        newState = deepcopy(self)
        frontFace = newState.cube.pop(0)
        
        newState.cube.insert(2,frontFace)

        # Bottom Face rotate
        newState.cube[3][8] = self.cube[3][0]
        newState.cube[3][3] = self.cube[3][1]
        newState.cube[3][7] = self.cube[3][2]
        newState.cube[3][6] = self.cube[3][3]
        newState.cube[3][0] = self.cube[3][4]
        newState.cube[3][2] = self.cube[3][5]
        newState.cube[3][1] = self.cube[3][6]
        newState.cube[3][5] = self.cube[3][7]
        newState.cube[3][4] = self.cube[3][8]

        return newState
        

