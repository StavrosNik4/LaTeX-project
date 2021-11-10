import math
import numpy as np
import matplotlib.pyplot as plt 

in_array_cos = np.linspace(-(np.pi), np.pi, 20) #the range of θ is(-π,π)
out_array_cos = []
#creating the points for the cos chart
for i in range(len(in_array_cos)):
    out_array_cos.append(math.cos(in_array_cos[i]))
    i += 1
   
print("in_array : ", in_array_cos)
print("\nout_array : ", out_array_cos)
  
# creating the chart
plt.plot(in_array_cos, out_array_cos, color = 'red', marker = "o", label = "cos(θ)") 

plt.title("Plot of cos(θ)") 
plt.xlabel("θ") 
plt.ylabel("cos(θ)") 

plt.annotate('cos(pi/4)', xy =(-0.85, 0.681),
                xytext =(-0.30, 0.651), 
                arrowprops = dict(facecolor ='red',
                                  shrink = 1),)

plt.legend()



plt.show()



