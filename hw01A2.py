#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def pmf(sample):
    t = pd.Series(sample)
    c = t.value_counts()
    p = c / len(sample)
    return p


def plotPmf(T1,T2,T3,T4,T5):
    sns.set()
    T = [T1,T2,T3,T4,T5]
    fig = plt.figure(figsize=(14, 5))
    ax1 = plt.subplot(231)
    ax2 = plt.subplot(232)
    ax3 = plt.subplot(233)
    ax4 = plt.subplot(234)
    ax5 = plt.subplot(235)
    axes = [ax1,ax2,ax3,ax4,ax5]
    for i in range(5):
        df = pmf(T[i])
        df1 = df.to_frame()
        df1.reset_index(inplace=True)
        df1.columns=['T','pmf']
        df1 = df1.astype(float)
        c=df1.sort_values(by=['T'])
        axes[i].bar(c['T'], c['pmf'],color ='b',edgecolor ='b', width=0.1)
    ax1.set_ylabel('Probability')
    ax1.set_xlabel('Temperature [deg C]\nSensor A')
    # ax2.bar(bins2[:-1], t2, width=0.51,edgecolor='c')
    ax2.set_ylabel('Probability')
    ax2.set_xlabel('Temperature [deg C]\nSensor B')
    # ax3.bar(bins3[:-1], t3, width=0.54,edgecolor='c')
    ax3.set_ylabel('Probability')
    ax3.set_xlabel('Temperature [deg C]\nSensor C')
    # ax4.bar(bins4[:-1], t4, width=0.51,edgecolor='c')
    ax4.set_ylabel('Probability')
    ax4.set_xlabel('Temperature [deg C]\nSensor D')
    # ax5.bar(bins5[:-1], t5, width=0.54,edgecolor='c')
    ax5.set_ylabel('Probability')
    ax5.set_xlabel('Temperature [deg C]\nSensor E')
    fig.suptitle('Pmfs forTemperature values of 5 sensors', )
    plt.tight_layout()
    plt.show()


def plotPdf(T1,T2,T3,T4,T5):
    plt.figure(figsize=(14, 5))
    ax1 = plt.subplot(111)
    ax1 = plt.subplot(231)
    ax2 = plt.subplot(232)
    ax3 = plt.subplot(233)
    ax4 = plt.subplot(234)
    ax5 = plt.subplot(235)
    sns.kdeplot(T1, color='b', ax=ax1, label='pdf')
    sns.kdeplot(T2, color='b', ax=ax2, label='pdf')
    sns.kdeplot(T3, color='b', ax=ax3, label='pdf')
    sns.kdeplot(T4, color='b', ax=ax4, label='pdf')
    sns.kdeplot(T5, color='b', ax=ax5, label='pdf')
    #ax1.hist(T1, bins=50, density=1, histtype='step', label='pdf')
    ax1.set_ylabel('Density')
    ax1.set_xlabel('Temperature [deg C]\nSensor A')
    #ax2.hist(T2, bins=50, density=1, histtype='step', label='pdf')
    ax2.set_ylabel('Density')
    ax2.set_xlabel('Temperature [deg C]\nSensor B')
    #ax3.hist(T3, bins=50, density=1, histtype='step', label='pdf')
    ax3.set_ylabel('Density')
    ax3.set_xlabel('Temperature [deg C]\nSensor C')
    #ax4.hist(T4, bins=50, density=1, histtype='step', label='pdf')
    ax4.set_ylabel('Density')
    ax4.set_xlabel('Temperature [deg C]\nSensor D')
    #ax5.hist(T5, bins=50, density=True, histtype='step', label='pdf')
    ax5.set_ylabel('Density')
    ax5.set_xlabel('Temperature [deg C]\nSensor E')
    plt.suptitle('Pdfs for Temperature values of 5 sensors ')
    plt.ylim(ymin=0)
    plt.tight_layout()
    plt.show()


def plotCdf(T1,T2,T3,T4,T5,A):
    fig = plt.figure(figsize=(14,8))
    ax1 = plt.subplot(231)
    ax2 = plt.subplot(232)
    ax3 = plt.subplot(233)
    ax4 = plt.subplot(234)
    ax5 = plt.subplot(235)
    '''a1 = ax1.hist(x=T1, bins=50, cumulative=1, density=1, color='w', alpha=0.7, rwidth=0.85 )#
    a2 = ax2.hist(x=T2, bins=50, cumulative=1, density=1, color='b', alpha=0.7, rwidth=0.85 )
    a3 = ax3.hist(x=T3, bins=50, cumulative=1, density=1, color='b', alpha=0.7, rwidth=0.85)
    a4 = ax4.hist(x=T4, bins=50, cumulative=1, density=1, color='b', alpha=0.7, rwidth=0.85)
    a5 = ax5.hist(x=T5, bins=50, cumulative=1, density=1, color='b', alpha=0.7, rwidth=0.85)
    ax1.plot(a1[1][1:] - (a1[1][1:] - a1[1][:-1]) / 2, a1[0], label='sensor1')
    ax2.plot(a2[1][1:] - (a2[1][1:] - a2[1][:-1]) / 2, a2[0], label='sensor2')
    ax3.plot(a3[1][1:] - (a3[1][1:] - a3[1][:-1]) / 2, a3[0], label='sensor3')
    ax4.plot(a4[1][1:] - (a4[1][1:] - a4[1][:-1]) / 2, a4[0], label='sensor4')
    ax5.plot(a5[1][1:] - (a5[1][1:] - a5[1][:-1]) / 2, a5[0], label='sensor5')'''
    sns.kdeplot(T1, cumulative=True, label='sensor A',ax=ax1,common_grid=True)
    sns.kdeplot(T2, cumulative=True, label='sensor B',ax=ax2)
    sns.kdeplot(T3, cumulative=True, label='sensor C',ax=ax3)
    sns.kdeplot(T4, cumulative=True, label='sensor D',ax=ax4)
    sns.kdeplot(T5, cumulative=True, label='sensor E',ax=ax5)
    if A=='T':
        X = 'Temperature'
        xlabel = 'Temperature [deg C]'
        ax1.set_xlim([5, 36])
        ax2.set_xlim([5, 36])
        ax3.set_xlim([5, 36])
        ax4.set_xlim([5, 36])
        ax5.set_xlim([5, 36])
    elif A == 'WS':
        X = 'Wind Speed'
        xlabel='Wind Speed [m/s]'
        ax1.set_xlim([-1, 8])
        ax2.set_xlim([-1, 8])
        ax3.set_xlim([-1, 8])
        ax4.set_xlim([-1, 8])
        ax5.set_xlim([-1, 8])
    ax1.set_xlabel(xlabel+"\nSensor A")
    ax1.set_ylabel('CDF')
    ax2.set_xlabel(xlabel+"\nSensor B")
    ax2.set_ylabel('CDF')
    ax3.set_xlabel(xlabel+"\nSensor C")
    ax3.set_ylabel('CDF')
    ax4.set_xlabel(xlabel+"\nSensor D")
    ax4.set_ylabel('CDF')
    ax5.set_xlabel(xlabel+"\nSensor E")
    ax5.set_ylabel('CDF')
    plt.suptitle('Cdfs for '+X+' values of 5 sensors')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()


def plotWS(T1,T2,T3,T4,T5):
    plt.figure(figsize=(14, 5))
    ax1 = plt.subplot(231)
    ax2 = plt.subplot(232)
    ax3 = plt.subplot(233)
    ax4 = plt.subplot(234)
    ax5 = plt.subplot(235)
    ax1.hist(T1, bins=25, density=1, histtype='step' ,label='pdf')
    ax2.hist(T2, bins=25, density=1, histtype='step',label='pdf')
    ax3.hist(T3, bins=25, density=1, histtype='step',label='pdf')
    ax4.hist(T4, bins=25, density=1, histtype='step',label='pdf')
    ax5.hist(T5,bins=25,density=True,histtype='step',label='pdf')
    sns.kdeplot(T1, color='r', ax=ax1,label='KDE')
    sns.kdeplot(T2, color='r', ax=ax2,label='KDE')
    sns.kdeplot(T3, color='r', ax=ax3,label='KDE')
    sns.kdeplot(T4, color='r', ax=ax4,label='KDE')
    sns.kdeplot(T5, color='r', ax=ax5,label='KDE')
    ax1.set_ylabel('Density')
    ax1.set_xlabel('Wind Speed [m/s]\nSensor A')
    # ax2.hist(T2, bins=50, density=1, histtype='step', label='pdf')
    ax2.set_ylabel('Density')
    ax2.set_xlabel('Wind Speed [m/s]\nSensor B')
    # ax3.hist(T3, bins=50, density=1, histtype='step', label='pdf')
    ax3.set_ylabel('Density')
    ax3.set_xlabel('Wind Speed [m/s]\nSensor C')
    # ax4.hist(T4, bins=50, density=1, histtype='step', label='pdf')
    ax4.set_ylabel('Density')
    ax4.set_xlabel('Wind Speed [m/s]\nSensor D')
    # ax5.hist(T5, bins=50, density=True, histtype='step', label='pdf')
    ax5.set_ylabel('Density')
    ax5.set_xlabel('Wind Speed [m/s]\nSensor E')
    plt.suptitle('Pdfs for Temperature values of 5 sensors ')
    plt.legend(loc=1)
    plt.suptitle(' Pdfs and the kernel density estimation for 5 sensors wind speed values', )
    plt.ylim(ymin=0)
    plt.tight_layout()
    plt.show()