def sum_nums():
    max_num = int(input("数値を入力してください："))
    
    if max_num < 0:
        return None
    
    ret = 0
    for i in range(max_num + 1):
        ret += i
    
    return ret

print(sum_nums())
