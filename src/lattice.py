import turtle

class Lattice:
    def __init__(self, cells, nbr):
        #Cells is amount of cells in lattice
        #nbr is amount of neighbors for the lattice
        self.cells = cells
        self.nbr = nbr

    def draw(self):
        if self.nbr == 4:
            print("Test failed")
        


    

    #def SAW:
    #    self_avoiding_walk()

n = 9
TwoD = Lattice(n, 4)

TwoD.draw()