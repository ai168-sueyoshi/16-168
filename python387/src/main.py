import sys
import engine_regist
import cmd_test_pos
import set_pos
import think_main
import pre_think
import mes
import convert_str

# 将棋所からの入力待ち。
# テストのための入力を省略する置き換え語句。
"""
a:usinewgame
s:position startpos
test-sente:テスト局面（いろは先手）をセット
test-sente:テスト局面（いろは後手）をセット
c:go b 思考開始
"""

while 1:
  # 将棋所からの入力データ
  input_str = input()

  # UIがエンジンを起動した時に最初に送るコマンド。
  # このコマンドを受信したらすぐにコマンドを返す。
  if input_str == "usi":
    # USIエンジン登録
    engine_regist.engine_registration()
  
  # quitを受信したらエンジンはすぐに終了する。
  if input_str == "quit":
    sys.exit()
  
  # isreadyを受信したら対局開始の準備をしてreadyokを返す。
  if input_str == "isready":
    print ("readyok")
  
  # 対局開始時にusinewgameを受け取る。これで対局開始。
  #「a」と入力しても「usinewgame」も同じ扱い。コマンドライン用。
  if input_str == "usinewgame" or input_str == "a":
    print(
        "テスト局面で動作確認する場合は、いろは先手「test-sente」、"\
        "いろは後手「test-gote」を入力してください。"
        )
    
  # 将棋所から思考開始局面を受け取る。
  #「s」と入力しても「position startpos」も同じ扱い。コマンドライン用。
  if input_str == "position startpos" or input_str == "s":
    if input_str == "s":
      # 局面のコマンドを格納する変数
      now_pos_str = "position startpos"
    else:
      now_pos_str = input_str
    # GUIからの局面のコマンドを解析して格納する配列
    cmd_lst = pre_think.new_cmd_analysis_lst(now_pos_str)
    # 平手startposの局面をセットした配列
    now_pos_lst = set_pos.new_startpos_lst()
    print("平手初期局面をセットしました。")
    mes.do_mes("局面表示")
    mes.do_mes("続きはc")
    # 盤上（左上からの座標）の例：[3][2]は8三を指す。
    #print("8三:" + now_pos_lst[3][2])
  elif "position startpos moves" in input_str:
    # 平手startposの局面をセットした配列
    now_pos_lst = set_pos.new_startpos_lst()
    # GUIからの局面のコマンドを格納する変数
    now_pos_str = input_str
    # GUIからの局面のコマンドを解析して格納する配列
    cmd_lst = pre_think.new_cmd_analysis_lst(now_pos_str)
    # 局面をセットした配列。
    now_pos_lst = set_pos.make_pos_lst(cmd_lst, now_pos_lst)
    print("コマンドから局面をセットしました。")
    mes.do_mes("局面表示")
    mes.do_mes("続きはc")

  # コマンド入力によって、テスト局面（いろは先手）をセットする。
  if input_str == "test-sente":
    input_str = cmd_test_pos.new_test_sente_pos_str()
    # 局面のコマンドを格納する変数
    now_pos_str = input_str
    # 局面をセットした配列。未着手。
    now_pos_lst = [""]

    print(input_str)
    print("テスト局面（いろは先手）をセットしました。")
    mes.do_mes("局面表示")
    mes.do_mes("続きはc")
  
  # コマンド入力によって、テスト局面（いろは後手）をセットする。
  if input_str == "test-gote":
    input_str = cmd_test_pos.new_test_gote_pos_str()
    # 局面のコマンドを格納する変数
    now_pos_str = input_str
    # 局面をセットした配列。未着手。
    now_pos_lst = [""]

    print(input_str)
    print("テスト局面（いろは後手）をセットしました。")
    mes.do_mes("局面表示")
    mes.do_mes("続きはc")
  
  # コマンド入力によって、テスト局面で思考させる。
  if input_str == "go btime" or input_str == "c":
    print("いろはが思考を開始します。")
    if input_str == "c":
      input_str = cmd_test_pos.new_think_start_test_str()
    
    # 局面を思考させる。
    #print(*now_pos_lst, sep='\n')
    #print("now_pos_str: " + now_pos_str)
    bestmove_str = think_main.create_thinking_main(now_pos_lst, now_pos_str)
    print(bestmove_str)

  # 局面を表示する。
  if input_str == "now":
    # 配列の中身を確認。２次元配列なので改行を使う。
    print(*now_pos_lst, sep='\n')
    mes.do_mes("駒の説明")

    # 手数の表示
    parsed_lst = pre_think.new_cmd_analysis_lst(now_pos_str)
    print("手数: " + str(pre_think.make_moves(parsed_lst)) )
