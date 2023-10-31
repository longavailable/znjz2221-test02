'''
Python 3
1、利用Pandas读写Excel
2、表格对比
'''

from pathlib import Path
import pandas as pd

# 输入文件路径、网址变量
file = Path('data/002-test-data.xlsx')
file = 'https://github.com/longavailable/znjz2221-test02/raw/main/data/002-test-data.xlsx'

# 利用Pandas读取Excel
sheet1 = pd.read_excel(file, sheet_name=0)
sheet2 = pd.read_excel(file, sheet_name=1)

# 检查读取是否正确
#print(sheet1)
#print(sheet2)

# 数据分析
# 在表1不在表2的部分
sheet3 = sheet1[~(sheet1['序号'].isin(sheet2['序号']))].reset_index(drop=True)
print(sheet3)


# 思考？
# 在表2不在表1的部分
# 表1和表2的公共部分
# 表1和表2的不重合部分

'''
# 输出
#sheet3.to_excel(file.parent / '022-result.xlsx', index=False)
#sheet3.to_excel('022-result.xlsx', index=False)
with pd.ExcelWriter(file, mode='a') as writer:
	sheet3.to_excel(writer, sheet_name='Sheet3', index=False)
'''

print('Done')

