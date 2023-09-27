import math
import itertools


def sort(get_data):
  #sorting data in ascending order
    sorted_data=[]
    n=len(get_data)
    while n>0:
        min_value=get_data[0]
        for val in get_data:
            if val<= min_value:min_value=val
        sorted_data.append(min_value)
        get_data.remove(min_value)
        n-=1
    return sorted_data


def Median(get_arr):
  #left_pos and right_pos hoilo median er ager value er position & porer value 
  #er position

  #left_pos & right_pos er value gulo k global variable hisebe declare krtechi
  #karon first_quartile & third_quartile er median ber korar somoy jeno amader k
  #abar ei value gulo return krte na hoi
  global left_pos, right_pos

  n=len(get_arr)
  if n%2==0:
    left_pos=int(n/2)-1
    right_pos=int(n/2)
    median=(get_arr[int(n/2)-1]+get_arr[int(n/2)])/2
  else:
    left_pos=int(n/2)-1
    right_pos=int(n/2)+1
    median=get_arr[int(n/2)]

  return median


def InterQuartileRange(get_arr):

  second_quartile=Median(get_arr) #median of the whole dataset is the second quartile

  left_half=[]
  for i in range(left_pos+1):
    left_half.append(get_arr[i])
  
  #left_half ber korei sathe sathe tar median ber korar jonno amra Median() function
  #k call krtechi na karon ei function call krle left_pos & right_pos er value
  #gulo update hoi jabe which we don't want 
  #right_half er khetre o same reason
  
  right_half=[]
  for j in range(right_pos, len(get_arr)):
    right_half.append(get_arr[j])
  
  first_quartile=Median(left_half) #median of first half is the first quartile
  third_quartile=Median(right_half) #mdian of last half is the third quartile

  interquartile_range=third_quartile - first_quartile
  print("{:.1f}".format(interquartile_range))



n = int(input().strip())

values = list(map(int, input().rstrip().split()))

freqs = list(map(int, input().rstrip().split()))
data=[]
for val, frq in list(zip(values, freqs)):
  data+=list(itertools.repeat(val,frq))

print(data)

get_sorted_data=sort(data)
InterQuartileRange(get_sorted_data)