import math
import numpy as np
import matplotlib.pyplot as plt 
 
in_array_cos = np.linspace(-(np.pi), np.pi, 20) #the range of θ is(-π,π)
out_array_cos = []
#creating the points for the cos graph
for i in range(len(in_array_cos)):
    out_array_cos.append(math.cos(in_array_cos[i]))
    i += 1

in_array_sin = np.linspace(-(np.pi), np.pi, 20)
out_array_sin = [] 

#creating the points for the sin graph
for i in range(len(in_array_cos)):
    out_array_sin.append(math.sin(in_array_sin[i]))
    i += 1
  
   
print("in_array : ", in_array_cos)
print("\nout_array : ", out_array_cos)
  
# creating the graph
plt.plot(in_array_cos, out_array_cos, color = 'blue', marker = "o") 
plt.plot(in_array_sin, out_array_sin, color = 'green', marker = "o")

plt.title("Plot of cos(θ) and sin(θ)") 
plt.xlabel("θ") 
plt.ylabel("cos(θ) and sin(θ)") 

plt.show()