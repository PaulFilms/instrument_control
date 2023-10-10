r'''
INCOMPLETE
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import serial


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    INCOMPLETE:
        - Not tested yet 
    '''
    def __init__(self, port: str = "COM1", baudrate: int = 9600, timeout: float = 1) -> None:
        self.DEVICE = serial.Serial(port, baudrate, timeout)

    def CLOSE(self):
        self.DEVICE.close()

    def WR(self, SENTENCE: str):
        '''
        Write
        '''
        bytes_value = SENTENCE.encode('utf-8')
        self.DEVICE.write(bytes_value)

    def RD(self, SENTENCE: str, FLOAT: bool = False) -> str | float:
        '''
        Query
        '''
        bytes_value = SENTENCE.encode('utf-8')
        self.DEVICE.write(bytes_value)
        VALUE = self.DEVICE.readline().decode('utf-8')
        if FLOAT:
            VALUE = float(VALUE)
        return VALUE