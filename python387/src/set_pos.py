"""局面をセットした配列を返すモジュール"""

import convert_str

def new_startpos_lst():
  """平手をセットする関数

  大文字: 先手 / 小文字: 後手
  W: 壁（侵入できない場所）
  スペース: 駒なし
  p歩、l香、n桂、s銀、g金、b角、r飛、k王
  成駒は、アルファベットの次の文字。竜だけd（Dragonのd）
  cと、y杏、a成（成り桂）、f全、o馬、e竜

  Args: なし。

  Returns:
    lst: 平手をセットした2次元配列

  """
  startpos_lst = [
    # startpos_lst[縦y][横x] ※x,yの順番に注意。
    ["W","W","W","W","W","W","W","W","W","W","W"],  # y:0
    ["W","l","n","s","g","k","g","s","n","l","W"],  # y:1
    ["W"," ","r"," "," "," "," "," ","b"," ","W"],  # y:2
    ["W","p","p","p","p","p","p","p","p","p","W"],  # y:3
    ["W"," "," "," "," "," "," "," "," "," ","W"],  # y:4
    ["W"," "," "," "," "," "," "," "," "," ","W"],  # y:5
    ["W"," "," "," "," "," "," "," "," "," ","W"],  # y:6
    ["W","P","P","P","P","P","P","P","P","P","W"],  # y:7
    ["W"," ","B"," "," "," "," "," ","R"," ","W"],  # y:8
    ["W","L","N","S","G","K","G","S","N","L","W"],  # y:9
    ["W","W","W","W","W","W","W","W","W","W","W"],  # y:10
    ["先手の持ち駒","P","L","N","S","G","B","R"],  # y:11
    [               0 , 0 , 0 , 0 , 0 , 0 , 0 ],  # y:12
    ["後手の持ち駒","p","l","n","s","g","b","r"],  # y:13
    [               0 , 0 , 0 , 0 , 0 , 0 , 0 ],  # y:14
  ]
  return startpos_lst

def make_pos_lst(lst_, pos_lst_):
  """コマンドから局面を変化させる関数

  大文字: 先手 / 小文字: 後手
  W: 壁（侵入できない場所）
  スペース: 駒なし
  p歩、l香、n桂、s銀、g金、b角、r飛、k王
  成駒は、アルファベット順（ループ）で13個後ろの文字。
  cと、y杏、a成（成り桂）、f全、o馬、e竜
  
  Args: 
    lst_: 「position」か「sfen」で始まるコマンドを分割した配列
    pos_lst_: 受け取った局面の2次元配列

  Returns:
    lst: コマンドで変化させた局面の2次元配列

  """
  if len(lst_) == 2:
    # 「position startpos」なら要素を空っぽにする。
    lst_.clear()
  else:
    # 「position startpos moves」ならmovesまで要素を削除する。
    del lst_[0:3]
  
  # 平手の局面から変化させていく
  # 何手目か
  for moves in range(len(lst_)):
    # lst_[0]は1手目のコマンド
    target_str = lst_[moves]
    # 手番
    if moves%2 == 1:
      turn = "先手"
    else:
      turn = "後手"
    # 動かす駒の位置 例:「7i6h+」のときは["7","i"]
    before_pos = [target_str[:1], target_str[1:2]]
    # 駒を動かす先の位置 例:「7i6h+」のときは["6","h"]
    after_pos = [target_str[2:3], target_str[3:4]]
    
    # 動かす駒の位置から、局面の配置の座標に変換する。
    before_x_int = convert_str.make_convert_pos(before_pos[0])
    # 駒を打つとき。例「P*6h」
    if before_pos[1] == "*":
      before_y_int = 12
      if turn == "後手":
        # 大文字を小文字（後手の駒）に変換する。
        before_pos[0] = str.swapcase(before_pos[0])
        before_y_int = 14
      #print("動かす駒: " + before_pos[0])
      # 動かす駒の種類を格納する。
      move_piece = before_pos[0]
    else:
      before_y_int = convert_str.make_convert_pos(before_pos[1])
      #print("動かす駒: " + pos_lst_[before_y_int][before_x_int])
      # 動かす駒の種類を格納する。
      move_piece = pos_lst_[before_y_int][before_x_int]
    # 動かす駒を成らせる。 例: target_str = "1c1b+"
    if len(target_str) == 5:  
      if move_piece == "P":  # 先手の歩
        move_piece = "C"
      elif move_piece == "L":  # 先手の香
        move_piece = "Y"
      elif move_piece == "N":  # 先手の桂
        move_piece = "A"
      elif move_piece == "S":  # 先手の銀
        move_piece = "F"
      elif move_piece == "B":  # 先手の角
        move_piece = "O"
      elif move_piece == "R":  # 先手の飛
        move_piece = "E"
      elif move_piece == "p":  # 先手の歩
        move_piece = "c"
      elif move_piece == "l":  # 後手の香
        move_piece = "y"
      elif move_piece == "n":  # 後手の桂
        move_piece = "a"
      elif move_piece == "s":  # 後手の銀
        move_piece = "f"
      elif move_piece == "b":  # 後手の角
        move_piece = "o"
      elif move_piece == "r":  # 後手の飛
        move_piece = "e"
      else:
        print("成りの変換エラーです。")

    # 動かした後の局面の配列の処理
    # 駒を打つとき。例「P*6h」
    if before_pos[1] == "*":
      # 持ち駒の数を減らす
      pos_lst_[before_y_int][before_x_int] += -1
    else:
      # 打たないときは、動く前の位置の駒の種類を空っぽにする。
      pos_lst_[before_y_int][before_x_int] = " "

    # 駒を動かす先の位置から、局面の配置の座標に変換する。
    after_x_int = convert_str.make_convert_pos(after_pos[0])
    after_y_int = convert_str.make_convert_pos(after_pos[1])
    # 取る駒の種類を格納する。
    get_piece = pos_lst_[after_y_int][after_x_int]
    #print("取る駒: " + get_piece)
    # 駒を置く。
    pos_lst_[after_y_int][after_x_int] = move_piece
    # 取った駒を局面に置く。
    if get_piece == "P" or get_piece == "C":  # 先手の歩と
      pos_lst_[14][0] += 1
    elif get_piece == "L" or get_piece == "Y":  # 先手の香杏
      pos_lst_[14][1] += 1
    elif get_piece == "N" or get_piece == "A":  # 先手の桂成
      pos_lst_[14][2] += 1
    elif get_piece == "S" or get_piece == "F":  # 先手の銀全
      pos_lst_[14][3] += 1
    elif get_piece == "G":  # 先手の金
      pos_lst_[14][4] += 1
    elif get_piece == "B" or get_piece == "O":  # 先手の角馬
      pos_lst_[14][5] += 1
    elif get_piece == "R" or get_piece == "E":  # 先手の飛竜
      pos_lst_[14][6] += 1
    elif get_piece == "p" or get_piece == "c":  # 後手の歩と
      pos_lst_[12][0] += 1
    elif get_piece == "l" or get_piece == "y":  # 後手の香杏
      pos_lst_[12][1] += 1
    elif get_piece == "n" or get_piece == "a":  # 後手の桂成
      pos_lst_[12][2] += 1
    elif get_piece == "s" or get_piece == "f":  # 後手の銀全
      pos_lst_[12][3] += 1
    elif get_piece == "g":  # 後手の金
      pos_lst_[12][4] += 1
    elif get_piece == "b" or get_piece == "o":  # 後手の角馬
      pos_lst_[12][5] += 1
    elif get_piece == "r" or get_piece == "e":  # 後手の飛竜
      pos_lst_[12][6] += 1
    elif get_piece == " ":  # 取る駒がない
      pass
    else:
      print("駒の位置の取得エラーです。")
    
    print("moves: " + str(moves))
    print("target_str: " + target_str)
    #print(*pos_lst_, sep='\n')

  return pos_lst_
