# import pandas as  pd
#
# df = pd.read_csv('netliix.csv')
# print(df)
# print(df.columns)
# print(df.head(20))
# print(df[a'].unique())
#
# # df1 = df['type'].value_counts()
# # print(df1)
# # #
# # # df1.to_excel('output.xlsx', sheet_name='sheet1', index=False)
# # # print("\nData  written to 'output,xlsx'.")
# #
# #
# # # #merging (used to combine dataframes)
# # #
# # # import pandas as pd
# # # # df1 = pd.DataFrame({
# # # #     'key':['A','B','C','D'],
# # # #     'value1':[1,2,3,4,]
# # # # })
# # # # df2 =pd.DataFrame({
# # # #     'key':['B','G','D','E'],
# # # #     'value2':[3,4,5,6]
# # # #  })
# # # # # # result = pd.merge(df1,df2,on='key', how ='inner')#intersection
# # # # # # print(result)
# # # # # #
# # # # # # result1 = pd.merge(df1,df2,on='key', how ='outer')#union
# # # # # # print(result1)
# # # # #
# # # # # result2 = pd.merge(df1,df2,on='key', how ='left')
# # # # # print(result2)
# # # # #
# # # # # result3 = pd.merge(df1,df2,on='key', how ='right')
# # # # # print(result3)
# # # #
# # # # #joining
# # # #
# # # #
# # # # df1= df1.set_index('key')
# # # # df2 = df2.set_index('key')
# # # #
# # # # #default is left join
# # # # result = df1.join(df2)
# # # # print(result)
# # # #
# # # # result0 = df2.join(df1)
# # # # print(result0)
# # # #
# # # # # #inner join
# # # # result1=df1.join(df2, how='inner')
# # # # print(result1)
# # # #
# # # # #outer join
# # # # result2 = df1.join(df2, how='outer')
# # # # print(result2)
# # # #
# # # # #concatenating
# # # #
# # # # df3 = pd.DataFrame({
# # # #     'key':['A','B','C','D'],
# # # #     'value1':[1,2,3,4]
# # # # })
# # # #
# # # # df4 = pd.DataFrame({
# # # #     'key':['E','F','G','H'],
# # # #     'value1':[5,6,7,8]
# # # # })
# # # # final=pd.concat([df3,df4],axis=1)
# # # # print(final)
# # #
# # # #appending in index
# # # df1=pd.DataFrame({
# # #
# # #
# # # 'A':[1,2,3],
# # # 'B':[4,5,6]
# # # })
# # # df2=pd.DataFrame({
# # #     'A':[7,8],
# # #     'B':[9,10]
# # # })
# # # final1 = pd.concat([df1,df2],ignore_index=False)#True(same index),False(index change)
# # # print(final1)
# # #
# # #
# # # final2 = pd.concat([df1,df2],ignore_index=True)#True(same index),False(index change)
# # # print(final2)
# #
import pandas as pd
# df = pd.DataFrame({
#   'a':['A','B','C','B','B','D'],
#     'b': [1, 2, 3, 4,7,8]
# })
#
# print(df.head(4))
# print(df['a'].unique())
import pandas as pd

#sample DATA
# data={
#     'A':[1,2,3,4,5,6]
# }
# df = pd.DataFrame(data)
# def square(x):
#     return x**2
# df['A_squared']= df['A'].apply(square)
# print(df)
#
# def add_one(x):
#     return x+1
# df = df.applymap(add_one)
# print(df)

#-------------------------------------------------------------
 # data={
 #     'A':[1,2,3,4,5],
 #     'B': [3,4,7,8,1]
 # }
#
# df = pd.DataFrame(data)
# def calculate_sum(series):
#     return series.sum()
# column_sums = df.apply(calculate_sum)#(by default column_sums,axis=0)
# print("Column Sum:\n",column_sums)
#
# rows_sum = df.apply(calculate_sum,axis=1)#axis=1(for rows sum)
# print("Rows Sum:\n",rows_sum)
#
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#sorting and ordering
import pandas as pd
# #sample data
# data={
#     'Name':['iqra','haya','khadija','fariha'],
#     'Age':[22,21,12,11],
#     'Score':[89,76,67,99]
# }
# #create Dataframe
# df= pd.DataFrame(data)
# print("Original Data:\n",df)
#
# #sort by a age
# sorted_by_age = df.sort_values(by='Name')
# print("\nSorted by Name (Ascending):\n",sorted_by_age)

df = pd.read_csv('netliix.csv')
print(df)
sorted_by_country = df.sort_values(by=['country','type'])
print("\nSorted by Country (Ascending):\n",sorted_by_country)

s=sorted_by_country['type']
print(s)

#s.to_excel('new.xlsx', sheet_name='sheet1', index=True)
#print("\nData  written to 'output,xlsx'.")
# #sort by score
# sorted_by_Score = df.sort_values(by='Score')
# print("\nSorted by Score (Ascending):\n",sorted_by_Score)
#
# #sorted by multiple column with different order
# sorted_by_age_score_custom = df.sort_values(by=['Age','Score'],ascending=[True,False])
# print("\nSorted by Age(Ascending),score(descending):\n",sorted_by_age_score_custom)