char_count={}
char_list=[]
char_list_input=[]
count=0
char_count=dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"),0)

while True:
    char_list_input=input("英単語を入力してください:")
    if char_list_input=="":
        break

#辞書に登場した単語の数を代入する
    for key in char_count.keys():
        if f"{key}" in char_list_input:
            count=char_list_input.count(f"{key}")
            char_count[f"{key}"]+=count
        else:
            continue
    char_list.append(char_list_input)

#1文字以上あった文字すべてについて表示する    
char_list.sort()
print("入力した英単語:",char_list)
for key,value in char_count.items():
    if value >0:
        print(f"{key}:{value}")
    else:
        continue
        