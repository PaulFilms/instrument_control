'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 3458A

TASK:
    ...

WARNINGS:
    ... 

'''

__version__ = '2023.12.18'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from typing import List

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

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

    def MEAS(self, *args) -> float:
        '''
        '''
        pass