import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array([0, 1, 2, 4, 5, 7, 9])
ypoints = np.array([1, 5, 6, 7, 10, 11, 14])

plt.subplot(1, 2, 1)
plt.plot(xpoints, ypoints)

plt.xlabel("Indepedent Variable")
plt.ylabel("Dependent Variable")
plt.title("Experiment #1 Results")
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.title("Experiment #2 Results")
plt.grid(linestyle = "dashed")

plt.suptitle("Main data")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.legend(title = "My fruit list")
plt.show() 