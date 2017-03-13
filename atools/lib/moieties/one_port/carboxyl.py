import mbuild as mb
import numpy as np


class Carboxyl(mb.Compound):
    """ A carboxyl group. """
    def __init__(self):
        super(Carboxyl, self).__init__()

        mb.load('carboxyl.pdb', compound=self, relative_to_module=self.__module__)
        #mb.spin_x(self, 90.0 * (np.pi / 180.0))
        mb.translate(self, -self[0].pos)

        self.add(mb.Port(anchor=self[0]), 'down')
        mb.translate(self['down'], [0, -0.07, 0])

if __name__ == '__main__':
    carboxyl = Carboxyl()
    carboxyl.save('carboxyl-test.mol2', overwrite=True)
