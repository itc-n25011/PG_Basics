def decimal(b):

"""
この関数は、文字列を浮動小数点数に変換する。
その結果を出力してプログラムに返す。
例外処理として、NameErrorとValueErrorとValueの時にメッセージを出力してプログラム
に返す。

引数：
　b----必須引数
戻り値：
 result----引数を５でかけた（出力）結果
b = str("")
"""
    
    try:
        print("入力された文字　=",float(b))
        return b
    except ValueError:
        print("整数、または、少数点数を入力してください。")
b = str(5)
b = str("い")


