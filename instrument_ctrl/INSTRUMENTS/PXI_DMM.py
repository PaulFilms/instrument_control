'''
`NI-DMM` (Python module: nidmm)
[readthedocs.io](https://nidmm.readthedocs.io/en/latest/nidmm.html)

INCOMPLETE:
    - En caso de error hay que devolver un false
    - Hay que cerrar session con self.session.close
    - Al usar range=-1 lo configuramos en AUTO
    - Hay que buscar las opciones de NULL
    - Añadir espera o indicación al terminar el self test y el self cal

mypyc:
    mypyc INSTRUMENTS/PXI_DMM.py
    import nidmm # type: ignore / ** Hay que incluirla en el pip freeze para importarla
    En el valor -1 para rango auto, estaba re-definiendo la variable, y eso no le gusta a mypyc
    NMB_FUNCTIONS genera error al indicarlo de esa forma en el class, hay que plantearse sacarlo fuera
'''

__version__ = '2024.10.17' # + '_Compile'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from typing import List

''' EXTERNAL LIBRARIES '''
import nidmm # type: ignore[import-untyped]


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    def __init__(self, resource: str = ""):
        self.session = nidmm.Session(resource)
        
        # 
        self.NMB_FUNCTIONS: List[str] = [
            'DEVICE_INFO',
            'SELF_TEST',
            'SELF_CAL',
            'CONFIG_VDC',
            'CONFIG_VAC',
            'CONFIG_RES_2W',
            'CONFIG_RES_4W',
            'CONFIG_IDC',
            'CONFIG_IAC',
            'CONFIG_FREQ',
            'CONFIG_TEMP',
            'MEAS_INFO',
            'MEAS',
        ]
    
    def CLOSE(self) -> None:
        self.session.close()

    def DEVICE_INFO(self, *args) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.session.instrument_manufacturer
        MODEL = self.session.instrument_model
        SERIAL_NUMBER = self.session.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

    def SELF_TEST(self, *args) -> None:
        '''
        No args
        '''
        self.session.self_test()

    def SELF_CAL(self, *args) -> None:
        '''
        No args
        '''
        self.session.self_cal()

    def CONFIG_VDC(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.DC_VOLTS,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
    
    def CONFIG_VAC(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## ARG1 (RANGE VALUE)
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## ARG2 (DIGITS VALUE)
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.AC_VOLTS,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
        self.session.ac_min_freq = 10
    
    def CONFIG_RES_2W(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.TWO_WIRE_RES,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_RES_4W(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.FOUR_WIRE_RES,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_IDC(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.DC_CURRENT,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_IAC(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.AC_CURRENT,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_FREQ(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.FREQ,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def CONFIG_TEMP(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value = -1.0
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[1])
        else: 
            digits_value = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.TEMPERATURE,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )

    def MEAS_INFO(self, *args) -> str:
        '''
        Get info (Measure Function, Range, Digits) about config

        No args
        '''
        FUNCTION = self.session.function
        RANGE = self.session.range
        DIGITS = self.session.resolution_digits
        return f"{FUNCTION}, {RANGE}, {DIGITS}"

    def MEAS(self, *args) -> float:
        '''
        Get measaure like float value

        No args
        '''
        try:
            measure = self.session.read()
            return float(measure)
        except:
            print("MEAS ERROR / Float value")
            return 0.0  