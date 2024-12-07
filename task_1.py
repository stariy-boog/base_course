import matplotlib.pyplot as plt
x = [1,1,5,5,1]
y = [1,5,5,1,1]
plt.plot(x,y, color = 'black', marker = 'o', ms = 20)
plt.axis('equal')
plt.savefig('fig_5.png')