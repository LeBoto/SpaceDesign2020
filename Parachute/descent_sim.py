import numpy as np


class DescentSim(object):
    def __init__(self, y_init, mass, area, c_d_down, c_d_side):
        self.pos = y_init
        self.mass = mass
        self.area = area
        self.cd_s = c_d_side
        self.cd_