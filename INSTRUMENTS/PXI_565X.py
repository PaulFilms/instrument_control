r'''
NI-RFSG (Python module: nirfsg)
pip install nirfsg
https://pypi.org/project/nirfsg/
'''

__update__ = '2023.10.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import nirfsg


''' MAIN CLASS
-------------------------------------------------------- '''

class INSTRUMENT:
    '''
    '''
    NMB_FUNCTIONS = [
        'DEVICE_INFO',
    ]

    def __init__(self, resource: str = ""):
        '''
        '''
        self.session = nirfsg.Session(resource)
        self.session.initiate()

    def DEVICE_INFO(self) -> str:
        '''
        Get info (Manufacturer, Model, Serial Id) about device
        '''
        MANUFACTURER = self.session.instrument_manufacturer
        MODEL = self.session.instrument_model
        SERIAL_NUMBER = self.session.serial_number
        idn = f"{MANUFACTURER},{MODEL},{SERIAL_NUMBER}"
        return idn