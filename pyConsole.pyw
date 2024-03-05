'''
# Py Console

TASK:
WARNINGS:
'''

__version__ = '2024.03.04'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
pass

''' MAIN LIBRARIES '''
from pydeveloptools import func_system as SYS
from instrument_control.VISA import INSTRUMENT as VISA


''' MAIN
-------------------------------------------------------- '''

class pyConsole:
    def __init__(self, NMEAS: int=5) -> None:
        pass

    def CMD_HEADER(self) -> None:
        print()
        print("PYCONSOLE APP")
        print("-------------------------------------------------------------")
        print("version: ", __version__)
        print("autor: ", __author__)
        print("date:", SYS.DATE_GET_NOW())
        print("-------------------------------------------------------------")
        print()

    def INPUT_FORM(self, TITLE: str = "", LIST: list = []) -> None:
        # value = None
        print(f"{TITLE}:")
        print("00 - [EXIT]")
        id = 1
        for point in LIST:
            print(f'{id:02d} - {point}')
            id += 1
        try:
            value = int(input("_ "))
            print()
            if value < 0 or value > len(LIST):
                value = None
        except:
            value = None
        if value == None:
            print()
            print("¡INPUT NOT VALID!")
            print()
        return value

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