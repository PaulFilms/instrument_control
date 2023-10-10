r'''
NI-DCPower (Python module: nidcpower)
https://nidcpower.readthedocs.io/en/latest/nidcpower.html

TASK:
    - Comprobar el nivel máximo de salida para evitar crasheo
WARNINGS:
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import nidcpower


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    '''
    
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'RESET',
        'OUTPUT',
        'SET_VOLT',
        'MEAS_VOLT',
        'SET_CURR',
        'MEAS_CURR'
    ]
    
    def __init__(self, resource: str = ""):
        '''
        '''
        self.session = nidcpower.Session(resource)
        self.session.initiate()
        
        self.type_voltage = nidcpower.MeasurementTypes.VOLTAGE
        self.type_current = nidcpower.MeasurementTypes.CURRENT
    
    def CLOSE(self) -> None:
        '''
        '''
        self.session.close()

    def DEVICE_INFO(self) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.session.instrument_manufacturer
        MODEL = self.session.instrument_model
        SERIAL_NUMBER = self.session.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

    def RESET(self, *args) -> None:
        '''
        '''
        self.session.reset()

    def OUTPUT(self, *args) -> None:
        '''
        arg0: bool = ON / OFF
        '''
        output: bool = False
        if len(args) > 0:
            if args[0] == True or args[0] == 1 or args[0] == "1" or args[0] == "ON":
                output = True
        self.session.output_enabled = output
    
    def SET_VOLT(self, *args) -> None:
        '''
        arg0: float = Value (Voltage)
        arg1: bool = Channel
        '''
        channel: int = args[1]
        value = float(args[0])
        self.session.channels[channel].voltage_level = value
       
    def MEAS_VOLT(self, *args) -> float:
        '''
        arg0: bool = Channel
        '''
        channel: int = args[0]
        meas = self.session.channels[channel].measure(self.type_voltage)
        return meas

    def SET_CURR(self, *args) -> None:
        '''
        arg0: float = Value (Current)
        arg1: bool = Channel
        
        '''
        channel: int = args[1]
        value = float(args[0])
        self.session.channels[channel].current_level = value

    def MEAS_CURR(self, *args) -> float:
        '''
        arg0: bool = Channel
        '''
        channel: int = args[0]
        meas = self.session.channels[channel].measure(self.type_current)
        return meas