'''
# Test Console (INCOMPLETE)

TASK:
WARNINGS:
'''

__version__ = '2024.03.04'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
from dataclasses import dataclass
from typing import Tuple, List

''' MAIN LIBRARIES '''
from pydeveloptools import func_system as SYS
from instrument_control.VISA import INSTRUMENT as VISA
from instrument_control.SPECIAL import SPECIAL_INSTRUMENTS as SPECIAL

''' JUPYTER LIBRARIES'''
# import ipywidgets as widgets
# from IPython.display import display


''' MAIN
-------------------------------------------------------- '''

@dataclass
class INSTRUMENT:
    NAME: str
    RESOURCE: str
    TYPE: VISA | SPECIAL

@dataclass
class TEST:
    TITLE: str
    CONFIG: str
    LOOP_LIST: tuple
    PROCEDURE: classmethod

class APP:
    '''
    '''
    def __init__(self, NMEAS: int=5, TEMPLATE: List[TEST] = None) -> None:
        self.NMEAS: int = NMEAS
        self.TEMPLATE = TEMPLATE

        ## INIT
        self.CMD_WR_HEADER()
        self.INPUT_FORM()
        # 
        print("STOP APP")
        print()

    # def TEMPLATE_CHECK(self):
    #     if self.TEMPLATE:
    #         TITLE('TEMPLATE AVAILABLE')
    #     else:
    #         TITLE("TEMPLATE NOT AVAILABLE")

    def CMD_WR_HEADER(self) -> None:
        '''
        Print Version Info
        '''
        print()
        print("TEST PYCONSOLE APP")
        print("-------------------------------------------------------------")
        print("version: ", __version__)
        print("autor: ", __author__)
        print("date:", SYS.DATE_GET_NOW())
        print("-------------------------------------------------------------")
        print()

    def CMD_WR_TITLE(self, text: str) -> None:
        '''
        '''
        print(text)
        print("-------------------------------------------------------------")
        print()

    def INPUT_FORM(self) -> None:
        '''
        '''
        # value = None
        # print(f"{TITLE}:")
        print("00 - [EXIT]")
        id = 1
        for point in self.TEMPLATE:
            print(f'{id:02d} - {point.TITLE}')
            id += 1
        try:
            value = int(input("_ "))
            print()
            if value < 0 or value > len(self.TEMPLATE):
                value = None
        except:
            value = None
        if value == None:
            print()
            print("¡INPUT NOT VALID!")
            print()
        # return value

    def TEST_RUN(self):
        '''
        INCOMPLETE:
        - Comprobar idn antes de la prueba
        - Bloquear APP al estar en RUN
        - Añadir boton de PANIC
        '''
        TBL_TEST = self.tbl_test
        TBL_INSTRU = self.tbl_instruments

        ## VALID TEST
        if TBL_TEST.rowCount() == 0:
            QT.INFOBOX("ATTENTION", "SELECT A VALID TEST")
            return

        currentTest = QT.CELL_RD(TBL_TEST, TBL_TEST.currentRow(), 1)
        TEST = SYS.CHECK_FUNCTIONS(self.TEMPLATE)
        tIndex = [testNames[0] for testNames in TEST].index(currentTest)
        STANDARDS = {}
        for row in range(TBL_INSTRU.rowCount()):
            TYPE = QT.CELL_RD(TBL_INSTRU, row, 0)
            DEVICE = QT.CELL_RD(TBL_INSTRU, row, 1)
            RESOURCE = QT.CELL_RD(TBL_INSTRU, row, 2)
            TIMEOUT = QT.CELL_RD(TBL_INSTRU, row, 4)
            ERROR = QT.CELL_RD(TBL_INSTRU, row, 5)
            STANDARDS[DEVICE] = None
            try:
                if TYPE == "VISA":
                    STANDARDS[DEVICE] = INST.VISA_INSTRUMENT(RESOURCE, TIMEOUT)
                if TYPE == "NI-DMM":
                    STANDARDS[DEVICE] = INST.PXI_DMM_INSTRUMENT(RESOURCE)
            except:
                QT.INFOBOX("ERROR", "CHECK AGAIN THE INSTRUMENTS")
                return
        ##
        try:
            self.LOG("# START TEST")
            self.LOG()
            self.NMEAS = self.sb_nmeas.value()
            self.EXCEL.WR_TITLE(self.EXCEL.ROW_GET(), 1, currentTest)
            self.EXCEL.WR(self.EXCEL.ROW_GET(), 6, SYS.GET_DATE_NOW())
            self.EXCEL.ROW_INC(2)
            self.tab_options.setCurrentIndex(0)
            TEST[tIndex][1](self, STANDARDS)
            for standard in STANDARDS: standard.CLOSE()
            self.EXCEL.SAVE()
            self.LOG()
            self.LOG("# STOP TEST")
            self.LOG()
        except:
            QT.INFOBOX("ERROR", "PROBLEMS IN TEST")
            return


''' APP
-------------------------------------------------------- '''

# if __name__ == '__main__':
#     APP()