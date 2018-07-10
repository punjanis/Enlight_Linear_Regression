from statistics import mean
import numpy as np
import matplotlib.pyplot as plt


xs = np.array([1,2,3,4,5,6])
ys = np.array([5,4,6,5,6,7])

def best_fit_slope_and_intercept (xs,ys):
	m = ( (mean(xs) * mean(ys)) - mean(xs*ys) )  / ( mean(xs)*mean(xs) - mean(xs*xs) )  
	
	b = mean(ys) - m*mean(xs)

	return m, b

def squared_error(ys_original, ys_line):
	return sum ((ys_line-ys_original)**2)

def coef_determination(ys_original, ys_line):
	y_mean_line = [mean(ys_original) for y in ys_original]
	squared_error_regr = squared_error(ys_original, ys_line)
	squared_error_y_mean = squared_error(ys_original, y_mean_line)
	return 1 - (squared_error_regr/squared_error_y_mean)


m, b = best_fit_slope_and_intercept(xs,ys)

regression_line = [(m*x)+b for x in xs]

print (m,b)

predict_x = 8
predict_y = (m*predict_x)+b

rsquared = coef_determination(ys, regression_line)
print (rsquared)

plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()


