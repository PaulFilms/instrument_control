r'''
SPECIAL INSTRUMENTS
TASK:
WARNINGS:
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum

''' MAIN LIBRARIES '''
from INSTRUMENTS.HP_344XX import INSTRUMENT as HP_344XX
from INSTRUMENTS.FLKE_5XXX import INSTRUMENT as FLKE_5XXX
from INSTRUMENTS.PXI_DMM import INSTRUMENT as PXI_DMM
from INSTRUMENTS.PXI_DCPOWER import INSTRUMENT as PXI_DCPOWER



''' MAIN CLASS
-------------------------------------------------------- '''

class SPECIAL_INSTRUMENTS(Enum):
    '''
    '''
    HP_344XX = HP_344XX
    FLKE_5XXX = FLKE_5XXX
    PXI_DMM = PXI_DMM
    PXI_DCPOWER = PXI_DCPOWER
    