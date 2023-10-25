'''
# SPECIAL INSTRUMENTS`

\n`TASK:`
\n`WARNINGS:`
    - If PXI_565X is imported and doesn't have the drivers, it causes a crash
'''
__update__ = '2023.10.11'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum

''' MAIN LIBRARIES '''
from instrument_control.INSTRUMENTS.HP_344XX import INSTRUMENT as HP_344XX
from instrument_control.INSTRUMENTS.FLKE_5XXX import INSTRUMENT as FLKE_5XXX
from instrument_control.INSTRUMENTS.PXI_DMM import INSTRUMENT as PXI_DMM
from instrument_control.INSTRUMENTS.PXI_DCPOWER import INSTRUMENT as PXI_DCPOWER
# from instrument_control.INSTRUMENTS.PXI_565X import INSTRUMENT as PXI_565X


''' MAIN
-------------------------------------------------------- '''

class SPECIAL_INSTRUMENTS(Enum):
    '''
    '''
    HP_344XX = HP_344XX
    FLKE_5XXX = FLKE_5XXX
    PXI_DMM = PXI_DMM
    PXI_DCPOWER = PXI_DCPOWER
    # PXI_565X = PXI_565X
    