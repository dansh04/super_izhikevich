# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:50:27 2021

@author: dansh
"""

import izhikevich_cells as izh


class ibCell(izh):
    def __init__(self, stimVal):
        super.__init(self, stimVal)