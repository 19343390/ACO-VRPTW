import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import math


dtb='Output/aco_dtb.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()


#vehcount count
c.execute('select count(distinct vehCount) from solutions')
vehCountCt=c.fetchall()[0][0]

#vehcount count
c.execute('select distinct vehCount from solutions')
vehCtList0=c.fetchall()
vehCtList=[]
for vc in vehCtList0:
    vehCtList.append(vc[0])

n_groups=vehCountCt
fig, ax = plt.subplots()
index = np.arange(n_groups)

bar_width = 0.3
opacity = 0.8

colorList=[ 'g','b','r','y','o','w']
g0=[]
for vehctT in vehCtList:

    c.execute('select count(idVar) from Solutions where  vehCount= '+str(vehctT)+' group by vehCount order by vehCount')
    recs=c.fetchall()
    if not recs:
        g0.append(0)
    else:
        g0.append(recs[0][0])


rects0 = plt.bar(index, g0, bar_width,
                 alpha=opacity,
                 color='b')

plt.xlabel('Vehicle Counts')
plt.ylabel('Run Counts')
plt.title('Run Counts of Vehicle Counts')
plt.xticks(index+bar_width, ('20', '21', '22', '23'))
plt.legend()
 
plt.tight_layout()
plt.show()
