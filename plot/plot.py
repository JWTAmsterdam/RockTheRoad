#very simple plotter for the csv data
#this example works specifically for the ice.csv data
#run on your terminal python plot.py
#how to change data here

from matplotlib import pyplot
import numpy as np

all_data = np.loadtxt(open("data/sample.csv","r"),
    delimiter=",",
    skiprows=1,
    dtype=np.float64
    )

velocity_data = all_data[:,0]
VW7FR_data = all_data[:,1]
VW7FL_data = all_data[:,2]
XAccel_data = all_data[:,3]

#print the values to veryfy the arrays
#print (velocity_data)
#print (VW7FR_data)
#print (VW7FL_data)
#print (XAccel_data)

fig = pyplot.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
fig.canvas.set_window_title('Data Plot')

plt1 = pyplot.subplot("321")
plt1.plot(velocity_data)
plt1.set_title('Velocity')
plt1.axes.get_xaxis().set_visible(False)
plt1.axes.get_yaxis().set_visible(False)

plt2 = pyplot.subplot("322")
plt2.plot(VW7FR_data)
plt2.set_title('VW Right')
plt2.axes.get_xaxis().set_visible(False)
plt2.axes.get_yaxis().set_visible(False)


plt3 = pyplot.subplot("323")
plt3.plot(VW7FL_data)
plt3.set_title('VW Left')
plt3.axes.get_xaxis().set_visible(False)
plt3.axes.get_yaxis().set_visible(False)


plt4 = pyplot.subplot("324")
plt4.plot(XAccel_data)
plt4.set_title('Acceleration')
plt4.axes.get_xaxis().set_visible(False)
plt4.axes.get_yaxis().set_visible(False)

#rest of plots

pyplot.show()