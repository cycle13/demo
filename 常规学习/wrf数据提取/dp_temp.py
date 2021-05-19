import math


def temp2dptemp(t,u):
    ew = math.pow(10,
                  10.79574*(1-273.16/(273.15+t))-
                  5.028*math.log(((273.15+t)/273.16),10)+
                  1.50475*math.pow(10,-4)*
                  (1-math.pow(10,-8.2969*((273.15+t)/273.16-1)))+
                  0.42873*math.pow(10,-3)*
                  (math.pow(10,4.76955*(1-273.16/(273.15+t)))-1)+
                  0.78614
    )
    e = u*ew/100
    td = (243.92*(math.log(e/6.1078,10))/(7.69-math.log(e/6.1078,10)))
    return td



def temp2dptempp(t,rh):
    a = 6.11
    b = 17.67
    c = 257.14
    d = 234.5
    ym = math.log(rh * math.exp((b - (t / d)) * (t / (c + t))) / 100, math.e)
    bhsq = a * math.exp((b - (t / d)) * (t / (c + t)))
    tdp = (c * ym) / (b - ym)
    return tdp


def calrh(q,t,h):
    rh = (q*h*1000)/((0.662+0.378*q)*6.112*math.pow(math.e,(17.67*t)/(t+243.4)))
    return rh


calrh(0.00386,6.1069,91.82384)
# temp2dptemp(20,100)
# print(temp2dptempp(-20,100))
