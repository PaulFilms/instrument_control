'''
`NI-DMM` (Python module: nidmm)
https://nidmm.readthedocs.io/en/latest/nidmm.html
'''
__update__ = '2023.10.25'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import nidmm


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    INCOMPLETE:
    - En caso de error hay que devolver un false
    - Hay que cerrar session con self.session.close
    - Al usar range=-1 lo configuramos en AUTO
    - Hay que buscar las opciones de NULL
    - Añadir espera o indicación al terminar el self test y el self cal
    '''

    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'SELF_TEST',
        'SELF_CAL',
        'MEAS_INFO',
        'MEAS',
        'CONFIG_VDC',
        'CONFIG_VAC',
        'CONFIG_RES_2W',
        'CONFIG_RES_4W',
        'CONFIG_IDC',
        'CONFIG_IAC',
        'CONFIG_FREQ',
        'CONFIG_TEMP'
        ]
    
    def __init__(self, resource: str = ""):
        self.session = nidmm.Session(resource)
    
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

    def MEAS_INFO(self, *args) -> str:
        '''
        Get info (Measure Function, Range, Digits) about config
        '''
        FUNCTION = self.session.function
        RANGE = self.session.range
        DIGITS = self.session.resolution_digits
        config = f"{FUNCTION}, {RANGE}, {DIGITS}"
        return config

    def MEAS(self, *args) -> float:
        '''
        No args
        Get measaure like float value
        '''
        measure = self.session.read()
        try:
            measure = float(measure)
            return measure
        except:
            print("MEAS ERROR / Float value")
            return 0.0  

    def CONFIG_VDC(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.AC_VOLTS,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
    
    def CONFIG_RES_2W(self, *args) -> None:
        '''
        arg1: int = RANGE (-1 AUTO)
        arg2: float = DIGITS RESOLUTION (6.5)
        '''
        ## RANGE
        if len(args) > 0 and args[0] and args[0] != "": 
            range_value = float(args[0])
        else: 
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
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
            range_value: float = -1
        ## DIGITS
        if len(args) > 1 and args[1] and args[1] != "": 
            digits_value = float(args[0])
        else: 
            digits_value: float = 6.5
        ## CONFIG
        self.session.configure_measurement_digits(
                measurement_function=nidmm.Function.TEMPERATURE,
                range = float(range_value),
                resolution_digits= float(digits_value)
                )
