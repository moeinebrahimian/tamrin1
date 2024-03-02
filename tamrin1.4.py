p1=float(input("ente your weight(kg): "))
p2=float(input("enter your hight(m):"))
x1=p1/p2**2
if x1<18.5:
    print(x1)
    print("you are under weight")
elif 18.5<=x1<=24.9:
    print(x1)
    print("you are normal")
elif 25<=x1<=29.9:
    print(x1)
    print("you are over weight")
elif 30<=x1<=34.9:
    print(x1)
    print("you are obesity")
elif 35<=x1<=39.9:
    print(x1)
    print("you are extrme obesity")