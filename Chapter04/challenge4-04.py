def division(x):

    """
    この関数は、整数を引数として受け取り、その整数を4で割る。
　 その結果を出力してプログラムに返す。
    
    引数：
　　a  ----- 必須引数
    戻り値：
　　result ---- 引数を4で割った（出力）結果
    """

    result = x / 4    # 入力値を4で割る
    print("入力された整数を2で割った結果＝", int(result))
    return result

def multiplication(y):
    """
    この関数は、整数を引数として受け取り、その整数を3でかける。
　 その結果を出力してプログラムに返す。
    
    引数：
　　b  ----- 必須引数
    戻り値：
　　result ---- 引数を3でかけた（出力）結果
    """

    result = y * 3    # 入力値を3でかける
    print("入力された整数を3でかけた結果＝", int(result))
    return result
    
x = 9
y = division(x)
multiplication(y)



  


