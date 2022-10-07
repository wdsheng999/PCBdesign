must_list=[2,2,1,2,2,2,3,2]
must=[86,86,84.5,82.7,88,96,75,87]
# print(len(must))
sum_must=0

for i in range(len(must)):
    print("loop:",i)
    print(sum_must)
    if(must[i]<60):
        sum_must=sum_must+0
    if(60<=must[i]<64):
        sum_must=sum_must+1*must_list[i]
    if(64<=must[i]<68):
        sum_must=sum_must+1.5*must_list[i]
    if(68<=must[i]<72):
        sum_must=sum_must+2*must_list[i]
    if(72<=must[i]<75):
        sum_must=sum_must+2.3*must_list[i]
    if(75<=must[i]<78):
        sum_must=sum_must+2.7*must_list[i]
    if(78<=must[i]<82):
        sum_must=sum_must+3*must_list[i]
    if(82<=must[i]<85):
        sum_must=sum_must+3.3*must_list[i]
    if(85<=must[i]<90):
        sum_must=sum_must+3.7*must_list[i]
    if(90<=must[i]):
        sum_must=sum_must+4*must_list[i]
    else:
        print("illegal!please check\n")


choose=[4,3,2,4,4]
sum_choose=sum(choose)/5
print(sum_choose)

sum_must=sum_must/sum(must_list)

print(sum_must)

gpa=sum_choose*0.35+sum_must*0.65
print(gpa)
print("score:",gpa*25)








