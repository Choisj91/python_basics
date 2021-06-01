# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함 | EXCEL데이터를 다룰 때 pandas사용!

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자(가지고오지않는행)
xlsx = pd.read_excel('./resource/sample.xlsx') # sheetname='시트명' 또는 숫자, header=3, skiprow=1 실습

# 상위 데이터 확인 : 처음부터 5개의 값만 보여줌
print(xlsx.head())
# print()

# 데이터 확인 : 꼬리 데이터 확인 끝의 5개 값만 확인
print(xlsx.tail())
# print()

# 데이터 구조
# print(xlsx.shape) # 행, 열


# # 엑셀 or CSV 다시 쓰기 : Index는 숫자를 붙여주는 것
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)