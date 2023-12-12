import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(x + np.pi/4)
y3 = np.sin(x + np.pi/2)
plt.plot(x, y1 , color='black', label='Sine Wave 1', linestyle='dashed')
plt.plot(x, y2, color='blue', label='Sine Wave 2', linestyle='dashed')
plt.plot(x, y3, color='red', label='Sine Wave 3', linestyle='dashed')
plt.title('Multiple Wave lines')
plt.xlabel('sin(x)')
plt.ylabel('cos(x)')
plt.legend()
plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.sin(x + np.pi/3)
# y3 = np.sin(x + np.pi/4)
# y4 = np.sin(x + np.pi/5)
# plt.plot(x, y1, color='blue', label='sine wave 1', linspace='dashed')
# plt.plot(x, y2, color='black', label='sin wave 2',linspace='dashed')
# plt.plot(x, y3, color='orange, label=sin wave 3',linspace='dashed')
# plt.plot(x, y4, color='red', label='sin wave4', linspace='dashed')
# plt.title('Multiple line wave')
# plt.xlabel('sin(x)')
# plt.ylabel('cos(y)')
# plt.legend()
# plt.show()

