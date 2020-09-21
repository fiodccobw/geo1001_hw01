#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513


import hw01A1
import hw01A2
import hw01A3
import hw01A4
import bonus
import xlrd
import numpy



def readHeat(n):
    workbook = xlrd.open_workbook(r'HEAT.xls')
    sheet = workbook.sheet_by_name('sheet'+str(n))
    dat = []
    for a in range(5,sheet.nrows):
        cells = sheet.row_values(a)
        dat.append(cells)
    DT = []
    WS = []
    CS = []
    HS = []
    T = []
    GT = []
    WC = []
    RH = []
    HSI = []
    DP = []
    PW = []
    SP = []
    B = []
    A = []
    DA = []
    NW = []
    WBGT = []
    TWL = []
    DM = []
    date = numpy.array(dat)
    for i in range(0,len(dat)):
        fields = date[i,:]
        DT.append(float(fields[1]))
        WS.append(float(fields[2]))
        CS.append(float(fields[3]))
        HS.append(float(fields[4]))
        T.append(float(fields[5]))
        GT.append(float(fields[6]))
        WC.append(float(fields[7]))
        RH.append(float(fields[8]))
        HSI.append(float(fields[9]))
        DP.append(float(fields[10]))
        PW.append(float(fields[11]))
        SP.append(float(fields[12]))
        B.append(float(fields[13]))
        A.append(float(fields[14]))
        DA.append(float(fields[15]))
        NW.append(float(fields[16]))
        WBGT.append(float(fields[17]))
        TWL.append(float(fields[18]))
        DM.append(float(fields[19]))

    return DT,WS,CS,HS,T,GT,WC,RH,HS,DP,PW,SP,B,A,DA,NW,WBGT,TWL,DM

DT1,WS1,CS1,HS1,T1,GT1,WC1,RH1,HSI1,DP1,PW1,SP1,B1,A1,DA1,NW1,WBGT1,TWL1,DM1 = readHeat(1)
DT2,WS2,CS2,HS2,T2,GT2,WC2,RH2,HSI2,DP2,PW2,SP2,B2,A2,DA2,NW2,WBGT2,TWL2,DM2 = readHeat(2)
DT3,WS3,CS3,HS3,T3,GT3,WC3,RH3,HSI3,DP3,PW3,SP3,B3,A3,DA3,NW3,WBGT3,TWL3,DM3 = readHeat(3)
DT4,WS4,CS4,HS4,T4,GT4,WC4,RH4,HSI4,DP4,PW4,SP4,B4,A4,DA4,NW4,WBGT4,TWL4,DM4 = readHeat(4)
DT5,WS5,CS5,HS5,T5,GT5,WC5,RH5,HSI5,DP5,PW5,SP5,B5,A5,DA5,NW5,WBGT5,TWL5,DM5 = readHeat(5)




hw01A1.calMSV(DT1,WS1,CS1,HS1,T1,GT1,WC1,RH1,HSI1,DP1,PW1,SP1,B1,A1,DA1,NW1,WBGT1,TWL1,DM1,'A')
hw01A1.calMSV(DT2,WS2,CS2,HS2,T2,GT2,WC2,RH2,HSI2,DP2,PW2,SP2,B2,A2,DA2,NW2,WBGT2,TWL2,DM2,'B')
hw01A1.calMSV(DT3,WS3,CS3,HS3,T3,GT3,WC3,RH3,HSI3,DP3,PW3,SP3,B3,A3,DA3,NW3,WBGT3,TWL3,DM3,'C')
hw01A1.calMSV(DT4,WS4,CS4,HS4,T4,GT4,WC4,RH4,HSI4,DP4,PW4,SP4,B4,A4,DA4,NW4,WBGT4,TWL4,DM4,'D')
hw01A1.calMSV(DT5,WS5,CS5,HS5,T5,GT5,WC5,RH5,HSI5,DP5,PW5,SP5,B5,A5,DA5,NW5,WBGT5,TWL5,DM5,'E')
hw01A1.plotHistogram(T1,T2,T3,T4,T5,5)
hw01A1.plotHistogram(T1,T2,T3,T4,T5,50)
hw01A1.plotPoligons(T1,T2,T3,T4,T5)
hw01A1.plotBox(T1,T2,T3,T4,T5,'T')
hw01A1.plotBox(WS1,WS2,WS3,WS4,WS5,'WS')
hw01A1.plotBox(DT1,DT2,DT3,DT4,DT5,'WD')
hw01A2.plotPmf(T1,T2,T3,T4,T5)
hw01A2.plotPdf(T1,T2,T3,T4,T5)
hw01A2.plotCdf(T1,T2,T3,T4,T5,'T')
hw01A2.plotWS(WS1,WS2,WS3,WS4,WS5)
hw01A3.showCorrelation(T1,T2,T3,T4,T5,'T')
hw01A3.plotScatter(T1,T2,T3,T4,T5,'T')
hw01A3.showCorrelation(WBGT1,WBGT2,WBGT3,WBGT4,WBGT5,'WBGT')
hw01A3.plotScatter(WBGT1,WBGT2,WBGT3,WBGT4,WBGT5,'WBGT')
hw01A3.showCorrelation(CS1,CS2,CS3,CS4,CS5,'CS')
hw01A3.plotScatter(CS1,CS2,CS3,CS4,CS5,'CS')
hw01A4.calcCI(T1,T2,T3,T4,T5,'T')
hw01A4.calcCI(WS1,WS2,WS3,WS4,WS5,'WS')
hw01A4.hypothesisTest(T1,T2,T3,T4,T5,'T')
hw01A4.hypothesisTest(WS1,WS2,WS3,WS4,WS5,'WS')
bonus.calHC(T1,T2,T3,T4,T5)


