"""
この関数は、整数を引数として受け取り、その整数を2で割る。
その結果を出力してプログラムに返す。

引数:
    x----必須引数
戻り値:
   result----引数を2で割った　(出力）結果
"""

def division(x):

  result = x / 2 #入力値を2で割る
  print("入力された整数を２で割った結果=", int(result))
  return result
def multiplication(y):


"""
この関数は、整数を引数として受け取り、その整数を４でかける。
その結果を出力してプログラムに返す。
引数:
 b----必須引数
戻り値:
 result---引数を４でかけた(出力)結果
"""


  result = y * 3 #入力値を3でかける
  print("入力された整数を3でかけた結果=", int(result))
  return result

x = 6
y = division(x)
multiplication(y)


  


