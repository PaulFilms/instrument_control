r'''
Especial functions for the device:
    - TYPE: CALIBRATOR
    - MANUFACTURER: FLUKE
    - MODEL: 5xxx

TASK:
WARNINGS:
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT(VISA):
    '''
    '''
    NMB_FUNCTIONS = [
        'MEAS',
        'OPER',
        'STBY',
        'OUT_VPP'
    ]

    def __init__(self, resource=str, timeout: int = 10):
        super().__init__(resource, timeout)
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        MODEL = IDN.split(chr(44))[1]
        self.MODEL = None
        if MODEL[0:2] == "57":
            self.MODEL = "5700"
        if MODEL[0:2] == "55":
            self.MODEL = "5500"
    
    def OPER(self, *args) -> None:
        '''
        '''
        self.WR("*CLS")
        # self.WR("ESE 1")
        # self.WR("SRE 32")
        self.WR("OPER")
        self.OPC()

    def STBY(self, *args) -> None:
        '''
        '''
        self.WR("*CLS")
        # self.WR("ESE 1")
        # self.WR("SRE 32")
        self.WR("OUT 0 HZ")
        self.WR("OUT 0 V")
        self.WR("STBY")
        self.OPC()

    def OUT_VPP(self, *args):
        '''
        arg1: float = Value
        arg2: str = Unit
        '''
        VPP: float = (float(args[0])*2**0.5)*2
        self.WR("*CLS")
        self.WR(f"OUT {VPP}{args[1]}")
        self.OPC()


    def FOUR_WIRES(self, *args) -> None:
        pass