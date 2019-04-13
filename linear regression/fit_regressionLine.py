from numpy import *
import matplotlib.pyplot as pt 
from mpl_toolkits.mplot3d import Axes3D


#for 2d plot 
#call   plot_2Dregression method with parameters  data points , b and m to fit the regression line and the scatter points 

#for 3D plot 
#call plot_3Dregression method



def plot_2Dregression(data,b,m):
	show_scatter_plot(data)
	show_regressionLine(data,b,m)
	pt.show()

def plot_3Dregression(data,a0,a1,a2):
	fig=pt.figure()
	ax=fig.add_subplot(111,projection='3d')
	show_scatter_3dplot(data,ax)
	show_3dregressionLine(data,a0,a1,a2,ax)
	pt.show()

########################################## 2D regression plot #####################

def show_scatter_plot(data):
	

	for i in range(len(data)):

		p=pt.scatter(data[i,0],data[i,1],color="RED")
		pt.xlabel('x-axis')
		pt.ylabel('y-axis')
		pt.title('This is the title of the data ')
	

def show_regressionLine(data,b,m):
     x1=[]
     y1=[]
     for i in range(len(data)):
     	x1.append(data[i,0])
     	y1.append(m*x1[i]+b)

     pt.plot(x1,y1)

#########################################################################################
######################################## 3D regression Plot ############################

def show_scatter_3dplot(data,ax):
	for i in range(len(data)):
		ax.scatter(data[i,1],data[i,2],data[i,3],color="RED")
	


def show_3dregressionLine(data,a0,a1,a2,ax):
	x1=[]
	x2=[]
	x3=[]

	for i in range(len(data)):
		x1.append(data[i,1])
		x2.append(data[i,2])
		x3.append(a0+a1*x1[i]+a2*x2[i])

	ax.plot(x1,x2,x3)
