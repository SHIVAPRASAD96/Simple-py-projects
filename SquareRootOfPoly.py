import sys

import math

#Pogram to find Discrement of the quadraatic Equation and find its roots

print("Enter Values of a , b and c");

print("Enter a");

a = int(input());

print("Enter b");

b = int(input());

print("Enter c");

c = int(input());

d = b * b - 4 * a * c ;
  
if d<0 :

    print("The Values are imaginary \n");
    
elif d==0:

    print("The disc==0 so only one root\n",b/(2*a));

else  :

    disc = math.sqrt(d);

    x = (b-disc)/(2*a);
    
    print("The first root is\n", x);

    x = (b+disc)/(2*a);

    print("The Second Root is\n",x);














    
    
