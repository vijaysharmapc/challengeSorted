
# coding: utf-8

# In[250]:

# match product and listings : done, 4522 matches found
# A single price listing may match at most one product (canon digital ixus 1000 hs - marron has 2 records for price 422.99)
# are many such cases)
# Precision – do you make many false matches( Tried my best , by making the join using fields title & product_name as tight as possible)
# Recall – how many correct matches did you make(3284)
# Appropriate data structure and algorithm choices ( Used dict ,pandas,series )
# I am not very sure if the o/p file format meets expectation


# In[251]:

import pandas as pd
import sqlite3
import json_lines


# In[252]:

def createDF(filename):
    fname = filename
    cnt =1
    with open(fname, 'rb') as f:
        for item in json_lines.reader(f):
            if cnt == 1 :
                ds = pd.Series(item)
                df =pd.DataFrame(ds)
                toDF = df.transpose()
                cnt += 1
            else :
                ds2 = pd.Series(item)
                df2 =pd.DataFrame(ds2)
                df2 = df2.transpose()
                toDF = pd.concat([toDF,df2])
    return(toDF)


# In[253]:

prodDF = createDF('products.txt')
lstDF = createDF('listings.txt')
print("products row count : ")
print(prodDF.count())
print("listings row count : ")
print(lstDF.count())


# In[254]:

#Data Prepration- to help with joins
new_prodDF= prodDF.replace({'_': ' '}, regex=True)
new_prodDF['product_name'] = new_prodDF['product_name'].str.lower()
#new_prodDF.head(10)


# In[255]:

#we need to avoid false positive match,hence exclude null fields that make product_name coulmn
# count of null values in family,manufacturer & model
print("Finding null values in product fields,only family has 258 nulls")
print(new_prodDF['family'].isnull().sum()) # only family has null values
print(new_prodDF['manufacturer'].isnull().sum())
print(new_prodDF['model'].isnull().sum())


# In[256]:

new_lstDF= lstDF
new_lstDF['title'] = new_lstDF['title'].str.lower()
#new_lstDF.head(5)


# In[257]:

#we join these two data frames


# In[258]:

import sqlite3
conn = sqlite3.connect(':memory:')
new_lstDF.to_sql('new_lstDF', conn, index=False)
new_prodDF.to_sql('new_prodDF', conn, index=False)
query = """
SELECT [new_prodDF].[product_name],
       [new_prodDF].[announced-date],
       [new_prodDF].[family],
       [new_prodDF].[model],
       [new_lstDF].[title],
       [new_lstDF].[manufacturer],
       [new_lstDF].[currency],
       [new_lstDF].[price]
FROM   ([new_lstDF]
        LEFT JOIN [new_prodDF]
                    on ([new_lstDF].[title]) LIKE ([new_prodDF].[product_name]||"%")
)   WHERE product_name IS NOT NULL
group by 1,2,3,4,5,6,7,8
"""
matchedDF = pd.read_sql_query(query, conn)
conn.close()
#matchedDF

#WHERE [new_prodDF].[family] IS NOT Null
#       AND [new_prodDF].[model] IS NOT NULL
#       AND [new_prodDF].[manufacturer] IS NOT NULL


# In[259]:

print("count of all matched records")
print(matchedDF.count())


# In[260]:

matchedDF.groupby(['product_name','title', 'price']).count()
# All the product name and title have a count of one, though there are multiple prices


# In[261]:

matchedDF =matchedDF[['product_name','title','manufacturer','currency','price']]
print("Top 20 objects from matched data frame")
print(matchedDF.head(20))


# In[263]:

out = matchedDF.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('results.txt', 'w') as f:
    f.write(out)
    print("matched records saved in file results.txt")


# In[ ]:




# In[ ]:




# out = df20.to_json(orient='records')[1:-1].replace('},{', '} {')
# with open('file_name.txt', 'w') as f:
#     f.write(out)

# In[ ]:




# df20['listings'] = df20[df20.columns[1:]].apply(lambda x: ','.join(x.dropna()),axis=1)
# df20 = df20[['product_name','listings']]
# df20

# In[ ]:



