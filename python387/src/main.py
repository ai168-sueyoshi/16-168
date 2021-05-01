import sys
import engine_registration
import cmd_test_position
import arr_position

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
  inputStr = input()

  # UIがエンジンを起動した時に最初に送るコマンド。
  # このコマンドを受信したらすぐにコマンドを返す。
  if inputStr == "usi":
    # USIエンジン登録
    engine_registration.usiEngineRegistration()
  
  # quitを受信したらエンジンはすぐに終了する。
  if inputStr == "quit":
    sys.exit()
  
  # isreadyを受信したら対局開始の準備をしてreadyokを返す。
  if inputStr == "isready":
    print ("readyok")
  
  # 対局開始時にusinewgameを受け取る。これで対局開始。
  #「a」と入力しても「usinewgame」も同じ扱い。コマンドライン用。
  if inputStr == "usinewgame" or inputStr == "a":
    print(
        "テスト局面で動作確認する場合は、いろは先手「test-sente」、"\
        "いろは後手「test-gote」を入力してください。"
        )
    
  # 将棋所から思考開始局面を受け取る。
  #「s」と入力しても「position startpos」も同じ扱い。コマンドライン用。
  if inputStr == "position startpos" or inputStr == "s":
    # 局面をセットした配列
    arrNowPosition = arr_position.arrStartpos()
    print("平手初期局面をセットしました。")
    # 配列の中身を確認。２次元配列なので改行を使う。
    #print(*arrNowPosition, sep='\n')
    # 盤上（左上からの座標）の例：[3][2]は8三を指す。
    #print("8三:"+arrNowPosition[3][2])
    
  # コマンド入力によって、テスト局面（いろは先手）をセットする。
  if inputStr == "test-sente":
    inputStr = cmd_test_position.setTestSentePosition()
    print(inputStr)
    print("テスト局面（いろは先手）をセットしました。"\
      "続きは「c」を入力してください。")
  
  # コマンド入力によって、テスト局面（いろは後手）をセットする。
  if inputStr == "test-gote":
    inputStr = cmd_test_position.setTestGotePosition()
    print(inputStr)
    print("テスト局面（いろは後手）をセットしました。"\
      "続きは「c」を入力してください。")
  
  # コマンド入力によって、テスト局面で思考させる。
  if inputStr == "go btime" or inputStr == "c":
    print("いろはが思考を開始します。")
    if inputStr == "c":
      inputStr = cmd_test_position.setTestTime()
  
  # 局面を表示する。作成中。


