def computepay(h, r):
    p=h*r
    if h > 40:
        p = 40 * r + (h-40) * r *1.5
    return p

hour = int(input('Enter hours : '))
rate = float(input('Enter rate : '))
print('Pay : ', computepay(hour, rate)) #hour*rate
