from pylab import *
import matplotlib.pyplot as plt

def my_autopct(pct):
	if pct > 5:
	    return '{p:.1f}%'.format(p=pct)
	else:
		return ''

cmap = plt.cm.prism
colors = cmap(np.linspace(0, 1,16))

# make a square figure and axes
figure(1, figsize=(12,6))
ax = axes([0.1, 0.1, 0.40, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = ['1+2', '1+2+3', '1+2+3+4', '2', '1+3', '1', '3', '2+4', '1+2+4', '2+3', '2+3+4', '1+3+4', '3+4' , '4' , '1+4']
# fracs = [11882,86122, 18239]
fracs = [28795,17057,11905,8992,6149,5865,1683, 1454, 1437, 1084, 679, 418, 296, 256, 52]
# explode=(0, 0.05, 0, 0)
explode=(0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0)


pie(fracs,  colors = colors ,explode=explode, labels=labels,
                autopct=my_autopct, shadow=False, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('Triangle Type Distribution')

show()