import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data= pd.read_csv('../credit_card.clean_2.csv')
print(data)


print(data['LIMIT_BAL'])

# print(data['LIMIT_BAL'].hist())

#data2=pd.DataFrame(data[1],data[5])
# plt.bar(data['LIMIT_BAL'],data['AGE'],color='b')
# plt.show()

df = pd.DataFrame({
    'LIMIT_BAL': data['LIMIT_BAL'],
    'AGE': data['AGE']
    })
hist = df.hist(color='g')
# plt.show()
print('trung bình tuổi: 35.5 - limit_bal: 167919.05')
print('độ lệch: tuổi: 9.22 - limit_bal: 129839.45')

print(df.describe())

print()
print('EDUCATION: ')
print(data['EDUCATION'].value_counts())
print('nhận xét: 0 ko có trong codebook')
print()

x=data['EDUCATION'].replace([0,5,6],[4,4,4],inplace=True)
print(data['EDUCATION'].value_counts())


plt.show()