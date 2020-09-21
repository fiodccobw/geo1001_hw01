#-- GEO1001.2020--hw01
#-- Linjun Wang
#-- 5214513


import pandas as pd
import xlrd
import numpy

def readDate(n):
    workbook = xlrd.open_workbook(r'HEAT.xls')
    sheet = workbook.sheet_by_name('sheet' + str(n))
    dat = []
    for a in range(5, sheet.nrows):
        cells = sheet.row_values(a)
        dat.append(cells)
    D = []
    date = numpy.array(dat)
    for i in range(0,len(dat)):
        fields = date[i,:]
        D.append(float(fields[0]))
    return D


def calHC(T1,T2,T3,T4,T5):
    D1 = readDate(1)
    D2 = readDate(2)
    D3 = readDate(3)
    D4 = readDate(4)
    D5 = readDate(5)
    D = [D1,D2,D3,D4,D5]
    p = []
    for i in range (5):
        r = []
        for j in range(len(D[i])):
            real_time = pd.to_datetime('1899-12-30') + pd.Timedelta(str(D[i][j]) + 'D')
            t = str(real_time.month)+'-'+str(real_time.day)
            r.append(t)
        p.append(r)
    l1 = pd.DataFrame([p[0], T1]).transpose()
    l1.columns = ['date','temperature']
    l2 = pd.DataFrame([p[1], T2]).transpose()
    l2.columns = ['date', 'temperature']
    l3 = pd.DataFrame([p[2], T3]).transpose()
    l3.columns = ['date', 'temperature']
    l4 = pd.DataFrame([p[3], T4]).transpose()
    l4.columns = ['date', 'temperature']
    l5 = pd.DataFrame([p[4], T5]).transpose()
    l5.columns = ['date', 'temperature']
    grouped1 = pd.to_numeric(l1['temperature']).groupby(l1['date']).mean()
    grouped2 = pd.to_numeric(l2['temperature']).groupby(l2['date']).mean()
    grouped3 = pd.to_numeric(l3['temperature']).groupby(l3['date']).mean()
    grouped4 = pd.to_numeric(l4['temperature']).groupby(l4['date']).mean()
    grouped5 = pd.to_numeric(l5['temperature']).groupby(l5['date']).mean()
    g = [grouped1,grouped2,grouped3,grouped4,grouped5]
    k = grouped1
    for i in range(1,5):
        k = k.append(g[i])
    f = k.groupby('date').mean()
    print('Hottest day:'+f.idxmax())
    print('Coldest day:'+f.idxmin())