import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#load credit_card_clean_1.csv.csv
data = pd.read_csv('../credit_card_clean_1.csv')
print(data)

#xem thông tin các cột = phương thức .info()
print(data.info())

#xem thông tin 10 cột đầu PAY_1
print(data['PAY_1'].value_counts(dropna=False))


#giá trị trống PAY_1

#làm sạch dữ liệu 0 của PAY_1
valid_pay = ~(data['PAY_1'].isnull())

print(valid_pay.value_counts())

#xóa dữ liệu:
data_clean_2= data.loc[valid_pay, :].copy()

data_clean_2.to_csv('../credit_card.clean_2.csv',index=False)