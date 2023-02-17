import numpy as np
L=12#length of beam in meters
w=10#intensity of load in KN/m

#Question a
#Bending moment(M) and shear force(V) at the first end, x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
m='The bending moment at x=0 is'
n='The shear force at x=0 is'
print('(a.1)' +m+('M')+'and',n+('V') )
#Bending moment(M) and shear force(V) at the first end, x=L=12
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
a=('The bending moment at x=L is')
b=('The shear force at x=L is')
print(('a.2')+a+('M')+('and'), b+('V'))

#Question b
("when the bending moment is zero, we get an expression x**2-L*x+L**2/6=0")
#from the expressiom
a=1
b=-L
c=L**2/6
#using the Almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print(('b The points of contra-flexure are {0} and {1}').format(root_1b,root_2b))

#Question c
("when the shear force is zero, x=L/2")
x=L/2
print(('c The point at which V=0 is {}').format(x))

#Question d
p=0
s=0.01
q=L+s
x=np.arange(p,q,s)
M=(w*(-6*x**2+6*L*x-L**2))/12
print(('d using the initialized variable, the bending moment at each step in the array is {0}').format(M))

#Question e
V=w*(L/2-x)
print(('e The shear force for each step along the span is {}').format(V))

#Question f
('let the absolute value of the bending moment array be  aM ')
('also let the minimum aM be m_aM')
('when the bending moment is m-aM, we get an expression x**2-L*x+(L**2/6)+(2*m_aM)/w=0')
AM=abs(M)
m_aM=min(AM)
#from the above equation
a=1
b=-L
c=(L**2/6)+(2*m_aM)/w
#using the Almigthy formula the two roots are;
discriminant=b**2-4*a*c
root_1f=(-b-np.sqrt(discriminant))/2*a
root_2f=(-b+np.sqrt(discriminant))/2*a
print(('f the point along L at which the absolute values of the bending moment array is minimum are {0} and {1} ').format(root_1f,root_2f))

#Question g
('let the relative errors be r_e')
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2b-root_2f)/root_2b*100)
print(('g the relative erros between estimated points of contra-flexure are {0}% and {1}%').format(r_e1,r_e2))

#Question h
('let the maximum bending moment be max_M and the minimum bending moment be min_M')
#for the minimum
min_M=min(M)
('When the bending moment is min_M, we get an expression x**2-l*x+(l**2/6)+(2*min_M)/w=0')
a=1
b=-L
c=(L**2/6)+(2*min_M)/w
#using the Almigthy formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print (('h.1 the points at which the minimum bending moment occur are {0} and {1}').format(root_1,root_2))
#for the maximum 
max_M=max(M)
('when the bending moment is max_M,we get an expression x**2-l*x+(L**2/6)+(2*max_M)/w=0')
a=1
b=-L 
c=(L**2/6)+(2*max_M)/w
#using the Almigthy formula the roots are;
discriminant=b**2-4*a*c
root_1=(-b-np.sqrt(discriminant))/2*a
root_2=(-b+np.sqrt(discriminant))/2*a
print(('h.2 the roots at which the maximum bending moment occur are {0} and {1}').format(root_1,root_2))  
       
#index number= 6948521
#github = https://github.com/Freda202
      
       