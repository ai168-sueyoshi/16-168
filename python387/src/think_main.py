"""局面を思考するモジュール"""

import pre_think

def create_thinking_main(lst_, str_):
  """局面を思考するメイン関数

  Args:
    lst_: 現在の局面の配列
    str_: USIプロトコルの「position startpos」で始まるコマンドの文字列

  Returns:
    str: 指し手（bestmove）のコマンドの文字列

  """
  # 受け取ったコマンドを解析して格納する配列
  parsed_lst = pre_think.new_cmd_analysis_lst(str_)
  
  # 手数の表示
  print("手数: " + str(pre_think.make_moves(parsed_lst)) )

  # いろはが先手か後手かを格納する変数
  iroha_turn = pre_think.make_turn_of_iroha(parsed_lst)
  print("いろはの手番: " + iroha_turn)

  # 仮の戻り値
  return "bestmove 7g7f"
