r'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 344XX

TASK:
    - INCOMPLETE
WARNINGS:
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' MAIN LIBRARIES '''
from VISA import INSTRUMENT as VISA


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT(VISA):
    '''
    '''
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'MEAS'
    ]

    def __init__(self, resource: str, timeout: int = 10):
        super().__init__(resource, timeout)
    
    def CONFIG(self, *args) -> None:
        '''
        '''
        self.WR('*CLS')
    
    def MEAS(self, *args) -> float:
        '''
        '''
        self.WR('*CLS')
        self.WR('TRIG:SOUR BUS')
        self.WR('INIT')
        self.WR('*TRG')
        self.OPC()
        self.WR('FETC?')
        meas = self.READ()
        meas = float(meas)
        return meas