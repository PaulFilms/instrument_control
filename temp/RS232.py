'''
INCOMPLETE
'''

__update__ = '2024.02.29'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import pyvisa


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    '''
    def __init__(self, resource: str = 'ASRL1::INSTR', timeout: int = 10) -> None:
        RM = pyvisa.ResourceManager()
        RM.list_resources()
        self.DEVICE = rm.open_resource(resource)
        self.DEVICE.read_termination = '\n'
        self.DEVICE.write_termination = '\n'

rm = pyvisa.ResourceManager()
rm.list_resources()

my_instrument = rm.open_resource(INSTR1)
my_instrument.read_termination = '\n'
my_instrument.write_termination = '\n'
v = my_instrument.query('*IDN?')



'''
-----------------------------------------------------------
'''
# import serial

# class INSTRUMENT:
#     '''
#     INCOMPLETE:
#         - Not tested yet 
#     '''
#     def __init__(self, port: str = "COM1", baudrate: int = 9600, timeout: float = 1) -> None:
#         self.DEVICE = serial.Serial(port, baudrate, timeout)

#     def CLOSE(self):
#         self.DEVICE.close()

#     def WR(self, SENTENCE: str):
#         '''
#         Write
#         '''
#         bytes_value = SENTENCE.encode('utf-8')
#         self.DEVICE.write(bytes_value)

#     def RD(self, SENTENCE: str, FLOAT: bool = False) -> str | float:
#         '''
#         Query
#         '''
#         bytes_value = SENTENCE.encode('utf-8')
#         self.DEVICE.write(bytes_value)
#         VALUE = self.DEVICE.readline().decode('utf-8')
#         if FLOAT:
#             VALUE = float(VALUE)
#         return VALUE




class RS_TEST:
    def __init__(self) -> None:
        rm = pyvisa.ResourceManager()
        rm.list_resources()
        # ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
        inst = rm.open_resource('GPIB0::12::INSTR')
        print(inst.query("*IDN?\n"))