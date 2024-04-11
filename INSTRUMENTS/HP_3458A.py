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
from typing import Tuple, List
from enum import Enum

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

NMB_FUNCTIONS: Tuple[str] = (
    # 'DEVICE_INFO',
    # 'CONFIG',
    # 'MEAS'
)

class MEASURES(Enum):
    VOLTAGE_DC = "DCV"
    VOLTAGE_AC = "ACV"
    CURRENT_DC = "DCI"
    CURRENT_AC = "ACI"
    RESISTANCE_2W = "OHM"
    RESISTANCE_4W = "OHMF"
    FREQUENCY = "FREQ"

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str, timeout: int = 5):
        super().__init__(resource, timeout=timeout, termination=True)
        # self.DEVICE.read_termination = '\n'
        # self.DEVICE.write_termination = '\n'

    def DEVICE_INFO(self, *args) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        self.WR("CLEAR")
        IDN = self.RD("ID?")
        return IDN

    def CONFIG(self, **kwargs) -> None:
        '''
        INCOMPLETE
        
        kwargs:
            - measure
            - NDIG
            - NPLC
        
        -------

        EXAMPLE:
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
        if 'NPLC' in kwargs:
            self.WR(f"NPLC {kwargs['NPLC']}")
        else:
            self.WR('NPLC 10')
        if 'NDIG' in kwargs:
            self.WR(f'NDIG {kwargs['NDIG']}')
        else:
            self.WR('NDIG 6')

    def MEAS(self):
        '''
        '''
        # CLEAR
        self.WR("CLEAR")
        self.RD("ERR?")

        # CONFIG MEASURE
        # self.WR(f'NPLC 10')

        # MEASURE
        meas = self.RD('TARM SGL')
        # meas = float(meas)
        return meas