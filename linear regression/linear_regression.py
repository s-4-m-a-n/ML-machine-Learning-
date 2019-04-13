from numpy import *
import fit_regressionLine as show

#regression line to fit y=mx+b

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))



def step_gradient(b,m,data,learning_rate):
	current_b=b
	current_m=m
	b_gradient=0
	m_gradient=0
	point=data
	R=learning_rate
	N=len(data)
	for i in range(0,N):
		x=data[i,0]
		y=data[i,1]

		b_gradient +=(current_m*x+current_b)-y
		m_gradient+=((current_m*x+current_b)-y)*x

	new_b=current_b-R*(1/N*b_gradient)
	new_m=current_m-R*(1/N*m_gradient)
	
	return [new_b,new_m]




def gradient_Descent(data,starting_b,starting_m,learning_rate,iteration):
	b=starting_b
	m=starting_m
	for i in range(iteration):
		b,m=step_gradient(b,m,data,learning_rate)

		print(f"b={b} and m={m}")

	return [b,m]




def run():
	points=genfromtxt('data.csv',delimiter=',')
	initial_b=0.00
	initial_m=0.00
	learning_rate=0.0001
	num_iteration=10000

	[b,m]=gradient_Descent(points,initial_b,initial_m,learning_rate,num_iteration)

	print(f"b={b}and m={m}")

	show.plot_2Dregression(points,b,m)

	print(f"{compute_error_for_line_given_points(b, m, points)}")



if __name__ == "__main__":
	run()