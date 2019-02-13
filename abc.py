y=int(input("请输入年："))
if(y%400==0) or (y%4==0 and y%100!=0): 
    print(y,'是闰年')
else:
    print(y,'不是闰年')