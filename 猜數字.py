import randam
num=int(input('plz input a num'))
ans=random.randint(1,10)
if not num==ans:
    print('你猜錯了')
else:
    print('你猜對了')
    print('答案是'ans)