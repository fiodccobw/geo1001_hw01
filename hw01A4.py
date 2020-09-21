#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def find_close(arr, e):

    size = len(arr)
    idx = 0
    val = abs(e - arr[idx])

    for i in range(1, size):
        val1 = abs(e - arr[i])
        if val1 < val:
            idx = i
            val = val1
    return idx



def calcCI(A1,A2,A3,A4,A5,B):
    A = [A1,A2,A3,A4,A5]
    sensor_list = ['A','B','C','D','E']
    lower_list = []
    upper_list = []

    fig = plt.figure(figsize=(14, 8))
    ax1 = plt.subplot(231)
    ax2 = plt.subplot(232)
    ax3 = plt.subplot(233)
    ax4 = plt.subplot(234)
    ax5 = plt.subplot(235)
    axes = [ax1,ax2,ax3,ax4,ax5]
    a1 = ax1.hist(x=A1, bins=50, cumulative=1, density=1,alpha=0.5, rwidth=0.85,color='w')  # histtype='barstacked'
    a2 = ax2.hist(x=A2, bins=50, cumulative=1, density=1, color='w', alpha=0.5, rwidth=0.85)
    a3 = ax3.hist(x=A3, bins=50, cumulative=1, density=1, color='w', alpha=0.5, rwidth=0.85)
    a4 = ax4.hist(x=A4, bins=50, cumulative=1, density=1, color='w', alpha=0.5, rwidth=0.85)
    a5 = ax5.hist(x=A5, bins=50, cumulative=1, density=1, color='w', alpha=0.5, rwidth=0.85)
    a = [a1,a2,a3,a4,a5]

    for i in range(5):
        '''mu, sigma = np.mean(A[i]), np.std(A[i])
        size = len(A[i])
        lower, upper = scipy.stats.t.interval(0.95, size - 1, mu, sigma)'''
        l = find_close(a[i][0],0.05)
        u = find_close(a[i][0],0.95)
        lower_list.append(a[i][1][l])
        upper_list.append(a[i][1][u])

    intervals_list = pd.DataFrame([sensor_list,lower_list,upper_list]).transpose()
    intervals_list.columns = ['Sensor','Lower boundary','Upper boundary']

    for i in range(5):
        axes[i].plot([lower_list[i],lower_list[i]],[0, 1.05], 'k-', lw=2, color='r')
        axes[i].plot([upper_list[i],upper_list[i]],[0, 1.05], 'k-', lw=2, color='r')

    ax1.plot(a1[1][1:] - (a1[1][1:] - a1[1][:-1]) / 2, a1[0])
    ax2.plot(a2[1][1:] - (a2[1][1:] - a2[1][:-1]) / 2, a2[0])
    ax3.plot(a3[1][1:] - (a3[1][1:] - a3[1][:-1]) / 2, a3[0])
    ax4.plot(a4[1][1:] - (a4[1][1:] - a4[1][:-1]) / 2, a4[0])
    ax5.plot(a5[1][1:] - (a5[1][1:] - a5[1][:-1]) / 2, a5[0])

    for i in range(5):
        axes[i].set_ylim(ymax=1.05)

    if B=='T':
        X = 'Temperature'
        xlabel = 'Temperature [deg]'
        ax1.set_xlim([5, 36])
        ax2.set_xlim([5, 36])
        ax3.set_xlim([5, 36])
        ax4.set_xlim([5, 36])
        ax5.set_xlim([5, 36])
    elif B == 'WS':
        X = 'Wind Speed'
        xlabel='Wind Speed [m/s]'
        ax1.set_xlim([-1, 8])
        ax2.set_xlim([-1, 8])
        ax3.set_xlim([-1, 8])
        ax4.set_xlim([-1, 8])
        ax5.set_xlim([-1, 8])
    ax1.set_xlabel(xlabel + "\nSensor A")
    ax1.set_ylabel('CDF')
    ax2.set_xlabel(xlabel + "\nSensor B")
    ax2.set_ylabel('CDF')
    ax3.set_xlabel(xlabel + "\nSensor C")
    ax3.set_ylabel('CDF')
    ax4.set_xlabel(xlabel + "\nSensor D")
    ax4.set_ylabel('CDF')
    ax5.set_xlabel(xlabel + "\nSensor E")
    ax5.set_ylabel('CDF')

    intervals_list.to_csv(X+'0.95CI.csv',encoding='gbk')
    plt.suptitle('Cdfs and 95% confidence interval for ' + X + ' values of 5 sensors')
    plt.tight_layout()
    plt.show()

from scipy import stats


def hypothesisTest(T1,T2,T3,T4,T5,C):
    a = ['A','B','C','D','E']
    b = [T1,T2,T3,T4,T5]
    t = [0,0,0,0]
    p =[0,0,0,0]
    for i in range(4):
        for j in range(1,5):
            t[i],p[i] = stats.ttest_ind(b[i],b[j])
            t[i] = abs(t[i])
        print('For sensor '+a[i]+' and sensor '+a[i+1]+':')
        if C == 'T':
            print('t(Temperature) =',t[i])
            print('p-value(Temperature) =',p[i])
        elif C =='WS':
            print('t(Wind speed) =', t[i])
            print('p-value(Wind speed) =', p[i])
