#list - create a list of intergers to represent the daily temperature of 
#temperature in celsius
temperature = [22, 24, 23, 30, 28, 27, 23]

#Add - the temperature 33 to the list (adds to the end)
temperature.append(33)

#Find - the index of value 33 in the list 
index = temperature.index(33)
print(index)
#Delete - the value 22 from the list 
temperature.remove(33)
print(temperature)
#Access value by index
sunday_temp = temperature[0]
print(sunday_temp)
#sort the list 
temperature.sort()
print(temperature)
#get and print the highest temperature
highest_temp = temperature.pop()
print(highest_temp)





