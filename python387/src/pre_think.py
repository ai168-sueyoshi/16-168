"""思考準備するモジュール"""

def new_cmd_analysis_lst(str_):
  """コマンド解析する関数

  Args:
    str_: USIプロトコルのコマンド
  
  Returns:
    lst: コマンドを区切り文字スペースで分割した配列
  
  """
  # 受け取ったコマンドを区切り文字スペースで分割した配列
  cmd_analysis_lst = str_.split()
  
  return cmd_analysis_lst

def make_turn_of_iroha(lst_):
  """いろはの手番（先手か後手）を返す関数

  Args:
    lst_: 「position」か「sfen」で始まるコマンドを分割した配列
  
  Returns:
    str: "先手" か "後手"の文字列
  
  Examples:
    「position startpos」は"先手"
    「position startpos moves 7i6h 3c3d」は"先手"
    「position startpos moves 2g2f」は"後手"
    「position startpos moves 2g2f 7a6b 2f2e」は"後手"

  """
  # 先手は、sfenではなく、トークンの数が2個か奇数のとき。
  if len(lst_) == 2 or len(lst_)%2 == 1:
    iroha_turn = "先手"
  else:
    iroha_turn = "後手"
  
  return iroha_turn

def make_moves(lst_):
  """手数を返す関数

  Args:
    lst_: 「position」か「sfen」で始まるコマンドを分割した配列
  
  Returns:
    int: 手数

  """
  if len(lst_) == 2:
    moves = 0  # 手数
  else:
    moves = len(lst_) - 3
  
  return moves

# 指し手生成する関数
# 戻り値：
# 指し手の配列
