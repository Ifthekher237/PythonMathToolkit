#this program prints variance, SD of a dataset and also plot the mean 
#and the values of the datatset
import math
import matplotlib.pyplot as plt

def mean(list):
  sum=0
  for ele in list:
    sum+=ele
  
  return sum/len(list)

data=[4,2,6,3,1,2]

#list of squared distances from mean
squared_dis_from_mean=[(mean(data)-ele)**2 for ele in data]

variance=mean(squared_dis_from_mean)    #variance is the mean of squared distances from mean
SD=math.pow(variance, .5)   #SD is the square root of variance
print("variance :{}\nSD :{}".format(variance, SD))

plt.title("variation of the values around the mean")
#plot an horizontal line, the mean of the dataset
plt.axhline(y=mean(data), color='r', linestyle='-', label="mean")
#ploting the values of the dataset to see how far they are from the mean line
plt.plot(range(len(data)),data, marker="o")
plt.legend()
plt.show()
