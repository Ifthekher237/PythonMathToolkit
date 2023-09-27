
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import math

def sort(get_data):
  #sorting get_sorted_data in ascending order
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

def Mean(get_data):
    #accumulate([1,2,3])==> a generator ==>list(generator)==>[1,3,6]
    mean=list(itertools.accumulate(get_data))[-1]/len(get_data)
    return "{:.1f}".format(mean)
    

def Median(get_data):        
    
    n=len(get_data)
    if n%2 != 0:
        median=get_data[int(math.floor(n/2))]
    else:
        median=(get_data[int((n/2)-1)] + get_data[int(n/2)])/2
    return "{:.1f}".format(median)
        

def Mode(get_data):
    print(get_data)
    freq_of_val={} #dictionary
    for val in get_data:
        if val not in freq_of_val:
            freq_of_val[val]=1
        else:
            freq_of_val[val]+=1

    max_freq=max(freq_of_val.values())

   
    tupl=freq_of_val.items()
    for val, freq in tupl:
      if freq==max_freq:
        mode=val
        break
  
    return mode

    

    

data=[64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
get_sorted_data=sort(data)


mean=Mean(get_sorted_data)
mode=Mode(get_sorted_data)
median=Median(get_sorted_data)

print(mean,median,mode)


