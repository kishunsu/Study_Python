notax_price=int(input("税抜き価格を入力してください:"))
tax_price=int(notax_price*1.08)


if tax_price>=2000:
    fare=0
else:
    fare=350
    print("送料として",fare,"かかります")

final_price=tax_price+fare
print("送料込みの価格は",final_price,"です。")
