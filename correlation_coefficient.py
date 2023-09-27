#correlation coefficient formula: https://cdn.corporatefinanceinstitute.com/assets/correlation1.png
#finds the correlation coefficient of two different datasets and graph a scatter plot these datasets to see their correlation

import math
import matplotlib.pyplot as plt

def Mean(list):
  sum=0
  for ele in list:
    sum+=ele
  mean=sum/len(list)
  return mean


def correlationOF_X_Y(X,Y):
  mean_x=Mean(X)
  mean_y=Mean(Y)
  numerator=0
  #denominator part is way long, so i divided it into 2 parts and after calculating
  #both part, I combined them to get the final denominator
  denominator_part1=0
  denominator_part2=0
  for x, y in zip(X, Y):
    numerator+=(x-mean_x)*(y-mean_y)
    denominator_part1+=(x-mean_x)**2
    denominator_part2+=(y-mean_y)**2

  denominator=math.sqrt(denominator_part1*denominator_part2)
  r=numerator/denominator
  print(r)


def scatter_plt(X,Y):
  plt.plot(X,Y,"o")
  plt.title("scatter plot")
  plt.xlabel("Temperature °C")
  plt.ylabel("Sales in $")
  plt.show()

X=[14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]
Y=[215,325,185,332,406,522,412,614,544,421,445,408]

correlationOF_X_Y(X,Y)
scatter_plt(X,Y)
