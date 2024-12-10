square_area=lambda a:a*a
a=int(input("enter the nsize of sqre:"))
print("area of sqre =",square_area(a),"square")


rect_area=lambda l,b:l*b
l=int(input("enter the legth of rctangle"))
b=int(input("enter the bredth of rctangle"))
print("area of rect=",rect_area(l,b))

tri_area=lambda b,h:0.5 *b*h
b=int(input("enter the legth of tri"))
h=int(input("enter the bredth of tri"))
print("area of rect=",tri_area(b,h))
