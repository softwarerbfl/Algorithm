dial=list(input())
time=len(dial)

for i in range(len(dial)):
    ascii=ord(dial[i])
    if(ascii>=65 and ascii<=67):
        time+=2
    elif(ascii>=68 and ascii<=70):
        time+=3
    elif(ascii>=71 and ascii<=73):
        time+=4
    elif(ascii>=74 and ascii<=76):
        time+=5
    elif(ascii>=77 and ascii<=79):
        time+=6
    elif(ascii>=80 and ascii<=83):
        time+=7
    elif(ascii>=84 and ascii<=86):
        time+=8
    elif(ascii>=87 and ascii<=90):
        time+=9
    else:
        time+=10
print(time)