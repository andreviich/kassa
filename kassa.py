import numpy as np
import math

N = [200, 350, 450] #количество посетителей утром, днем и вечером
prom = [10, 10, 10] #анализируемый временной промежуток

intense = []
for n in range(len(prom)):
   intense.append(N[n]/prom[n])
print('Интенсивность входного потока: ', intense)

t = np.array([1.5, 1.5, 1.5]) #время обслуживания одного клиента
intense1 = 1/t
print ('Интенсивность выходного потока: ', intense1)

ro = [] #показатель нагруженности
for i in range(len(intense1)):
   ro.append(intense[i]/intense1[i])
print('Показатель нагруженности: ', ro)

n = 10 #количество касс
m = 10 #количество человек

vsp = []
for l in range(0,5):
   vsp.append(ro[0]**l/math.factorial(l))

vs_p = []
for l in range (5, 15):
   vs_p.append(ro[0]**l/(n**(l-n)*math.factorial(n)))

vspomog = vsp + vs_p
print('Вспомогательный массив утра: ', vspomog)



vsp1 = []
for l in range(0,5):
   vsp1.append(ro[1]**l/math.factorial(l))

vs_p1 = []
for l in range (5, 15):
   vs_p1.append(ro[1]**l/(n**(l-n)*math.factorial(n)))

vspomog1 = vsp1 + vs_p1
print('Вспомогательный массив дня: ', vspomog1)


vsp2 = []
for l in range(0,5):
   vsp2.append(ro[2]**l/math.factorial(l))

vs_p2 = []
for l in range (5, 15):
   vs_p2.append(ro[2]**l/(n**(l-n)*math.factorial(n)))

ver = []
v = (sum(vspomog)**-1)*100
ver.append(v)
for y in range (1, len(vspomog)):
    ver.append(vspomog[y]*v)
print('Вероятности по состоянию на утро: ', ver)
vspomog2 = vsp2 + vs_p2
print('Вспомогательный массив вечера: ', vspomog2)

ver1 = []
v1 = (sum(vspomog1)**-1)*100
ver1.append(v1)
for y1 in range (1, len(vspomog)):
    ver1.append(vspomog1[y1]*v1)
print('Вероятности по состоянию на день: ', ver1)

ver2 = []
v2 = (sum(vspomog2)**-1)*100
ver2.append(v2)
for y2 in range (1, len(vspomog2)):
    ver2.append(vspomog2[y2]*v2)
print('Вероятности по состоянию на вечер: ', ver2)

print ('Состояние системы утром')
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
ax.bar(langs, ver)
plt.show()

print ('Состояние системы днем')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
ax.bar(langs, ver1)
plt.show()

print ('Состояние системы вечером')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
ax.bar(langs, ver2)
plt.show()




print ('Вероятность отказа в обслуживании утром: ', ver[14])
print ('Вероятность отказа в обслуживании днем: ', ver1[14])
print ('Вероятность отказа в обслуживании вечером: ', ver2[14])


print ('Вероятность встать в очередь утром: ', sum(ver[5:14]))
print ('Вероятность встать в очередь днем: ', sum(ver1[5:14]))
print ('Вероятность встать в очередь вечером: ', sum(ver2[5:14]))


print('Абсолютная пропускная способность утром: ', intense[0]*(1-ver[14]))
print('Абсолютная пропускная способность днем: ', intense[1]*(1-ver1[14]/100))
print('Абсолютная пропускная способность вечером: ', intense[2]*(1-ver2[14]))


print('Относительная пропускная способность утром: ', 1-ver[14])
print('Относительная пропускная способность днем: ', 1-ver1[14])
print('Относительная пропускная способность вечером: ', 1-ver2[14])

print('Среднее колчество занятых касс утром: ', intense[0]*(1-ver[14])/intense1[0])
print('Среднее количество занятых касс днем: ', intense[1]*(1-ver1[14]/100)/intense1[1])
print('Среднее количество занятых касс вечером: ', intense[2]*(1-ver2[14])/intense1[2])

print('Коэффициент простоя утром: ', (1-(intense[0]*(1-ver[14])/intense1[0])/n)*100)
print('Коэффициент простоя днем: ', (1-(intense[1]*(1-ver1[14]/100)/intense1[1])/n)*100)
print('Коэффициент простоя вечером: ', (1-(intense[2]*(1-ver2[14])/intense1[2])/n)*100)
