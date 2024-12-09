r'''
NI-RFSG (Python module: nirfsg)
pip install nirfsg
https://pypi.org/project/nirfsg/
'''

__update__ = '2024.12.09'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from nirfsg import PXIe_5654
from dataclasses import dataclass
from enum import Enum


''' MAIN CLASS
-------------------------------------------------------- '''

@dataclass
class UNIT:
    baseUnit: str
    factor: int

class UNITS(Enum):
    uHz = UNIT("Hz", 1e-6)
    mHz = UNIT("Hz", 1e-3)
    Hz = UNIT("Hz", 1)
    kHz = UNIT("Hz", 1e3)
    MHz = UNIT("Hz", 1e6)
    GHz = UNIT("Hz", 1e9)

class INSTRUMENT:
    '''
    '''
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'OUTPUT'
    ]

    def __init__(self, resource: str = ""):
        '''
        '''
        self.sig_gen = PXIe_5654(resource)
        # self.sig_gen.initiate()
    
    def CLOSE(self) -> None:
        self.sig_gen.close()

    def DEVICE_INFO(self) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.sig_gen.instrument_manufacturer
        MODEL = self.sig_gen.instrument_model
        SERIAL_NUMBER = self.sig_gen.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn
    
    def OUTPUT(self, *args) -> None:
        '''
        Set Output State ON / OFF
        arg0: bool = ON / OFF
        '''
        state = args[0]
        if state == True or state == 1 or state == "1" or state == "ON":
            self.sig_gen.initiate()
        else:
            self.sig_gen.abort()
    
    def FREQUENCY(self, *args):
        '''
        Set FRECUENCY value
        arg0: float = Frequency
        arg1: str = Unit
        '''
        value = float(args[0])
        unit = None
        if len(args) > 1 and args[1] in [e.name for e in UNITS]:
            unit = str(args[1])
            factor = UNITS[unit].value.factor
            value = value * factor
        self.sig_gen.rf_frequency = value # Hz
    
    def LEVEL(self, *args):
        '''
        Set POWER LEVEL value
        arg0: float = Level
        arg1: str = Unit
        
        INCOMPLETE:
        - Only dBm
        '''
        value = float(args[0])
        self.sig_gen.rf_power = value # dBm
