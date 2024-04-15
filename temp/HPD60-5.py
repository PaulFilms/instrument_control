## EXCEL
import os
from pydeveloptools.func_xlsx import XLSREPORT
from pydeveloptools.func_system import DATE_GET_NOW
EXCEL = XLSREPORT(os.path.join(r"C:\Users\GONZA_PA\Desktop","REPORT_HPD605"))

## HEADER
EXCEL.WR_HEADER(EXCEL.ROW, 1, "REPORT")
EXCEL.WR_HEADER(EXCEL.ROW, 3, DATE_GET_NOW())
EXCEL.ROW_INC()
EXCEL.LOW_BORDER(EXCEL.ROW)
EXCEL.ROW_INC(3)
EXCEL.SAVE()

## INSTRUMENTS
from instrument_control import VISA
from instrument_control.SPECIAL import HP_344XX
DUT = VISA.INSTRUMENT("GPIB0::2::INSTR")
DMM = HP_344XX("USB0::0x2A8D::0x1301::SG60000138::INSTR")
N_MEAS = 5

## PROCEDURES
from time import sleep

class PROCEDURES:
    @staticmethod
    def VDC():
        EXCEL.ROW = 5
        EXCEL.WR_TITLE(EXCEL.ROW, 1, "DC VOLTAGE ACCURACY")
        EXCEL.WR(EXCEL.ROW, 6, DATE_GET_NOW())
        EXCEL.ROW_INC(2)
        LIST = [
            1,
            2,
            3,
            5,
            10,
            20,
            30,
            40,
            50,
            60,
        ]
        ## INIT
        DUT.WR(f"VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT OFF")

        ## LOOP
        for i in LIST:
            print("VALUE:", i)
            DUT.WR(f"VSET {i}")
            DUT.WR("ISET 1.0")
            DUT.WR("OUT ON")
            sleep(1)
            DMM.CONFIG("VOLTAGE_DC")
            for meas in range(N_MEAS):
                ## DMM
                value = DMM.MEAS()
                value = float(value)
                EXCEL.WR(EXCEL.ROW, 2, "DMM:")
                EXCEL.WR(EXCEL.ROW, 3+meas, value)
                ## DUT
                value = DUT.RD("VOUT?")
                value = value.replace("VOUT", str())
                value = value.replace(" ", str())
                value = float(value)
                EXCEL.WR(EXCEL.ROW, 4+N_MEAS, "DUT:")
                EXCEL.WR(EXCEL.ROW, 5+N_MEAS+meas, value)
            EXCEL.ROW_INC()
        
        ## FIN
        EXCEL.ROW_INC()
        DUT.WR(f"VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT OFF")
        EXCEL.SAVE()

    @staticmethod
    def ADC():
        EXCEL.ROW = 19
        EXCEL.WR_TITLE(EXCEL.ROW, 1, "DC CURRENT ACCURACY")
        EXCEL.WR(EXCEL.ROW, 6, DATE_GET_NOW())
        EXCEL.ROW_INC(2)
        LIST = [
            1,
            2,
            3,
            4,
            5,
        ]
        ## INIT
        DUT.WR(f"VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT OFF")

        ## LOOP
        for i in LIST:
            print("VALUE:", i)
            DUT.WR("VSET 1")
            DUT.WR(f"ISET {i}")
            DUT.WR("OUT ON")
            sleep(1)
            DMM.CONFIG("CURRENT_DC")
            DMM.WR("SENS:CURR:DC:TERM 10")
            for meas in range(N_MEAS):
                ## DMM
                value = DMM.MEAS()
                value = float(value)
                EXCEL.WR(EXCEL.ROW, 2, "DMM:")
                EXCEL.WR(EXCEL.ROW, 3+meas, value)
                ## DUT
                value = DUT.RD("IOUT?")
                value = value.replace("IOUT", str())
                value = value.replace(" ", str())
                value = float(value)
                EXCEL.WR(EXCEL.ROW, 4+N_MEAS, "DUT:")
                EXCEL.WR(EXCEL.ROW, 5+N_MEAS+meas, value)
            EXCEL.ROW_INC()
        
        ## FIN
        EXCEL.ROW_INC()
        DUT.WR(f"VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT OFF")
        EXCEL.SAVE()

    @staticmethod
    def STOP():
        DUT.WR("VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT OFF")
        # print(DUT.RD("ID?"))

    @staticmethod
    def TEST():
        DUT.WR("VSET 0")
        DUT.WR("ISET 0")
        DUT.WR("OUT ON")

TEST = [PROCEDURES.STOP, PROCEDURES.VDC, PROCEDURES.ADC, PROCEDURES.TEST]

menu: str = "\nSELECT PROCEDURE:\n\n"
for p in TEST: menu += f"{TEST.index(p)} - {p.__name__}\n"
select = input(f"{menu}--> ")

try:
    select = int(select)
    print()
    print("START TEST:")
    print()
    TEST[select]()
    PROCEDURES.STOP()
    print()
    print("STOP TEST.")
    print()
except:
    print("ERROR !!")
EXCEL.close()
