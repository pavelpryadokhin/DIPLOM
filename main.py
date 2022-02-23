#J=x^2(T)+k∫u^2(t)dt, где 0<=x<=1.5 и -1<u<=1
import numpy as np
k=2
a=0
N=2
x=np.array([0,0.5,1.0,1.5])
u={-1,-0.5,0,0.5,1}
x_cost=x**2
result=dict()
while N!=0:
    u_effort=np.zeros((len(x),len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            cost=x[j]-x[i]
            if cost in u:
                u_effort[i][j]=(cost**2)*k #вычисление прироста стоимости
                u_effort[i][j]+=x_cost[j]#затраты в момент времени N-1
            else:
                u_effort[i][j]=None
    best_action=dict()
    for i in range(len(x)):
        min_value=(np.nanmin(u_effort[i]))#mинимальные затраты
        ind,= np.where(np.isclose(u_effort[i], min_value))#поиск на каком индекса
        best_action[x[i]]=float(x[ind])
    result[N]=best_action
    N-=1
print(result)