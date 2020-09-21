#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def calMSV(DT1,WS1,CS1,HS1,T1,GT1,WC1,RH1,HSI1,DP1,PW1,SP1,B1,A1,DA1,NW1,WBGT1,TWL1,DM1,KEY):
    DT = np.mean(DT1)
    DTstd = np.std(DT1)
    DTvar = np.var(DT1)
    WS = np.mean(WS1)
    WSstd = np.std(WS1)
    WSvar = np.var(WS1)
    CS = np.mean(CS1)
    CSstd = np.std(CS1)
    CSvar = np.var(CS1)
    HS = np.mean(HS1)
    HSstd = np.std(HS1)
    HSvar = np.var(HS1)
    T = np.mean(T1)
    Tstd = np.std(T1)
    Tvar = np.var(T1)
    GT = np.mean(GT1)
    GTstd = np.std(GT1)
    GTvar = np.var(GT1)
    WC = np.mean(WC1)
    WCstd = np.std(WC1)
    WCvar = np.var(WC1)
    RH = np.mean(RH1)
    RHstd = np.std(RH1)
    RHvar = np.var(RH1)
    HSI = np.mean(HSI1)
    HSIstd = np.std(HSI1)
    HSIvar = np.var(HSI1)
    DP = np.mean(DP1)
    DPstd = np.std(DP1)
    DPvar = np.var(DP1)
    PW = np.mean(PW1)
    PWstd = np.std(PW1)
    PWvar = np.var(PW1)
    SP = np.mean(SP1)
    SPstd = np.std(SP1)
    SPvar = np.var(SP1)
    B = np.mean(B1)
    Bstd = np.std(B1)
    Bvar = np.var(B1)
    A = np.mean(A1)
    Astd = np.std(A1)
    Avar = np.var(A1)
    DA = np.mean(DA1)
    DAstd = np.std(DA1)
    DAvar = np.var(DA1)
    NW = np.mean(NW1)
    NWstd = np.std(NW1)
    NWvar = np.var(NW1)
    WBGT = np.mean(WBGT1)
    WBGTstd = np.std(WBGT1)
    WBGTvar = np.var(WBGT1)
    TWL = np.mean(TWL1)
    TWLstd = np.std(TWL1)
    TWLvar = np.var(TWL1)
    DM = np.mean(DM1)
    DMstd = np.std(DM1)
    DMvar = np.var(DM1)
    MEANL =[DT,WS,CS,HS,T,GT,WC,RH,HSI,DP,PW,SP,B,A,DA,NW,WBGT,TWL,DM]
    STDL = [DTstd,WSstd,CSstd,HSstd,Tstd,GTstd,WCstd,RHstd,HSIstd,DPstd,PWstd,SPstd,Bstd,Astd,DAstd,NWstd,WBGTstd,TWLstd,DMstd]
    VARL =[DTvar,WSvar,CSvar,HSvar,Tvar,GTvar,WCvar,RHvar,HSIvar,DPvar,PWvar,SPvar,Bvar,Avar,DAvar,NWvar,WBGTvar,TWLvar,DMvar]
    variable_list = pd.DataFrame([MEANL,STDL,VARL]).transpose()
    variable_list.columns = ['Mean', 'Standard Deviation', 'Variance']
    variable_list.to_csv(KEY+'.csv', encoding='gbk')


def plotHistogram(T1,T2,T3,T4,T5,n):
    sns.set_style('darkgrid')
    fig = plt.figure(figsize=(14,6))
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax1.hist(x=T1, bins=n,color='b',alpha=0.7, rwidth=0.85)
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Temperature [deg C]\nSensor A')
    ax2.hist(x=T2, bins=n,color='b',alpha=0.7, rwidth=0.85)
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Temperature [deg C]\nSensor B')
    ax3.hist(x=T3, bins=n,color='b',alpha=0.7, rwidth=0.85)
    ax3.set_ylabel('Frequency')
    ax3.set_xlabel('Temperature [deg C]\nSensor C')
    ax4.hist(x=T4, bins=n,color='b',alpha=0.7, rwidth=0.85)
    ax4.set_ylabel('Frequency')
    ax4.set_xlabel('Temperature [deg C]\nSensor D')
    ax5.hist(x=T5, bins=n,color='b',alpha=0.7, rwidth=0.85)
    ax5.set_ylabel('Frequency')
    ax5.set_xlabel('Temperature [deg C]\nSensor E')
    fig.suptitle('Histograms for 5 sensors Temperature values('+str(n)+'bins)')
    plt.tight_layout()
    plt.show()


def plotPoligons(T1,T2,T3,T4,T5):
    plt.figure(figsize=(14,5))
    [frequency1, bins1] = np.histogram(T1, bins=50)
    [frequency2, bins2] = np.histogram(T2, bins=50)
    [frequency3, bins3] = np.histogram(T3, bins=50)
    [frequency4, bins4] = np.histogram(T4, bins=50)
    [frequency5, bins5] = np.histogram(T5, bins=50)
    plt.plot(bins1[:-1], frequency1, label='sensor1')
    plt.plot(bins2[:-1], frequency2, label='sensor2')
    plt.plot(bins3[:-1], frequency3, label='sensor3')
    plt.plot(bins4[:-1], frequency4, label='sensor4')
    plt.plot(bins5[:-1], frequency5, label='sensor5')
    plt.ylabel('Frequency')
    plt.xlabel('Temperature [deg C]')
    plt.legend(loc='best')
    plt.title('Frequency poligons for the 5 sensors Temperature values')
    plt.show()


def plotBox(A1,A2,A3,A4,A5,B):
    fig,axes = plt.subplots(1, 5,figsize=(14,5))
    ax1, ax2, ax3, ax4, ax5 = axes.ravel()
    ax1.boxplot(A1, showmeans=True)
    ax2.boxplot(A2, showmeans=True)
    ax3.boxplot(A3, showmeans=True)
    ax4.boxplot(A4, showmeans=True)
    ax5.boxplot(A5, showmeans=True)
    if B == 'WS':
        ax1.set_ylabel('Wind speed [m/s]')
        fig.suptitle("Boxplots for Wind speed")
    if B == 'T':
        ax1.set_ylabel('Temperature [deg C]')
        fig.suptitle("Boxplots for Temperature")
    if B == 'WD':
        ax1.set_ylabel('Wind direction [deg]')
        fig.suptitle("Boxplots for Wind direction")
    plt.tight_layout()
    plt.show()