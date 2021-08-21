import numpy as np
import pandas as pd

data=pd.read_csv('..\credit_card.csv')
print(data)
data['PAY_1'] = pd.to_numeric(data['PAY_1'], errors='coerce')

# 2. kiểm tra số dòng và cột
print('số dòng: ',len(data))
print('số cột: ',len(data.columns))

#data.to_csv('redit_card.csv',index=False)

# 3. kiểm tra các cột
print(data.columns)

# 4. 5 dòng đầu
print(data.head(5))

# 5. uni
#print(np.unique(x))
z=data['ID'].unique()

print('đếm số lượng giá trị duy nhất: ',len(z))

# 6. value_count: xem giá trị nào xuất hiện hơn 1 lần
id_counts=data['ID'].value_counts()
print('trả về 1 chuỗi chứa các giá trị duy nhất')
print(id_counts.head())
print(len(id_counts.head()))
print('Nhận xét: đếm những value nào bị lặp lại ')

# BT2
# 7. đánh dấu những id trùng đó;
dupe_mask=(id_counts==2)
print (dupe_mask[0:5])

# 8. chọn lọc và chứa các id thành 1 nhóm:
dupe_ids=list(id_counts.index[dupe_mask])
print(len(id_counts.index))
print('nhận xét: đếm những giá trị không bị trùng')

# 9. kiểm tra số phần tử
print('kiểm tra phần tử: ',len(dupe_ids))
print('nhận xét: gom các phần tử giống nhau vào 1 danh sách')

print(data.loc[data['ID'].isin(dupe_ids[0:3]),:].head(10))

# BT3
df_zero_mask=data==0 #
feature_zero_mask = df_zero_mask.iloc[:,1:].all(axis=1)
df_clean_1 = data.loc[~feature_zero_mask,:].copy()

print('số hàng: ',len(df_clean_1))
print('số cột: ', len(df_clean_1.columns))
xx=df_clean_1['ID'].unique
print('giá trị ko lặp:',xx)

print('dữ liệu 1: ',len(data))
print('dữ liệu xóa 0: ',len(df_clean_1))

print(df_zero_mask.value_counts().head(10))

#df_clean_1.to_csv('../credit_card_clean_1.csv',index=False)