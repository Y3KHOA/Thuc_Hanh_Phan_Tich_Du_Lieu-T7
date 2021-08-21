import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

data= pd.read_csv('credit_card_clean_3.csv')
print(data)

x=data['LIMIT_BAL'].describe()
print(x)
print('số tiền trung bình: 167919.05')
print('độ lệch: 129839.45')

#tính sao kê
df=pd.DataFrame({'LIMIT_BAL': data['LIMIT_BAL']})
hist=df.hist(bins=20)



bill_feats = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']

pay_amt_feats = ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

x=data[pay_amt_feats].describe()
print(x)
print(x.value_counts())

#tính số tiền đã trả
#vẽ biểu đồ vs 3 dòng, 2 cột
df2=pd.DataFrame({  'bill 1': data['BILL_AMT1'],
                    'bill 2': data['BILL_AMT2'],
                    'bill 3': data['BILL_AMT3'],
                    'bill 4': data['BILL_AMT4'],
                    'bill 5': data['BILL_AMT5'],
                    'bill 6': data['BILL_AMT6']
                  })
h1=df2.hist(bins=30,figsize=(10,7))

pay_zero_mask = data[pay_amt_feats] == 0
print(pay_zero_mask.sum())
pay_zero_mask.sum()
data[pay_amt_feats][~pay_zero_mask].apply(np.log10).hist(layout=(2,3))

print()
print('giải thích:')
print('pay_zero_mask = data[pay_feats] == 0: gán các giá trị 0 vào cho pay_zero_mask')
print('pay_zero_mask.sum(): đếm lại các biên có giá trị =0')
print('data[pay_feats][~pay_zero_mask].apply(numpy.log10).hist(layout=(2,3),figsize=(20,20)): vẽ đồ thị cho pay_feats loại trừ những người không có số tiền trả, biểu đồ dạng Histogram.')
print('')
print('So Sánh:')
print('Biểu đồ em vẽ: được vẽ theo tỉ lệ 1:1')
print('Biểu đồ thầy vẽ: được vẽ theo tỉ lệ 1:Log10(số liệu thực)')

plt.show()