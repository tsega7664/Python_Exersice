import math
def calc_paint_area(height,width,cover):
    numOfCans = math.ceil((height*width)/cover)
    print(f"You will need {numOfCans} cans of paint.")
test_h = int(input("Height of wall:\t"))
test_w = int(input("Width of wall:\t"))
test_cover = int(input("Area of cover:\t"))
calc_paint_area(height=test_h,width=test_w,cover= test_cover)
