s="07:08:20PM"

s=s.split(":")
print(s)
h=int(s[0])
m=s[1]
suff=s[2]
s=suff[:2]
ampm=suff[2:]
print(s,' ',ampm,' ',suff,' ',m,' ',h)
if ampm=="PM":
    if h==12:
        h=0
    else:
        h=h+12
else:
    h=h
print(f"{h}:{m}")