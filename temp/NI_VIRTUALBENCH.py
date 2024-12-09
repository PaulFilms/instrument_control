r'''
INCOMPLETE
PyMeasure
'''

__update__ = '2024.12.09'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

from pymeasure.instruments.ni import VirtualBench
# from pyvirtualbench import PyVirtualBench, PyVirtualBenchException, Waveform

class INSTRUMENT:
    '''
    INCOMPLETE
    '''
    def __init__(self, resource: str):
        
        self.virtualbench = VirtualBench(device_name=resource)
        # self.fgen = self.virtualbench.acquire_function_generator()
        self.fgen = self.virtualbench.FunctionGenerator()

    def DEVICE_INFO(self) -> str:
        '''
        INCOMPLETE
        '''
        MANUFACTURER = "NATIONAL INSTRUMENTS"
        MODEL = self.virtualbench.device_name
        SERIAL_NUMBER = ""
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn

    # def FGEN_ONOFF(self):
    #     self.fgen.run()
    #     self.fgen.

    def FGEN_SETUP(self,
                waveform_function: str,
                frequency: float, # Hz
                amplitude: float, # Vpp
                dc_offset: float, # V
                duty_cycle: float, # %
                ) -> None:
        '''
        waveform_function: DC / SINE / SQUARE / TRIANGLE
        frequency (Hz) / amplitude (Vpp) / dc_offset (V) / duty_cycle (%)
        '''
        # if waveform_function == "DC":
        #     waveForm = Waveform.DC
        # if waveform_function == "SINE":
        #     waveForm = Waveform.SINE
        # if waveform_function == "SQUARE":
        #     waveForm = Waveform.SQUARE
        # if waveform_function == "TRIANGLE":
        #     waveForm = Waveform.TRIANGLE
        self.fgen.configure_standard_waveform(
            waveform_function="", 
            amplitude=amplitude, 
            dc_offset=dc_offset, 
            frequency=frequency, 
            duty_cycle=duty_cycle
            )

