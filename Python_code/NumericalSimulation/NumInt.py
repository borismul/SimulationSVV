#Numerical integration of a function described by arrays x and y between x-coordinates a and b
def NumInt(x,y,a,b):
    total = 0
#check if inputted boundries a & b are within the function defined by x & y
    if b>x[-1] or a<x[0]: raise IOError('boundaries (a and/or b) out of range')
#find in between which x-coordinates described in array x a and b lie  
    i=0
    while x[i]<=a: i+=1
    j=len(x)-1
    while x[j]>=b: j-=1
#find the part of the slice in x from the left boundary to a and b
    part_begin = (a-x[i-1])/(x[i]-x[i-1])
    part_end = (b-x[j])/(x[j+1]-x[j])
#find the y value at a and b by linear interpoation
    y_begin = y[i-1]+(y[i]-y[i-1])*part_begin
    y_end = y[j]+(y[j]-y[j+1])*part_end
#add the parts of the first and last slices of the function to the final answer
    total += (1-part_begin)*(x[i]-x[i-1])*((y_begin+y[i])/2)
    total += part_end*(x[j+1]-x[j])*((y_end+y[j])/2)
#add the rest of the slices of the function to the final answer
    count = i;
    while count<=j-1 and count>=i:
        total += (x[count+1]-x[count])*((y[count]+y[count+1])/2)
        count += 1 
    return total

#test module
x = range(0,10)
y = [1,1,1,1,1,1,1,1,1,1]
a = 0
b = 9
if NumInt(x,y,a,b) != b-a: raise IOError('answer not valid')