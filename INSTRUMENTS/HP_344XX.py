r'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 344XX

TASK:
    - MEASURES Enum Class
    - CONFIG FUNCTIONS
WARNINGS:
'''

__update__ = '2023.10.11'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

class MEASURES(Enum):
    VOLTAGE = "VOLT"
    CURRENT = "CURR"
    RESISTANCE_2W = ""
    RESISTANCE_4W = ""
    FREQUENCY = "FREQ"

class INSTRUMENT(VISA):
    '''
    '''
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'CONFIG',
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