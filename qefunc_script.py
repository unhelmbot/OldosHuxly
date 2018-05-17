#-------------------------------------------------------------------------------
# Name:        qefunc_script
# Purpose:
#
# Author:       unhelmbot
#
# Created:     15.05.2018
# Copyright:   (c) unhelmbot
# Licence:     <no licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print('standard type of quadratic equation')
print('a+b+c=0')
print('Enter the qefunc() and her parametres')
def qefunc(x,b,c):

    dis=b*b-4*x*c
    print('Discriminant=',dis)
    if dis>0:
        dis=pow(dis, .5)
        print('Sqrt Discriminant=',dis)
        global x1,x2
        x1=-1*b-dis
        x1/=2*x
        x2=-1*b+dis
        x2/=2*x
        print('answer=')
        print('x1=',x1)
        print('x2=',x2)
    elif dis==0:
        xx=-1*b/2*x
        print('answer=',xx)
    elif   dis<0:
        print('No answer')
    else:
        print('Error 404')
    pass


