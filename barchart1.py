import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import math


dtb='Output/aco_dtb.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

varvar='alpha'

#vehcount count
c.execute('select count(distinct vehCount) from solutions')
vehCountCt=c.fetchall()[0][0]

#vehcount count
c.execute('select distinct vehCount from solutions')
vehCtList0=c.fetchall()
vehCtList=[]
for vc in vehCtList0:
    vehCtList.append(vc[0])

#varvar count
c.execute('select count(distinct '+varvar+') from solutions')
varvarCt=c.fetchall()[0][0]

#distint varvars
c.execute('select distinct '+varvar+' from solutions')
varvarlist0=c.fetchall()
varvarlist=[]
for vv in varvarlist0:
    varvarlist.append(vv[0])

print('vehcountct',vehCountCt)
print('varvarCt',varvarCt)
print('vavarlist',varvarlist)
print('vehCountlist',vehCtList)

#c.execute('select '+varvar+', vehCount, count(idVar) as runCount from Solutions group by '+varvar+',vehCount order by '+varvar+',vehCount')
#recs=c.fetchall()
#for rec in recs:
#    print(rec)


#g1=[1,3,4,2]
#g2=[1,2,6,1]
#g3=[3,5,5,3]
#g4=[3,5,5,3]

# create plot
n_groups=vehCountCt
fig, ax = plt.subplots()
index = np.arange(n_groups)

print('vavarlistlen',len(varvarlist))
bar_width = 0.7/len(varvarlist)
opacity = 0.8
print('index is',index)

colorList=[ 'g','b','r','y','o','w']
barP=0
for varvarT in varvarlist:
    g0=[]
    for vehctT in vehCtList:
        c.execute('select count(idVar) from Solutions where '+varvar+' = '+str(varvarT)+ ' and vehCount= '+str(vehctT)+' group by vehCount order by vehCount')
        recs=c.fetchall()
        if not recs:
            g0.append(0)
        else:
            g0.append(recs[0][0])

    barD=1
    if barP%2==0:
        barD=(-1)
    barP1=math.ceil(barP/2)
    print('********************')
    print('alpha',varvarT)
    print('g0',g0)
    print('index',index)
    print('position',barD*barP1*bar_width)
    print('********************')

    rects0 = plt.bar(index+barD*barP1*bar_width, g0, bar_width,
                 alpha=opacity,
                 color=colorList[barP],
                 label=varvar+' '+str(varvarT))
    barP+=1
#rects2 = plt.bar(index - bar_width, g2, bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='alpha 0.2')

#rects3 = plt.bar(index+bar_width, g3, bar_width,
#                 alpha=opacity,
#                 color='r',
#                 label='alpha 0.3')
 


plt.xlabel('Vehicle Counts')
plt.ylabel('Run Counts')
plt.title('Run Counts of Vehicle Counts')
plt.xticks(index+bar_width, ('20', '21', '22', '23'))
plt.legend()
 
plt.tight_layout()
plt.show()



conn.close()
