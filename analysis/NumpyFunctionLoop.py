import numpy as np

#create array of weekly vaccination numbers from https://opendata-geohive.hub.arcgis.com/datasets/0101ed10351e42968535bb002f94c8c6_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D

a= np.array([3946,
43856,
52659,
49703,
51381,
56267,
32176,
86434,
88578,
88294,
91298,
64535,
133195,
139946,
131038,
155716,
188626,
211497,
245947,
323166,
331292,
305479,
277195,
290362,
357077,
370059,
370544,
390891,
373319,
336086,
300378,
232066,
232234,
229694,
183158,
121650,
108327,
95192,
63718,
43289,
23643,
21081,
24567,
22115,
18434,
15138,
21262,
21259,
19713,
14174,
14862,
])

#print(a.shape)

#print(np.mean(a))

#print(np.median(a))

#print(np.max(a))

#Generate min and % of adult population vaccinated per week

def uptake(value):
    WkTotal = np.min(value)
    WkTotalStr = "% s" % WkTotal
    Str1="Minimum Uptake "
    print(Str1 + WkTotalStr)
    Str2="% of Population Vaccinated per Week"
    print(Str2)
    for i in a:
        print(i / 4000000 * 100)

uptake(a)


