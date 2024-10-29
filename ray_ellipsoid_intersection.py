# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z

#  Text explaining script usage

# Parameters:
# d_l_x: x-coordinate of origin-referenced ray unit vector
# d_l_y: y-coordinate of origin-referenced ray unit vector
# d_l_z: z-coordinate of origin-referenced ray unit vector
# c_l_x: x-coordiante of the ray origin offset
# c_l_y: y-coordiante of the ray origin offset
# c_l_z: z-coordiante of the ray origin offset


# Output:
#  print the x,y, and z coordiantes of teh interesection if it exists 
#
# Written by Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
e_E = 0.081819221456

# helper functions

## vector magnitude
def mag(v):
    sum_of_squares = 0.0 
    for i in range(0,len(v)):
        sum_of_squares += v[i] * v[i]
    return math.sqrt(sum_of_squares)

## scalar multiplication
def smul(s,v):
    sprod=[]
    for i in range(0,len(v)):
        sprod.append(s*v[i])
    return sprod
#   return [s*e for e in v]

## vector addition
def add(v1,v2):
    if len(v1) != len(v2):
        return None
    else:
        v3=[]
        for i in range(0,len(v1)):
            v3.append(v1[i]+v2[i])
        return v3
    
## vector subtraction
def sub(v1,v2):
    if len(v1) != len(v2):
        return None
    else:
        v3=[]
        for i in range(0,len(v1)):
            v3.append(v1[i]-v2[i])
        return v3
    
## dot product 
def dot(v1,v2):
    if len(v1) != len(v2):
        return float('nan')
    else:
        dp=0.0
        for i in range(0,len(v1)):
            dp += v1[i] * v2[i]
        return dp


# initialize script arguments
d_l_x= float('nan')
d_l_y= float('nan')
d_l_z= float('nan')
c_l_x= float('nan')
c_l_y= float('nan')
c_l_z= float('nan')


# parse script arguments
if len(sys.argv)==7:
    d_l_x= float(sys.argv[1])
    d_l_y= float(sys.argv[2])
    d_l_z= float(sys.argv[3])
    c_l_x= float(sys.argv[4])
    c_l_y= float(sys.argv[5])
    c_l_z= float(sys.argv[6])
    
else:
    print(\
     'Usage: '\
     'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z '
   )
    exit()

# write script below this line

## setup vectors
d_l=[d_l_x, d_l_y,d_l_z]
c_l=[c_l_x, c_l_y,c_l_z]


## discriminant

a=d_l_x**2 + d_l_y**2 + (d_l_z**2/(1-(e_E**2)))
b= 2.0*(d_l_x*c_l_x + d_l_y*c_l_y + (d_l_z*c_l_z)/((1-(e_E**2))))
c= c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1-(e_E**2)) - R_E_KM**2
discr=b*b-4.0*a*c

## solution logic
if discr>=0.0:
    d= (-b-math.sqrt(discr))/(2*a)
    if d<0.0:
        d= (-b+math.sqrt(discr))/(2*a)
    if d>= 0.0:
        l_d = add(smul(d,d_l),c_l)
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])

