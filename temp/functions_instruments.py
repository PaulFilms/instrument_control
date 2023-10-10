r'''
NOTES:
    -
TASK:
    - Implementar la comunicación por RS-232
    - SPECIAL INSTRUMENTS
        Fluke 5xxx: esperar a quitar indicador de U, checkear si serie 700 o 500 para funciones especificas
        HP 34xxx: MEAS, CONFIG
        HP 3458A: CONFIG, MEAS
        R&S SM+NRP: ALC control, NRP-Zero, NRP-Meas, 
WARNINGS
    - al usar "sleep" crashea desde una app con PyQt, estar atento (19.09.2023)
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from dataclasses import dataclass
from enum import Enum
# from time import sleep

''' VISA INSTRUMENT
--------------------------------------------------------  '''

class VISA_INSTRUMENT:
    '''
    visa_resource: GPIB0::17::INSTR / USB0::0x0AAD::0x014E::101060::INSTR / PXI1Slot2\n
    timeout (seconds) = 10 seconds default
    '''
    def __init__(self, resource: str, timeout: int = 10) -> None:
        import pyvisa
        RM = pyvisa.ResourceManager()
        RM.list_resources()
        self.DEVICE = RM.open_resource(resource)
        self.DEVICE.timeout = timeout * 1000 # miliseconds
    
    def CLOSE(self) -> None:
        self.DEVICE.close()

    def DEVICE_INFO(self) -> str:
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
    
    def OPC(self) -> None:
        self.DEVICE.write("*CLS")
        # self.DEVICE.write("ESE 1")
        # self.DEVICE.write("SRE 32")
        self.DEVICE.write("*OPC?")
        self.DEVICE.read()


''' RS232 INSTRUMENT
--------------------------------------------------------  '''

class RS232_INSTRUMENT:
    '''
    INCOMPLETE:
        - Not tested yet 
    '''
    def __init__(self, port: str = "COM1", baudrate: int = 9600, timeout: float = 1) -> None:
        import serial
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


''' PXI INSTRUMENT
--------------------------------------------------------  '''

''' NI MODULES
NI-DCPower (Python module: nidcpower)
NI-Digital Pattern Driver (Python module: nidigital)
NI-DMM (Python module: nidmm)
NI-FGEN (Python module: nifgen)
NI-ModInst (Python module: nimodinst)
NI-SCOPE (Python module: niscope)
NI Switch Executive (Python module: nise)
NI-SWITCH (Python module: niswitch)
NI-TClk (Python module: nitclk)
'''

# import nidmm

class PXI_DMM:
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
        import nidmm
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
        self.session.self_test()

    def SELF_CAL(self, *args) -> None:
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
        measure = self.session.read()
        try:
            measure = float(measure)
            return measure
        except:
            print("MEAS ERROR / Float value")
            return 0.0  

    def CONFIG_VDC(self, *args) -> None:
        '''
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

class PXI_DCPOWER:
    '''
    https://nidcpower.readthedocs.io/en/latest/nidcpower.html
    '''
    
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'OUTPUT',
        'SET_VOLT',
        'MEAS_VOLT',
        'SET_CURR',
        'MEAS_CURR'
    ]
    
    def __init__(self, resource: str = ""):
        '''
        '''
        import nidcpower
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

    def OUTPUT(self, *args) -> None:
        '''
        arg1: bool = ON / OFF
        '''
        output: bool = False
        if len(args) > 0:
            if args[0] == True or args[0] == 1 or args[0] == "1":
                output = True
        self.session.output_enabled = output
    
    def SET_VOLT(self, *args) -> None:
        '''
        arg1: bool = Channel
        arg2: float = Value (Voltage)
        '''
        channel: int = args[0]
        value: float = args[1]
        self.session.channels[channel].voltage_level = value
       
    def MEAS_VOLT(self, *args) -> float:
        '''
        arg1: bool = Channel
        '''
        channel: int = args[0]
        meas = self.session.channels[channel].measure(self.type_voltage)
        return meas

    def SET_CURR(self, *args) -> None:
        '''
        arg1: bool = Channel
        arg2: float = Value (Current)
        '''
        channel: int = args[0]
        value: float = args[1]
        self.session.channels[channel].current_level = value

    def MEAS_CURR(self, *args) -> float:
        '''
        arg1: bool = Channel
        '''
        channel: int = args[0]
        meas = self.session.channels[channel].measure(self.type_current)
        return meas

''' SPECIAL INSTRUMENT
--------------------------------------------------------  '''

class HP_344XX(VISA_INSTRUMENT):
    '''
    Especial functions for the device:
        - TYPE: MULTIMETER
        - MANUFACTURER: HP / AGILENT / KEYSIGHT
        - MODEL: 344XX
    '''
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
        'MEAS'
    ]
    def __init__(self, resource: str, timeout: int = 10):
        super().__init__(resource, timeout)

    def DEVICE_INFO(self, *args) -> str:
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        IDNL = IDN.split(chr(44))
        MANUFACTURER = IDNL[0]
        MODEL = IDNL[1]
        SERIAL_NUMBER = IDNL[2]
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn
    
    def CONFIG(self, *args) -> None:
        '''
        '''
        self.WR()
    
    def MEAS(self, *args) -> float:
        '''
        '''
        self.WR('*CLS')
        self.WR('TRIG:SOUR BUS')
        self.WR('INIT')
        self.WR('*TRG')
        self.OPC()
        self.WR('FETC?')
        meas = self.READ()
        meas = float(meas)
        return meas

class FLKE_5XXX(VISA_INSTRUMENT):
    '''
    Especial functions for the device:
        - TYPE: CALIBRATOR
        - MANUFACTURER: FLUKE
        - MODEL: 5xxx
    '''

    NMB_FUNCTIONS = [
        'OPER',
        'STBY'
    ]

    def __init__(self, resource=str, timeout: int = 10):
        super().__init__(resource, timeout)
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        MODEL = IDN.split(chr(44))[1]
        self.MODEL = None
        if MODEL[0:2] == "57":
            self.MODEL = "5700"
        if MODEL[0:2] == "55":
            self.MODEL = "5500"
    
    def DEVICE_INFO(self) -> str:
        self.WR("*CLS")
        IDN = self.RD("*IDN?; *WAI")
        IDNL = IDN.split(chr(44))
        MANUFACTURER = IDNL[0]
        MODEL = IDNL[1]
        SERIAL_NUMBER = IDNL[2]
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn
    
    def OPER(self, VALUE: str, UNIT: str) -> None:
        '''
        '''
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("OPER")
        self.OPC()

    def STBY(self, *args) -> None:
        '''
        '''
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("OUT 0 HZ")
        self.WR("OUT 0 V")
        self.WR("STBY")
        self.OPC()

    def OUT_VPP(self, *args):
        pass

    def FOUR_WIRES(self, *args) -> None:
        pass

class RS_SM(VISA_INSTRUMENT):
    '''
    Especial functions for the device:
        - TYPE: SIGNAL GENERATOR
        - MANUFACTURER: ROHDE & SCHWARZ
        - MODEL: SMx
    '''
    def __init__(self, resource: str, timeout: int = 10):
        super().__init__(resource, timeout)
        
        ## NMBv3 FUNCTIONS
        self.NMB_FUNCTIONS: tuple = (
            self.STBY,
            self.NRP_MEAS,
            self.NRP_ALC
        )
    
    def STBY(self, *args):
        self.WR("*CLS")
        self.WR("ESE 1")
        self.WR("SRE 32")
        self.WR("SOUR:POW -100 DBM")
        self.WR("OUTP:STAT OFF")
        self.OPC()
    
    def NRP_MEAS(self, *args):
        '''
        '''
        pass

    def NRP_ALC(self, *args):
        '''
        Set Power Level to Target Level in NRP
        ** Make sure the generator has a NRP connected and is identified as 1
        INCOMPLETE:
        '''
        # Chekear la sonda
        # Revisar el modelo
        # En caso de fallo llamar STBY
        pass

class SPECIAL_INSTRUMENTS(Enum):
    '''
    '''
    # FLKE_5XXX = FLKE_5XXX
    # RS_SM = RS_SM
    PXI_DMM = PXI_DMM
    PXI_DCPOWER = PXI_DCPOWER


''' TEST
--------------------------------------------------------  '''