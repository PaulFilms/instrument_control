'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 344XX


TASK:
    - ...


WARNINGS:
    - ...
'''

__update__ = '2024.12.09'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum
from typing import List

''' MAIN LIBRARIES '''
from instrument_ctrl.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

class MEASURES(Enum):
    VOLTAGE_DC = "VOLT:DC"
    VOLTAGE_AC = "VOLT:AC"
    CURRENT_DC = "CURR:DC"
    CURRENT_AC = "CURR:AC"
    RESISTANCE_2W = "RES"
    RESISTANCE_4W = "FRES"
    FREQUENCY = "FREQ"

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str, timeout: int = 10):
        super().__init__(resource, timeout)

        # 
        self.NMB_FUNCTIONS: List[str] = [
            'DEVICE_INFO',
            'CONFIG',
            'MEAS'
        ]
    
    def DEVICE_INFO(self, *args) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        IDN = self.RD("*IDN?; *WAI")
        return IDN
    
    def CONFIG(self, *args) -> None:
        '''
        arg0: str = UNIT
        
        `UNITS:`
            - VOLTAGE_DC
            - VOLTAGE_AC
            - CURRENT_DC
            - CURRENT_AC
            - RESISTANCE_2W
            - RESISTANCE_4W
            - FREQUENCY
        '''
        ## ARG0 (UNIT)
        unit = args[0]
        try:
            unit = MEASURES[unit].value
        except:
            unit = MEASURES.VOLTAGE_DC.value
        ## 
        self.WR('*CLS')
        self.WR(f'CONF:{unit}')
        self.OPC()
    
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