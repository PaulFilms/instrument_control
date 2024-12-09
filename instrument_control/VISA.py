'''
# Toolset for remote control of instruments VISA

TASK:
WARNINGS:
'''

__update__ = '2024.03.04'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import pyvisa


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    visa_resource: str
        - GPIB    -> GPIB0::17::INSTR
        - USB     -> USB0::0x0AAD::0x014E::101060::INSTR
        - PXI     -> PXI1Slot2
        - RS-232  -> ASRL1::INSTR
    
    timeout: int (seconds) = 10 seconds default
    '''
    def __init__(self, resource: str, timeout: int = 10, termination: bool = None) -> None:
        RM = pyvisa.ResourceManager()
        RM.list_resources()
        self.DEVICE = RM.open_resource(resource)
        self.DEVICE.timeout = int(timeout*1000)
        if termination:
            self.DEVICE.read_termination = '\n'
            self.DEVICE.write_termination = '\n'
    
    def CLOSE(self) -> None:
        '''
        '''
        self.DEVICE.close()

    def DEVICE_INFO(self) -> str:
        '''
        '''
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        IDNL = IDN.split(chr(44))
        MANUFACTURER = IDNL[0]
        MODEL = IDNL[1]
        SERIAL_NUMBER = IDNL[2]
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn
    
    def WR(self, SENTENCE: str) -> None:
        '''
        Write
        '''
        self.DEVICE.write(SENTENCE)
    
    def RD(self, SENTENCE: str, FLOAT: bool = False) -> str | float:
        '''
        Query
        '''
        VALUE = self.DEVICE.query(SENTENCE)
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE

    def READ(self, FLOAT: bool = False) -> str | float:
        '''
        Read
        '''
        VALUE = self.DEVICE.read()
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE
    
    def OPC(self, *args) -> None:
        self.DEVICE.write("*CLS")
        # self.DEVICE.write("ESE 1")
        # self.DEVICE.write("SRE 32")
        self.DEVICE.write("*OPC?")
        self.DEVICE.read()