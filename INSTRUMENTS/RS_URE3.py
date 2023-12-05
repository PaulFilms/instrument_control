'''
`Especial functions for the device:`
    - TYPE: RMS VOLTIMETER
    - MANUFACTURER: ROHDE & SCHWARZ
    - MODEL: URE3

\n
`TASK:`
\n
`WARNINGS:`
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
    NMB_FUNCTIONS = [
        'MEAS_VRMS'
        ]

    def __init__(self, resource: str = "", timeout: int = 10):
        super().__init__(resource, timeout)
        self.WR("*CLS")
    
    def MEAS_VRMS(self, *args):
        '''
        arg1: int = FREQUENCY VALUE
        '''
        ## ARG1 (FREQUENCY VALUE)
        freq_value: float
        if len(args) > 0 and args[0] and args[0] != "": 
            freq_value = float(args[0])
        else: 
            freq_value = 0
        
        ## 
        meas: float = 0.0
        return meas
