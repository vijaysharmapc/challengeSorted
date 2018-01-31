# challengeSorted

ON python3 cli- please run the file finalMatchingProductListing.py (python finalMatchingProductListing.py)
On NOtebook - please view and run the commands in file "finalMatchingProductListing.ipynb"


Contains:
Challenged posted here (https://sortable.com/project/)

Steps followed:
1) Read the files into Pandas Dataframe
2) Parse & Normalise the text fields
3) Join the two data frames using sqlite
4) Save the resulting data frame as json file-results.txt(matchedDF,record count 4522)

Task Objectives:
# match product and listings : done, 4522 matches found
# A single price listing may match at most one product (canon digital ixus 1000 hs - marron has 2 records for price 422.99,cases like these were handeled by group by)
# Precision – do you make many false matches( Tried my best , by making the join using fields title & product_name as tight as possible)
# Recall – how many correct matches did you make(4522)
# Appropriate data structure and algorithm choices ( Used dict ,pandas,series )
# I am not very sure if the o/p file format meets expectation as the curl test gave an Error


