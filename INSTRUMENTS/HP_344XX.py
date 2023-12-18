'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 344XX

\n
`TASK:`
    - MEASURES Enum Class
    - CONFIG FUNCTIONS

\n
`WARNINGS:`
    - @
'''

__update__ = '2023.12.05'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum
from typing import List

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

class MEASURES(Enum):
    VOLTAGE_DC = "VOLT:DC"
    VOLTAGE_AC = "VOLT:AC"
    CURRENT_DC = "CURR:DC"
    CURRENT_AC = "CURR:AC"
    RESISTANCE_2W = ""
    RESISTANCE_4W = ""
    FREQUENCY = "FREQ"

NMB_FUNCTIONS: List[str] = [
    'DEVICE_INFO',
    'CONFIG',
    'MEAS'
]

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str, timeout: int = 10):
        super().__init__(resource, timeout)
    
    def CONFIG(self, *args) -> None:
        '''
        arg1: int = RANGE VALUE
        arg2: float = UNIT
        '''
        ## ARG1 (RANGE VALUE)
        range_value: float
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1
        ## ARG2 (UNIT)
        unit: str
        if len(args) > 1 and args[1] and args[1] != "": 
            unit = ""
        else: 
            unit = ""
        ## 
        self.WR('*CLS')
        # INCOMPLETE
    
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