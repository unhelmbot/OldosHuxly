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
    print('Discrement=',dis)
    if dis<0:
        print('No answer')
    if dis>0:
        global kvdis
        kvdis=pow(dis, .5)
        print('Sqrt discrement',kvdis)
    global x1,x2
    x1=-1*b-kvdis
    x1/=2*x
    x2=-1*b+kvdis
    x2/=2*x
    print('answer=',x1,x2)
    if dis==0:
        xx=-1*b/2*x
        print('answer=',xx)
    pass


