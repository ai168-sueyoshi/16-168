"""文字列の変換に関するモジュール"""

def make_convert_pos(str_):
  """位置の文字列を局面の配列の座標に変換する関数

  Args:
    str_: 「position」コマンドの駒の位置。
      例:「7i6h」の「7i」の「7」はx座標、「i」はy座標。

  Returns:
    int: 局面の配列の座標のxかyの座標

  """
  if str_ == "9" or str_ == "a":
    output = 1
  elif str_ == "8" or str_ == "b":
    output = 2
  elif str_ == "7" or str_ == "c":
    output = 3
  elif str_ == "6" or str_ == "d":
    output = 4
  elif str_ == "5" or str_ == "e":
    output = 5
  elif str_ == "4" or str_ == "f":
    output = 6
  elif str_ == "3" or str_ == "g":
    output = 7
  elif str_ == "2" or str_ == "h":
    output = 8
  elif str_ == "1" or str_ == "i":
    output = 9

  elif str_ == "P":
    output = 0  # 持ち駒:x座標
  elif str_ == "L":
    output = 1
  elif str_ == "N":
    output = 2
  elif str_ == "S":
    output = 3
  elif str_ == "G":
    output = 4
  elif str_ == "B":
    output = 5
  elif str_ == "R":
    output = 6
  elif str_ == "*":
    output = 12  # とりあえず先手として持ち駒:y座標
  else:
    print("駒の位置の取得エラーです。")
  
  return output
