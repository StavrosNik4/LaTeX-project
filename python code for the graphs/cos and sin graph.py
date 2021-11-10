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
  
#printing the values for θ and cos(θ)   
print("in_array_cos : ", in_array_cos)
print("\nout_array_cos : ", out_array_cos)


#printing the values for θ and sin(θ) 
print("in_array_sin : ", in_array_sin)
print("\nout_array_sin : ", out_array_sin)
  
# creating the graph
plt.plot(in_array_cos, out_array_cos, color = 'blue', marker = "o", label='cos(θ)') 
plt.plot(in_array_sin, out_array_sin, color = 'green', marker = "o", label='sin(θ)')
plt.title("Plot of cos(θ) and sin(θ)") 
plt.xlabel("θ") 
plt.ylabel("cos(θ) and sin(θ)") 

# annotations for cos(-pi/4) and sin(-pi/4)
plt.annotate('cos(-pi/4)', xy =(-0.85, 0.681),
                xytext =(-0.30, 0.651), 
                arrowprops = dict(facecolor ='black',
                                  shrink = 1),)
plt.annotate('sin(-pi/4)', xy =(-0.85, -0.710),
                xytext =(-0.2, -0.730), 
                arrowprops = dict(facecolor ='black',
                                  shrink = 1),)

plt.legend()

plt.show()
