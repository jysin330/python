sub1=int(input("enter your english marks1:"))
sub2=int(input("enter your maths marks2:"))
sub3=int(input("enter your hindi marks3:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject")
elif((sub1+sub2+sub3)/3<40):
    print("you are fail due to total percentage less than 40")
else:
     print("congratulation! you passed the exam")