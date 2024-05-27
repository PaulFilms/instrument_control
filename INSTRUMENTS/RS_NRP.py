'''
`Especial functions for the device:`
    - TYPE: POWER SENSOR
    - MANUFACTURER: ROHDE & SCHWARZ
    - MODEL: NRP

`TASK:`
    - ...

`WARNINGS:`
    - ...

'''

__update__ = '2023.12.05'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA

''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str, timeout: int = 10, termination: bool = None) -> None:
        super().__init__(resource, timeout, termination)
        self.WR("*CLS")
    
    def ZERO(self):
        self.WR()
        self.OPC()