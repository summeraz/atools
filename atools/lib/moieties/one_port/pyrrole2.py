import mbuild as mb
import numpy as np


class Pyrrole2(mb.Compound):
    """ A pyrrole group with a port at the 2 position. """
    def __init__(self):
        super(Pyrrole2, self).__init__()

        mb.load('2pyrrole.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)

        self.add(mb.Port(anchor=self[0], orientation=[0, -1, 0], separation=0.07),
            'down')

if __name__ == '__main__':
    pyrrole2 = Pyrrole2()
    pyrrole2.save('pyrrole2-test.mol2', overwrite=True)
