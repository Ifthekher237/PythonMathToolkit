from collections import Counter
import matplotlib.pyplot as plt
def freq_table(list):
  #list.sort()
  c=Counter(list)
  mode=c.most_common()
  print("Score  ","Frequency")
  scores=[]
  freqs=[]
  for score, freq in mode:
    scores.append(score)
    freqs.append(freq)
    print("{:^7d}{:^9d}".format(score, freq))
  
  plt.bar(scores, freqs)
  plt.axis(ymax=10)
  plt.title("frequency distribution")
  plt.xlabel("value")
  plt.ylabel("frequency")
  plt.show()
  
data=[7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
data.sort()
freq_table(data)