import matplotlib.pyplot as plt
def fibo_and_golden(n):
  #first 2 numbers of the fibonacci sequence
  fibo_seq=[1,1]
  for i in range(n):
    fibo_seq.append(fibo_seq[-1]+fibo_seq[-2])
  
  golden_ratio=[]
  for j in range(len(fibo_seq)-1):
    ratio=fibo_seq[j+1]/fibo_seq[j]
    golden_ratio.append(ratio)
  
  plt.plot(range(1,len(golden_ratio)+1),golden_ratio)
  plt.show()
  

fibo_and_golden(100)

