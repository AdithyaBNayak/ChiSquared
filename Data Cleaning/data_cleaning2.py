import pandas as pd
import numpy as np

df = pd.read_excel(r"Customer Call List.xlsx")
print(df)

"""
Output:    

    CustomerID First_Name    Last_Name  ... Paying Customer Do_Not_Contact Not_Useful_Column
0         1001      Frodo      Baggins  ...             Yes             No              True
1         1002       Abed        Nadir  ...              No            Yes             False
2         1003     Walter       /White  ...               N            NaN              True
3         1004     Dwight      Schrute  ...             Yes              Y              True
4         1005        Jon         Snow  ...               Y             No              True
5         1006        Ron      Swanson  ...             Yes            Yes              True
6         1007       Jeff       Winger  ...              No             No             False
7         1008   Sherlock       Holmes  ...               N             No             False
8         1009    Gandalf          NaN  ...             Yes            NaN             False
9         1010      Peter       Parker  ...             Yes             No              True
10        1011    Samwise       Gamgee  ...             Yes             No              True
11        1012      Harry    ...Potter  ...               Y            NaN              True
12        1013        Don       Draper  ...             Yes              N             False
13        1014     Leslie        Knope  ...             Yes             No             False
14        1015       Toby  Flenderson_  ...               N             No             False
15        1016        Ron      Weasley  ...              No              N             False
16        1017   Michael         Scott  ...             Yes             No             False
17        1018      Clark         Kent  ...               Y            NaN              True
18        1019      Creed       Braton  ...             N/a            Yes              True
19        1020     Anakin    Skywalker  ...             Yes              N              True
20        1020     Anakin    Skywalker  ...             Yes              N              True

[21 rows x 8 columns]
    
"""

print("\nDropping Duplicates")
df = df.drop_duplicates()
print(df)

""" 
Dropping Duplicates
    CustomerID First_Name    Last_Name  ... Paying Customer Do_Not_Contact Not_Useful_Column
0         1001      Frodo      Baggins  ...             Yes             No              True
1         1002       Abed        Nadir  ...              No            Yes             False
2         1003     Walter       /White  ...               N            NaN              True
3         1004     Dwight      Schrute  ...             Yes              Y              True
4         1005        Jon         Snow  ...               Y             No              True
5         1006        Ron      Swanson  ...             Yes            Yes              True
6         1007       Jeff       Winger  ...              No             No             False
7         1008   Sherlock       Holmes  ...               N             No             False
8         1009    Gandalf          NaN  ...             Yes            NaN             False
9         1010      Peter       Parker  ...             Yes             No              True
10        1011    Samwise       Gamgee  ...             Yes             No              True
11        1012      Harry    ...Potter  ...               Y            NaN              True
12        1013        Don       Draper  ...             Yes              N             False
13        1014     Leslie        Knope  ...             Yes             No             False
14        1015       Toby  Flenderson_  ...               N             No             False
15        1016        Ron      Weasley  ...              No              N             False
16        1017   Michael         Scott  ...             Yes             No             False
17        1018      Clark         Kent  ...               Y            NaN              True
18        1019      Creed       Braton  ...             N/a            Yes              True
19        1020     Anakin    Skywalker  ...             Yes              N              True

[20 rows x 8 columns]

No of rows decresed from 21 to 20
"""
print("\n\nRemove a particular column")
df = df.drop(columns = "Not_Useful_Column")
print(df)

"""
    CustomerID First_Name    Last_Name  Phone_Number                                Address Paying Customer Do_Not_Contact       
0         1001      Frodo      Baggins  123-545-5421                  123 Shire Lane, Shire             Yes             No       
1         1002       Abed        Nadir  123/643/9775                    93 West Main Street              No            Yes       
2         1003     Walter       /White    7066950392                     298 Drugs Driveway               N            NaN       
3         1004     Dwight      Schrute  123-543-2345  980 Paper Avenue, Pennsylvania, 18503             Yes              Y       
4         1005        Jon         Snow  876|678|3469                       123 Dragons Road               Y             No       
5         1006        Ron      Swanson  304-762-2467                       768 City Parkway             Yes            Yes       
6         1007       Jeff       Winger           NaN                      1209 South Street              No             No       
7         1008   Sherlock       Holmes  876|678|3469                          98 Clue Drive               N             No       
8         1009    Gandalf          NaN           N/a                       123 Middle Earth             Yes            NaN       
9         1010      Peter       Parker  123-545-5421             25th Main Street, New York             Yes             No       
10        1011    Samwise       Gamgee           NaN                  612 Shire Lane, Shire             Yes             No       
11        1012      Harry    ...Potter    7066950392                   2394 Hogwarts Avenue               Y            NaN       
12        1013        Don       Draper  123-543-2345                       2039 Main Street             Yes              N       
13        1014     Leslie        Knope  876|678|3469                       343 City Parkway             Yes             No       
14        1015       Toby  Flenderson_  304-762-2467                          214 HR Avenue               N             No       
15        1016        Ron      Weasley  123-545-5421                   2395 Hogwarts Avenue              No              N       
16        1017   Michael         Scott  123/643/9775         121 Paper Avenue, Pennsylvania             Yes             No       
17        1018      Clark         Kent    7066950392                        3498 Super Lane               Y            NaN       
18        1019      Creed       Braton           N/a                                    N/a             N/a            Yes       
19        1020     Anakin    Skywalker  876|678|3469            910 Tatooine Road, Tatooine             Yes              N    
"""

print("\n\nStrip the '...' in Last_name column")
# df['Last_Name'] = df['Last_Name'].str.lstrip("...")
# df['Last_Name'] = df['Last_Name'].str.strip("/")
# df['Last_Name'] = df['Last_Name'].str.rstrip("_")
df['Last_Name'] = df['Last_Name'].str.strip("123/._")

print(df)

""" 
...Potter changed to Potter
/White changed White
Flenderson_ changed to Flenderson
"""
print("\n\nFormat the phone number")
#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','') This is not workings

df["Phone_Number"] = df["Phone_Number"].str.replace('-','')
df["Phone_Number"] = df["Phone_Number"].str.replace('|','')
df["Phone_Number"] = df["Phone_Number"].str.replace('/','')


print(df)


""" 
    CustomerID First_Name   Last_Name Phone_Number                                Address Paying Customer Do_Not_Contact
0         1001      Frodo     Baggins   1235455421                  123 Shire Lane, Shire             Yes             No
1         1002       Abed       Nadir   1236439775                    93 West Main Street              No            Yes
2         1003     Walter       White          NaN                     298 Drugs Driveway               N            NaN
3         1004     Dwight     Schrute   1235432345  980 Paper Avenue, Pennsylvania, 18503             Yes              Y
4         1005        Jon        Snow   8766783469                       123 Dragons Road               Y             No
5         1006        Ron     Swanson   3047622467                       768 City Parkway             Yes            Yes
6         1007       Jeff      Winger          NaN                      1209 South Street              No             No
7         1008   Sherlock      Holmes   8766783469                          98 Clue Drive               N             No
8         1009    Gandalf         NaN           Na                       123 Middle Earth             Yes            NaN
9         1010      Peter      Parker   1235455421             25th Main Street, New York             Yes             No
10        1011    Samwise      Gamgee          NaN                  612 Shire Lane, Shire             Yes             No
11        1012      Harry      Potter          NaN                   2394 Hogwarts Avenue               Y            NaN
12        1013        Don      Draper   1235432345                       2039 Main Street             Yes              N
13        1014     Leslie       Knope   8766783469                       343 City Parkway             Yes             No
14        1015       Toby  Flenderson   3047622467                          214 HR Avenue               N             No
15        1016        Ron     Weasley   1235455421                   2395 Hogwarts Avenue              No              N
16        1017   Michael        Scott   1236439775         121 Paper Avenue, Pennsylvania             Yes             No
17        1018      Clark        Kent          NaN                        3498 Super Lane               Y            NaN
18        1019      Creed      Braton           Na                                    N/a             N/a            Yes
19        1020     Anakin   Skywalker   8766783469            910 Tatooine Road, Tatooine             Yes              N
"""

print("\n\nFormatting more...")
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:9] )
df["Phone_Number"] = df["Phone_Number"].str.replace("Na--", "NaN")
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "")
print(df)

"""
    CustomerID First_Name   Last_Name Phone_Number                                Address Paying Customer Do_Not_Contact
0         1001      Frodo     Baggins  123-545-542                  123 Shire Lane, Shire             Yes             No
1         1002       Abed       Nadir  123-643-977                    93 West Main Street              No            Yes
2         1003     Walter       White                                  298 Drugs Driveway               N            NaN
3         1004     Dwight     Schrute  123-543-234  980 Paper Avenue, Pennsylvania, 18503             Yes              Y
4         1005        Jon        Snow  876-678-346                       123 Dragons Road               Y             No
5         1006        Ron     Swanson  304-762-246                       768 City Parkway             Yes            Yes
6         1007       Jeff      Winger                                   1209 South Street              No             No
7         1008   Sherlock      Holmes  876-678-346                          98 Clue Drive               N             No
8         1009    Gandalf         NaN                                    123 Middle Earth             Yes            NaN
9         1010      Peter      Parker  123-545-542             25th Main Street, New York             Yes             No
10        1011    Samwise      Gamgee                               612 Shire Lane, Shire             Yes             No
11        1012      Harry      Potter                                2394 Hogwarts Avenue               Y            NaN
12        1013        Don      Draper  123-543-234                       2039 Main Street             Yes              N
13        1014     Leslie       Knope  876-678-346                       343 City Parkway             Yes             No
14        1015       Toby  Flenderson  304-762-246                          214 HR Avenue               N             No
15        1016        Ron     Weasley  123-545-542                   2395 Hogwarts Avenue              No              N
16        1017   Michael        Scott  123-643-977         121 Paper Avenue, Pennsylvania             Yes             No
17        1018      Clark        Kent                                     3498 Super Lane               Y            NaN
18        1019      Creed      Braton                                                 N/a             N/a            Yes
19        1020     Anakin   Skywalker  876-678-346            910 Tatooine Road, Tatooine             Yes              N

"""
# df[['Street_Adress', 'Street','PinCode']] = df['Address'].str.split(",",expand=True)
# print(df)

"""
        CustomerID First_Name   Last_Name Phone_Number  ... Do_Not_Contact         Street_Adress         Street PinCode
0         1001      Frodo     Baggins  123-545-542  ...             No        123 Shire Lane          Shire    None
1         1002       Abed       Nadir  123-643-977  ...            Yes   93 West Main Street           None    None
2         1003     Walter       White               ...            NaN    298 Drugs Driveway           None    None
3         1004     Dwight     Schrute  123-543-234  ...              Y      980 Paper Avenue   Pennsylvania   18503
4         1005        Jon        Snow  876-678-346  ...             No      123 Dragons Road           None    None
5         1006        Ron     Swanson  304-762-246  ...            Yes      768 City Parkway           None    None
6         1007       Jeff      Winger               ...             No     1209 South Street           None    None
7         1008   Sherlock      Holmes  876-678-346  ...             No         98 Clue Drive           None    None
8         1009    Gandalf         NaN          NaN  ...            NaN      123 Middle Earth           None    None
9         1010      Peter      Parker  123-545-542  ...             No      25th Main Street       New York    None
10        1011    Samwise      Gamgee               ...             No        612 Shire Lane          Shire    None
11        1012      Harry      Potter               ...            NaN  2394 Hogwarts Avenue           None    None
12        1013        Don      Draper  123-543-234  ...              N      2039 Main Street           None    None
13        1014     Leslie       Knope  876-678-346  ...             No      343 City Parkway           None    None
14        1015       Toby  Flenderson  304-762-246  ...             No         214 HR Avenue           None    None
15        1016        Ron     Weasley  123-545-542  ...              N  2395 Hogwarts Avenue           None    None
16        1017   Michael        Scott  123-643-977  ...             No      121 Paper Avenue   Pennsylvania    None
17        1018      Clark        Kent               ...            NaN       3498 Super Lane           None    None
18        1019      Creed      Braton          NaN  ...            Yes                   N/a           None    None
19        1020     Anakin   Skywalker  876-678-346  ...              N     910 Tatooine Road       Tatooine    None
"""
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

print(df)
""" 
    CustomerID First_Name   Last_Name  ...                                Address Paying Customer Do_Not_Contact 
0         1001      Frodo     Baggins  ...                  123 Shire Lane, Shire               Y             No 
1         1002       Abed       Nadir  ...                    93 West Main Street               N            Yes 
2         1003     Walter       White  ...                     298 Drugs Driveway               N            NaN 
3         1004     Dwight     Schrute  ...  980 Paper Avenue, Pennsylvania, 18503               Y              Y 
4         1005        Jon        Snow  ...                       123 Dragons Road               Y             No 
5         1006        Ron     Swanson  ...                       768 City Parkway               Y            Yes 
6         1007       Jeff      Winger  ...                      1209 South Street               N             No 
7         1008   Sherlock      Holmes  ...                          98 Clue Drive               N             No 
8         1009    Gandalf         NaN  ...                       123 Middle Earth               Y            NaN 
9         1010      Peter      Parker  ...             25th Main Street, New York               Y             No 
10        1011    Samwise      Gamgee  ...                  612 Shire Lane, Shire               Y             No 
11        1012      Harry      Potter  ...                   2394 Hogwarts Avenue               Y            NaN 
12        1013        Don      Draper  ...                       2039 Main Street               Y              N 
13        1014     Leslie       Knope  ...                       343 City Parkway               Y             No 
14        1015       Toby  Flenderson  ...                          214 HR Avenue               N             No 
15        1016        Ron     Weasley  ...                   2395 Hogwarts Avenue               N              N 
16        1017   Michael        Scott  ...         121 Paper Avenue, Pennsylvania               Y             No 
17        1018      Clark        Kent  ...                        3498 Super Lane               Y            NaN 
18        1019      Creed      Braton  ...                                    N/a             N/a            Yes 
19        1020     Anakin   Skywalker  ...            910 Tatooine Road, Tatooine               Y              N 

"""
print("\n\n Remove all NA values to empty string '' ")
df = df.replace("N/a", "")
df = df.replace("NaN", "")
# df = df.replace(np.nan, "")
df = df.fillna("")
print(df)

"""
   CustomerID First_Name   Last_Name  ...                                Address Paying Customer Do_Not_Contact
0         1001      Frodo     Baggins  ...                  123 Shire Lane, Shire               Y             No 
1         1002       Abed       Nadir  ...                    93 West Main Street               N            Yes 
2         1003     Walter       White  ...                     298 Drugs Driveway               N
3         1004     Dwight     Schrute  ...  980 Paper Avenue, Pennsylvania, 18503               Y              Y 
4         1005        Jon        Snow  ...                       123 Dragons Road               Y             No 
5         1006        Ron     Swanson  ...                       768 City Parkway               Y            Yes 
6         1007       Jeff      Winger  ...                      1209 South Street               N             No 
7         1008   Sherlock      Holmes  ...                          98 Clue Drive               N             No 
8         1009    Gandalf              ...                       123 Middle Earth               Y
9         1010      Peter      Parker  ...             25th Main Street, New York               Y             No 
10        1011    Samwise      Gamgee  ...                  612 Shire Lane, Shire               Y             No 
11        1012      Harry      Potter  ...                   2394 Hogwarts Avenue               Y
12        1013        Don      Draper  ...                       2039 Main Street               Y              N 
13        1014     Leslie       Knope  ...                       343 City Parkway               Y             No 
14        1015       Toby  Flenderson  ...                          214 HR Avenue               N             No 
15        1016        Ron     Weasley  ...                   2395 Hogwarts Avenue               N              N 
16        1017   Michael        Scott  ...         121 Paper Avenue, Pennsylvania               Y             No 
17        1018      Clark        Kent  ...                        3498 Super Lane               Y
18        1019      Creed      Braton  ...                                                                   Yes 
19        1020     Anakin   Skywalker  ...            910 Tatooine Road, Tatooine               Y              N 

[20 rows x 7 columns]
    """

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')

for x in df.index:
    # df.loc[row_selection, column_selection]
    if df.loc[x,'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace=True)

# df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace("","N")
print(df)
""" 
    CustomerID First_Name   Last_Name  ...                         Address Paying Customer Do_Not_Contact
0         1001      Frodo     Baggins  ...           123 Shire Lane, Shire               Y            NNN        
2         1003     Walter       White  ...              298 Drugs Driveway               N              N        
4         1005        Jon        Snow  ...                123 Dragons Road               Y            NNN        
6         1007       Jeff      Winger  ...               1209 South Street               N            NNN        
7         1008   Sherlock      Holmes  ...                   98 Clue Drive               N            NNN        
8         1009    Gandalf              ...                123 Middle Earth               Y              N        
9         1010      Peter      Parker  ...      25th Main Street, New York               Y            NNN        
10        1011    Samwise      Gamgee  ...           612 Shire Lane, Shire               Y            NNN        
11        1012      Harry      Potter  ...            2394 Hogwarts Avenue               Y              N        
12        1013        Don      Draper  ...                2039 Main Street               Y            NNN        
13        1014     Leslie       Knope  ...                343 City Parkway               Y            NNN        
14        1015       Toby  Flenderson  ...                   214 HR Avenue               N            NNN        
15        1016        Ron     Weasley  ...            2395 Hogwarts Avenue               N            NNN        
16        1017   Michael        Scott  ...  121 Paper Avenue, Pennsylvania               Y            NNN        
17        1018      Clark        Kent  ...                 3498 Super Lane               Y              N        
19        1020     Anakin   Skywalker  ...     910 Tatooine Road, Tatooine               Y            NNN        

[16 rows x 7 columns]

"""
print(df.reset_index())
""" 
   index  CustomerID First_Name  ...                         Address Paying Customer Do_Not_Contact
0       0        1001      Frodo  ...           123 Shire Lane, Shire               Y              N
1       2        1003     Walter  ...              298 Drugs Driveway               N
2       4        1005        Jon  ...                123 Dragons Road               Y              N
3       6        1007       Jeff  ...               1209 South Street               N              N
4       7        1008   Sherlock  ...                   98 Clue Drive               N              N
5       8        1009    Gandalf  ...                123 Middle Earth               Y
6       9        1010      Peter  ...      25th Main Street, New York               Y              N
7      10        1011    Samwise  ...           612 Shire Lane, Shire               Y              N
8      11        1012      Harry  ...            2394 Hogwarts Avenue               Y
9      12        1013        Don  ...                2039 Main Street               Y              N
10     13        1014     Leslie  ...                343 City Parkway               Y              N
11     14        1015       Toby  ...                   214 HR Avenue               N              N
12     15        1016        Ron  ...            2395 Hogwarts Avenue               N              N
13     16        1017   Michael   ...  121 Paper Avenue, Pennsylvania               Y              N
14     17        1018      Clark  ...                 3498 Super Lane               Y
15     19        1020     Anakin  ...     910 Tatooine Road, Tatooine               Y              N

[16 rows x 8 columns]

This keeps the old index as well
"""
df = print(df.reset_index(drop= True))
print(df)
""" 
   CustomerID First_Name   Last_Name  ...                         Address Paying Customer Do_Not_Contact
0         1001      Frodo     Baggins  ...           123 Shire Lane, Shire               Y              N        
1         1003     Walter       White  ...              298 Drugs Driveway               N
2         1005        Jon        Snow  ...                123 Dragons Road               Y              N        
3         1007       Jeff      Winger  ...               1209 South Street               N              N        
4         1008   Sherlock      Holmes  ...                   98 Clue Drive               N              N        
5         1009    Gandalf              ...                123 Middle Earth               Y
6         1010      Peter      Parker  ...      25th Main Street, New York               Y              N        
7         1011    Samwise      Gamgee  ...           612 Shire Lane, Shire               Y              N        
8         1012      Harry      Potter  ...            2394 Hogwarts Avenue               Y
9         1013        Don      Draper  ...                2039 Main Street               Y              N        
10        1014     Leslie       Knope  ...                343 City Parkway               Y              N        
11        1015       Toby  Flenderson  ...                   214 HR Avenue               N              N        
12        1016        Ron     Weasley  ...            2395 Hogwarts Avenue               N              N        
13        1017   Michael        Scott  ...  121 Paper Avenue, Pennsylvania               Y              N        
14        1018      Clark        Kent  ...                 3498 Super Lane               Y
15        1020     Anakin   Skywalker  ...     910 Tatooine Road, Tatooine               Y              N        

[16 rows x 7 columns]
None
"""