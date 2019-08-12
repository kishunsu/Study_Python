# 九九のリストを作成する
list_outer = []

for x in range(1,10):
        list_inner = []
        
        for y in range(1,10):
                list_inner.append(x * y)
        
        list_outer.append(list_inner)

# 九九の表を表示する
for v in range(9):
    for h in range(9):
        print(f"{list_outer[v][h]:3d}", end="")
    
    print("")