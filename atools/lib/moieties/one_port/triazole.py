import mbuild as mb
import numpy as np


class Triazole(mb.Compound):
    """ A triazole group. """
    def __init__(self):
        super(Triazole, self).__init__()

        mb.load('triazole.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)

        self.add(mb.Port(anchor=self[0], orientation=[0, -1, 0], separation=0.07),
            'down')

if __name__ == '__main__':
    triazole = Triazole()
    triazole.save('triazole-test.mol2', overwrite=True)
