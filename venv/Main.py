# import numpy
# import random
#
# arr=numpy.empty([5,2],dtype=numpy.uint16)
# arr[1][1]=10
#
# arr=numpy.arange(100,200,10)
# arr=arr.reshape(5,2)
#
# print(arr)

#------------------------------------------------------------------

# import numpy
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
# print("Printing Input Array")
# print(sampleArray)
# print("\n Printing array of items in the third column from all rows")
# newArray = sampleArray[...,2]
# print(newArray)
#------------------------------------------------------------------

# import numpy
# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
# print("Printing Input Array")
# print(sampleArray)
# print("\n Printing array of odd rows and even columns")
# newArray = sampleArray[0::2, 1::2]
# print(newArray)

#------------------------------------------------------------------

# import pandas as pd
# import os
# print(os.getcwd())
# try:
#     df = pd.read_csv("Automobile_data.csv",na_values={'price':["?","n.a"],'stroke':["?","n.a"],'horsepower':["?","n.a"],'peak-rpm':["?","n.a"],'average-mileage':["?","n.a"]})
#     print(df['price'])
#     # print(df.tail(5))
# except Exception as exp:
#     print(exp)
#------------------------------------------------------------------
# import pandas as pd
# df = pd.read_csv("Automobile_data.csv")
# # find columns having name toyota
# # print(df[['company','price']][df['company']=="toyota"])
# #or
# car_manufacturer = df.groupby('company')
# # print(df['company'].value_counts())
# #find each company's highest price car
# print(car_manufacturer['company','price'].max())
#------------------------------------------------------------------
#concatenate data from two different dictionary objects
# import pandas as pd
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# carsDf1 = pd.DataFrame.from_dict(GermanCars)
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
# carsDf2 = pd.DataFrame.from_dict(japaneseCars)
# carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
# print(carsDf)
#------------------------------------------------------------------
# # merge data from two objects, merge data on the basis of a common key
# import pandas as pd
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# carPriceDf = pd.DataFrame.from_dict(Car_Price)
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
# carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)
# carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
# print(carsDf)
#------------------------------------------------------------------