def timeConversion(s):
    t=s.split(':')
    h=int(t[0])
    m=int(t[1])
    x=t[2]
    s=x[:2]
    ampm=x[2:]
    if ampm=='PM':
        if h==12:
            h=0
        else:
            h=h+12
    else:
        h=h

    print(f'{h}:{m}:{s}')
if __name__ == '__main__':
   

    s = input()

    result = timeConversion(s)

    
