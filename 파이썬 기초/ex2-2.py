#ex1-2 참조
def computepay(h,r) :
    if h > 40 :
        pay = 40*r + (h-40)*r*1.5
    else :
        pay = h*r
    return pay

hour = int(input('Enter hours : '))
rate = float(input('Enter rate : '))
print('Pay : ', computepay(hour, rate))
