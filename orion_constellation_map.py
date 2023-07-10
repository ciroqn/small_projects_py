# import tools for 3D scatter plot and rotation tools (which is what %matplotlib allows one to do in jupyter)
%matplotlib notebook
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data from NTU (Nottingham Trent Univ) for x, y ,z positions of stars in Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 2D scatter of x, y positions of stars
fig = plt.figure()
# axes for figure
fig.add_subplot(1,1,1)
plt.scatter(x,y)
plt.show()

# 3D scatter (x,y,z) of Orion constellation
fig_3d = plt.figure()
# adding axes for plot and specifying 3D projection
fig_3d.add_subplot(1,1,1, projection="3d")
# add data to 3D projection
consetellation3d = plt.scatter(x,y,z)
plt.show()
