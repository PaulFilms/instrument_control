'''
Especial functions for the device:
    - TYPE: MULTIMETER
    - MANUFACTURER: HP / AGILENT / KEYSIGHT
    - MODEL: 3458A

TASK:
    ...

WARNINGS:
    - INCOMPLETE

'''

__version__ = '2024.03.01'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from typing import List
from enum import Enum

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

NMB_FUNCTIONS: List[str] = [
    'DEVICE_INFO',
    'CONFIG',
    'MEAS'
]

class MEASURES(Enum):
    VOLTAGE_DC = "DCV"
    VOLTAGE_AC = "ACV"
    CURRENT_DC = "DCI"
    CURRENT_AC = "ACI"
    RESISTANCE_2W = "OHM"
    RESISTANCE_4W = ""
    FREQUENCY = ""

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str, timeout: int = 5):
        super().__init__(resource, timeout=timeout, termination=True)
        # self.DEVICE.read_termination = '\n'
        # self.DEVICE.write_termination = '\n'

    def CONFIG(self, **kwargs) -> None:
        '''
        INCOMPLETE
        
        kwargs:
            - measure
        
        -------

        instrumentVM.WriteString("PRESET", True)
        instrumentVM.WriteString("OFORMAT ASCII", True)
        instrumentVM.WriteString("BEEP", True)
        instrumentVM.WriteString("DCV AUTO", True)
        instrumentVM.WriteString("TARM AUTO", True)
        instrumentVM.WriteString("TRIG AUTO", True)
        instrumentVM.WriteString("DCV 30,100", True)
        instrumentVM.WriteString("NRDGS 1,SYN", True)
        instrumentVM.WriteString("MEM OFF", True)
        instrumentVM.WriteString("END ALWAYS", True)
        instrumentVM.WriteString("NDIG 6", True)
        instrumentVM.WriteString("TERM SCANNER", True)
        instrumentVM.WriteString("CHAN 0", True)
        '''
        if 'measure' in kwargs:
            if type(kwargs['measure']) == MEASURES:
                self.WR(f'{kwargs['measure'].value} AUTO')
            else:
                self.WR(f'{kwargs['measure']} AUTO')
        self.WR('NPLC 5,AUTO')
        self.WR('NDIG 8')
        pass

    def MEAS(self):
        '''
        '''
        # self.WR(f'NPLC 10')
        self.WR('TARM SGL')
        # self.OPC()
        meas = self.DEVICE.query('A$')
        # meas = float(meas)
        return meas