
try:
    score=int(input("点数を入力してください:"))
    
except ValueError:
    print("エラー:数値を入力してください")
except:
    print("エラー:何かしらのエラーが発生しました")
else:
    if score >=60:
        print("合格です\nおめでとうございます")
finally:    
    print("処理を終了します")
    