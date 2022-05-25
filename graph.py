import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # графики

day=[i for i in range(31)]
day.extend([i for i in range(31)])
day.extend([i for i in range(31)])
q1=[189300.0, 107800.0, 107700.0, 80100.0, 94500.0, 78500.0, 72900.0, 53200.0, 65850.0, 64600.0, 76500.0, 64100.0, 79400.0, 22500.0, 44400.0, 24400.0, 37400.0, 31200.0, 33400.0, 37200.0, 35600.0, 13600.0, 14900.0, 13400.0, 11500.0, 23700.0, 10500.0, 18300.0, 0, 11500.0, 11700.0]

#доверительная погрешность 20%
q11=list(map(lambda x:x*1.2,q1))
q12=list(map(lambda x:x*0.8,q1))
q1.extend(q12)
q1.extend(q11)


q2=[240700.0, 110600.0, 114200.0, 78400.0, 83550.0, 72250.0, 53250.0, 48750.0, 42600.0, 50950.0, 58000.0, 58500.0, 63850.0, 24600.0, 41050.0, 25850.0, 43150.0, 38650.0, 39800.0, 38550.0, 44700.0, 36200.0, 26250.0, 49850.0, 22550.0, 32050.0, 32200.0, 32950.0, 18850.0, 27300.0, 29150.0]

#доверительная погрешность 20%
q21=list(map(lambda x:x*1.2,q2))
q22=list(map(lambda x:x*0.8,q2))
q2.extend(q22)
q2.extend(q21)

df=pd.DataFrame()
plt.figure(figsize=(7.5, 5))
plt.title('Средняя выручка в день', fontsize=15)
plt.xlabel('Глубина бронирования', fontsize=15)
plt.ylabel('Выручка', fontsize=15)
df['cost']=q1
df['day']=day
sns.lineplot(data=df, x="day", y="cost", lw=3, label='Исходная стратегия')
df['cost']=q2
df['day']=day
sns.lineplot(data=df, x="day", y="cost", lw=3, label='Разработанная стратегия')

plt.show()