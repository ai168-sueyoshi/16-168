import sys
import engine_registration

# 将棋所からデータを受け取る
while 1:
  # 将棋所から受け取るデータ
  inputStr = input()

  # UIがエンジンを起動した時に最初に送るコマンド。
  # このコマンドを受信したらすぐにidコマンドを返す。
  if inputStr == "usi":
    # USIエンジン登録
    engine_registration.usiEngineRegistration()
  
  # これを受信したらエンジンはすぐに終了する。
  if inputStr == "quit":
    sys.exit()
