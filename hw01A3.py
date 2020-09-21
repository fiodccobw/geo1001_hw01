#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513


import numpy as np																	#
import matplotlib.pyplot as plt														#
from scipy import stats
import seaborn as sns


def calcCorrealation(a,b):
    # Step 1 --- remove nan numbers
    a1 = np.array(a)
    b1 = np.array(b)
    a2 = a1[~np.isnan(a1)]
    b2 = b1[~np.isnan(b1)]

    # Step 2 --- interpolate to equal size samples
    a3 = np.interp(np.linspace(0,len(b2),len(b2)),np.linspace(0,len(a2),len(a2)),a2)

    # Step 3 --- normalize because variables have different units
    a_normalized = (a3 - a3.mean())/a3.std()
    b_normalized = (b2 - b2.mean())/b2.std()

    # Step 4 --- compute statistics
    pcoef,pvps = stats.pearsonr(a_normalized,b_normalized)
    prcoef,pvsp = stats.spearmanr(a_normalized,b_normalized)
    if a == b:
        pcoef = 1
    return pcoef,prcoef,pvps,pvsp


def showCorrelation(T1,T2,T3,T4,T5,A):
    sns.set_style('darkgrid')
    a = np.zeros((5,5))
    b = np.zeros((5,5))
    c = np.zeros((5,5))
    d = np.zeros((5,5))
    D = [T1,T2,T3,T4,T5]
    for i in range(5):
        for j in range(5):
            a[i][j],b[i][j],c[i][j] ,d[i][j] = calcCorrealation(D[i],D[j])
    if A == 'T':
        B = 'Temperature'
    elif A == 'WBGT':
        B = 'Wet Bulb Globe'
    elif A == 'CS':
        B = 'Crosswind speed'
    print("Pearson's coefficients for",B)
    print(a)
    print("Spearmann's coefficients for",B)
    print(b)
    name_list = ['A','B','C','D','E']
    num_list1,num2_list1 = a[0][:],b[0][:]
    num_list2,num2_list2 = a[1][:],b[1][:]
    num_list3,num2_list3 = a[2][:],b[2][:]
    num_list4,num2_list4 = a[3][:],b[3][:]
    num_list5,num2_list5 = a[4][:],b[4][:]
    num1 = [num_list1,num2_list1]
    num2 = [num_list2,num2_list2]
    num3 = [num_list3,num2_list3]
    num4 = [num_list4,num2_list4]
    num5 = [num_list5,num2_list5]
    plt.figure(figsize=(16,5))
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    axes = [ax1,ax2]
    k =["Pearson's","Spearman's"]
    for i in range(2):
        axes[i].plot(name_list, num1[i], 'ro', color = 'g', label = 'Sensor A')
        axes[i].plot(name_list, num2[i], 'ro', color = 'b', label = 'Sensor B')
        axes[i].plot(name_list, num3[i], 'ro', color = 'r', label = 'Sensor C')
        axes[i].plot(name_list, num4[i], 'ro', color = 'k', label = 'Sensor D')
        axes[i].plot(name_list, num5[i], 'ro', color = 'y', label = 'Sensor E')
        axes[i].set_xlabel(k[i]+" correlation coefficient between sensors for "+B)
    plt.legend(loc='right')
    plt.tight_layout()
    plt.show()


def plotScatter(T1,T2,T3,T4,T5,A):
    fig = plt.figure(figsize=(14,5))
    ax1 = plt.subplot(251)
    ax2 = plt.subplot(252)
    ax3 = plt.subplot(253)
    ax4 = plt.subplot(254)
    ax5 = plt.subplot(255)
    ax6 = plt.subplot(256)
    ax7 = plt.subplot(257)
    ax8 = plt.subplot(258)
    ax9 = plt.subplot(259)
    ax10 = plt.subplot(2,5,10)
    D = [T1, T2, T3, T4, T5]
    axes = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]
    X = ['A','B','C','D','E']
    a = 0
    if A == 'T':
        B = 'Temperature'
    elif A == 'WBGT':
        B = 'Wet Bulb Globe'
    elif A == 'CS':
        B = 'Crosswind speed'
    fig.suptitle('Scatter plots of '+B+' values between sensors')
    for i in range(5):
        for j in range(i+1,5):
            dat = pScatter(D[i],D[j])
            axes[a].scatter(dat,D[j],c='b',s = 1.3)
            axes[a].set_xlabel(B+"(sensor "+X[i]+")")
            axes[a].set_ylabel(B + "(sensor " + X[j] + ")")
            a = a+1
    plt.tight_layout()
    plt.show()


def pScatter(a,b):
    # Step 1 --- remove nan numbers
    a = np.array(a)
    b = np.array(b)
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]

    # Step 2 --- interpolate to equal size samples
    a1 = np.interp(np.linspace(0,len(b),len(b)),np.linspace(0,len(a),len(a)),a)
    return  a1