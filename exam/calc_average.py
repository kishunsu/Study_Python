score=0
member=0
total=0
average=0
while True:
    score=int(input("点数を入力してください:"))
    
    if score==-1:
        break
    member+=1
    total+=score
    
average=total/member
print(member,"人のテストの平均点は",average,"点です")

    