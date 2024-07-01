'''
Especial functions for the device:
    - TYPE: CALIBRATOR
    - MANUFACTURER: FLUKE
    - MODEL: 5xxx


TASK:
    - 5080A Functions
    - SCOPE Functions

WARNINGS:
    -
'''

__version__ = '2023.12.20'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum
from typing import List, Tuple

''' MAIN LIBRARIES '''
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN CLASS
-------------------------------------------------------- '''

class SCOPE_MODE(Enum):
    OFF = "OFF"
    VOLT = "VOLT"
    EDGE = "EDGE"
    LEVSINE = "LEVSINE"
    MARKER = "MARKER"

class SCOPE_IMP(Enum):
    Z1M = "Z1M"
    Z50 = "Z50"

class INSTRUMENT(VISA):
    '''
    '''
    def __init__(self, resource: str = "", timeout: int = 10):
        super().__init__(resource, timeout)

        # 
        self.NMB_FUNCTIONS: Tuple[str] = (
            'MEAS',
            'OPER',
            'STBY',
            'OUT_VPP',
            'TWO_WIRES',
            'FOUR_WIRES'
        )

        # 
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        MODEL = IDN.split(chr(44))[1]
        self.MODEL = None
        if MODEL[0:2] == "57":
            self.MODEL = "5700"
        if MODEL[0:2] == "55":
            self.MODEL = "5500"

        # 
        self.NMB_FUNCTIONS = [
            'MEAS',
            'OPER',
            'STBY',
            'OUT_VPP',
            'TWO_WIRES',
            'FOUR_WIRES'
        ]
    
    def DEVICE_INFO(self, *args) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        IDN = self.RD("*IDN?; *WAI")
        return IDN

    def OPER(self, *args) -> None:
        '''
        No args
        '''
        self.WR("*CLS")
        # self.WR("ESE 1")
        # self.WR("SRE 32")
        self.WR("OPER")
        self.OPC()

    def STBY(self, *args) -> None:
        '''
        No args
        '''
        self.WR("*CLS")
        # self.WR("ESE 1")
        # self.WR("SRE 32")
        self.WR("OUT 0 HZ")
        self.WR("OUT 0")
        self.WR("STBY")
        self.OPC()

    def OUT_VPP(self, *args):
        '''
        arg1: float = Value
        '''
        VPP: float = (float(args[0])*2**0.5)*2
        self.WR("*CLS")
        self.WR(f"OUT {VPP}{args[1]}")
        self.OPC()

    def TWO_WIRES(self, *args) -> None:
        '''
        `arg1:` float = Resistance Value

        `5500(s) Parameter: `

            - NONE (Turns off impedance compensation circuitry)
            - WIRE2 (Turns on the 2-wire impedance compensation circuitry)
            - WIRE4 (Turns on the 4-wire impedance compensation circuitry)
        
        `Example: `

            - ZCOMP WIRE2
        
        '''
        ## ARG1 (Resistance Value)
        if len(args) > 0 and args[0]!= None and args[0] != "": 
            value = float(args[0])
        else: 
            value: float = 100000
        
        ## ZCOMP
        if self.MODEL == "5700":
            if value < 100000:
                self.WR(f"RCOMP ON")
            else:
                self.WR(f"RCOMP OFF")
        if self.MODEL == "5500":
            if value > 100000:
                self.WR(f"ZCOMP NONE")
            else:
                self.WR(f"ZCOMP WIRE2")

    def FOUR_WIRES(self, *args) -> None:
        '''
        `arg1:` float = Resistance Value
        '''
        ## ARG1 (Resistance Value)
        if len(args) > 0 and args[0] != None and args[0] != "": 
            value = float(args[0])
        else: 
            value: float = 10000000
        
        ## EXTSENSE
        if self.MODEL == "5700":
            if value > 10000000:
                self.WR(f"EXTSENSE OFF")
            else:
                self.WR(f"EXTSENSE ON")
        if self.MODEL == "5500":
            if value > 100000:
                self.WR(f"ZCOMP NONE")
            else:
                self.WR(f"ZCOMP WIRE4")
        
        # 
        self.WR(f"*WAI")
    
    def SCOPE(self, LEVEL: float = 0, FREQ_PER: float = 0, OUT_IMP: str = SCOPE_IMP.Z1M.value, MODE: str = SCOPE_MODE.VOLT.value):
        '''
        FREQ_PER / Frequency (Hz), Pert
        '''
        self.WR(f"SCOPE {MODE};")
        self.WR(f"OUT {LEVEL} HZ")
        if MODE == SCOPE_MODE.MARKER.value:
            self.WR(f"OUT {FREQ_PER} MS")
        else:
            self.WR(f"OUT {FREQ_PER} HZ")
        self.WR(f"OUT_IMP {OUT_IMP}")
        self.WR("*WAI")
