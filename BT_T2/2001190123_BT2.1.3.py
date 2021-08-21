import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data= pd.read_csv('../credit_card.clean_2.csv')
print(data)

#Tạo một cột trống mới dùng để chứa nhãn với tên là EDUCATION_CAT
data['EDUCATION_CAT']='none'

#Xem xét 10 dòng đầu tiên của 2 thuộc tính EDUCATION và EDUCATION_CAT.
print(data['EDUCATION_CAT'].head(10))
print(data['EDUCATION'].head(10))

#Tạo một dictionary để mô tả và map các giá trị của thuộc tính EDUCATION
cat_mapping = {
1: "graduate school",
2: "university",
3: "high school",
4: "others"
}

#Sử dụng phương thức map để gán cho cột
data['EDUCATION_CAT'] = data['EDUCATION'].map(cat_mapping)
print(data[['EDUCATION', 'EDUCATION_CAT']].head(10))

#Xem xét và nhận xét kết quả.
print('các giá trị đã được chuyển đổi')

#Tạo dummy code
edu_ohe = pd.get_dummies(data['EDUCATION_CAT'])
print(edu_ohe.head(10))

#Gắn kết 2 dataframe lại với nhau để thành 1 dataframe mới đầy đủ
data2 = pd.concat([data, edu_ohe], axis=1)
data2[['EDUCATION_CAT', 'graduate school', 'high school', 'university','others']].head(10)

#Xuất thành file credit_card_clean_3.csv.
data2.to_csv('../credit_card.clean_3.csv',index=False)