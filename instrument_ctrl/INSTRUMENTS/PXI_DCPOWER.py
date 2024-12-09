'''
NI-DCPower (Python module: nidcpower)
[pypi.org](https://pypi.org/project/nidcpower/)
[readthedocs.io](https://nidcpower.readthedocs.io/en/latest/nidcpower.html)

TASK:
    - Comprobar el nivel máximo de salida para evitar crasheo
    ... 

WARNINGS:
    ... 

'''

__update__ = '2024.12.09'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from enum import Enum
from typing import List

''' MAIN LIBRARIES '''
import nidcpower


''' MAIN CLASS
-------------------------------------------------------- '''

BOOLEANS: list = ("TRUE", True, 1, "1", "On", "ON")

class TYPES(Enum):
    VOLTAGE = nidcpower.MeasurementTypes.VOLTAGE
    CURRENT = nidcpower.MeasurementTypes.CURRENT

class OUT_FUNC(Enum):
    VOLTAGE = nidcpower.OutputFunction.DC_VOLTAGE
    CURRENT = nidcpower.OutputFunction.DC_CURRENT

class INSTRUMENT:
    '''
    '''
    def __init__(self, resource: str = ""):
        self.session = nidcpower.Session(resource)
        # self.session.voltage_level_autorange = True
        # self.session.current_level_autorange = True
        # self.session.initiate()

        # 
        self.NMB_FUNCTIONS: List[str] = [
            'DEVICE_INFO',
            'RESET',
            'OUTPUT',
            'VOLT_CONF',
            'CURR_CONF',
            'VOLT_SET',
            'CURR_SET',
            'VOLT_MEAS',
            'CURR_MEAS',
        ]

    def CLOSE(self) -> None:
        '''
        '''
        self.session.output_enabled = False
        self.session.abort()
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
        self.session.output_enabled = False
        self.session.abort()
        self.session.reset()

    def OUTPUT(self, *args) -> None:
        '''
        arg0: bool = State ON / OFF
        arg1: str = Channel
        '''
        ## State
        state: bool = False
        if args[0] in BOOLEANS:
            state = True
        else:
            state = False
        ## Channel
        channel: str = None
        if args[1]:
            channel = str(args[1])
        ## Output
        if channel:
            self.session.channels[channel].output_enabled = state
            if state:
                self.session.channels[channel].initiate()
            else:
                self.session.channels[channel].abort()
        else:
            self.session.output_enabled = state
            if state:
                self.session.initiate()
            else:
                self.session.abort()
    
    def VOLT_CONF(self, *args) -> None:
        '''
        arg0: str = Channel
        '''
        try:
            channel = int(args[0])
            if self.session.channels[str(channel)].output_function == OUT_FUNC.VOLTAGE.value:
                return
            self.session.channels[str(channel)].output_function = OUT_FUNC.VOLTAGE.value
            self.session.channels[str(channel)].voltage_level_autorange = True
            self.session.channels[str(channel)].current_limit_autorange = True
        except:
            print("ERROR VOLT_CONF")

    def CURR_CONF(self, *args) -> None:
        '''
        arg0: str = Channel
        '''
        try:
            channel = int(args[0])
            if self.session.channels[str(channel)].output_function == OUT_FUNC.CURRENT.value:
                return
            self.session.channels[str(channel)].output_function = OUT_FUNC.CURRENT.value
            self.session.channels[str(channel)].current_level_autorange = True
            self.session.channels[str(channel)].voltage_limit_autorange = True
        except:
            print("ERROR CURR_CONF, CHANNEL")

    def VOLT_SET(self, *args) -> None:
        '''
        arg0: float = Value (Voltage)
        arg1: str = Channel
        '''
        ## 
        value: float = float(args[0])
        channel: str = str(args[1])
        ## 
        # self.session.channels[channel].voltage_level_autorange = True
        self.session.channels[channel].voltage_level_range = abs(value)
        self.session.channels[channel].voltage_level = value

    def CURR_SET(self, *args) -> None:
        '''
        arg0: float = Value (Current)
        arg1: str = Channel
        '''
        ## 
        value: float = float(args[0])
        channel: str = str(args[1])
        ## 
        # self.session.channels[channel].current_level_autorange = True
        self.session.channels[channel].current_level_range = abs(value)
        self.session.channels[channel].current_level = value
       
    def VOLT_MEAS(self, *args) -> float:
        '''
        arg0: bool = Channel
        '''
        channel: str = str(args[0])
        meas = self.session.channels[channel].measure(TYPES.VOLTAGE.value)
        return meas
        
    def CURR_MEAS(self, *args) -> float:
        '''
        arg0: str = Channel
        '''
        channel: str = str(args[0])
        meas = self.session.channels[channel].measure(TYPES.CURRENT.value)
        return meas


''' TEST
----------------------------------------------------------------------- '''

# def STANDARD_ROUTINE():
#     with nidcpower.Session("PXI1Slot3") as session:
#         from time import sleep
#         # session.initiate()
#         print(session.instrument_manufacturer, session.instrument_model)
#         print(session.output_function)

#         ## VOLTAGE
#         session.channels['0'].output_function = nidcpower.OutputFunction.DC_VOLTAGE
#         session.channels['0'].voltage_level_autorange = True
#         session.channels['0'].current_limit_autorange = True
#         session.channels['0'].voltage_level = 4
#         session.initiate()

#         ## CURRENT
#         # session.channels['0'].output_function = nidcpower.OutputFunction.DC_CURRENT
#         # session.channels['0'].current_level_autorange = True
#         # session.channels['0'].voltage_level_autorange = True
#         # session.channels['0'].current_level = 0.4

#         ## 
#         session.output_enabled = False
#         sleep(1)
#         session.channels['0'].output_enabled = True
#         # session.output_enabled = True
        
#         # session.initiate()
#         sleep(5)
#         # meas = session.channels['0'].measure(nidcpower.MeasurementTypes.VOLTAGE)
#         meas = session.channels['0'].measure(TYPES.VOLTAGE.value)
#         print(meas)
#         session.output_enabled = False

#     print("FIN")
