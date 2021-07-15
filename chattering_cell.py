# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:30:58 2021

@author: dansh
"""

import izhikevich_cells as izh



class CCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = 'Chattering_Cell'
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
        
def createCell():
    myCell = CCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=='__main__':
    createCell()
