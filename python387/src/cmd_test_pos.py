"""テスト局面をUSIプロトコルのコマンドで返すモジュール"""

def new_test_sente_pos_str():
  """テスト局面（いろは先手）をセットする関数

  Args: なし。

  Returns:
    str: テスト局面（いろは先手）のコマンド
  
  """
  return "position startpos moves"\
    " 2g2f 5a5b 9i9h 8b6b 8g8f 6b8b 2h7h 2c2d 2f2e"\
    " 7a6b 9g9f 6b5a 9h9g 4a3b 8f8e 6a7b 7h2h 3a4b"\
    " 6g6f 6c6d 6f6e 7b6c 6e6d 2b3a 2h7h 9c9d 8e8d"\
    " 9a9c 8d8c+ 5b4a 6i5h 6c6b 8c7c 8b9b 7c8c 5a5b"\
    " 6d6c+ 2d2e P*2f 1a1b 8c9c 6b6a P*6b P*8f L*7f"\
    " 6a7a P*8b 8a7c 6c7c 5b6a 6b6a+ 7a8a 8b8a+ 4a5b"\
    " G*4a 3b2b"

def new_test_gote_pos_str():
  """テスト局面（いろは後手）をセットする関数

  Args: なし。

  Returns:
    str: テスト局面（いろは後手）のコマンド
  """
  return "position startpos moves"\
    " 2g2f 5a5b 9i9h 8b6b 8g8f 6b8b 2h7h 2c2d 2f2e 7a6b"\
    " 9g9f 6b5a 9h9g 4a3b 8f8e 6a7b 7h2h 3a4b 6g6f 6c6d"\
    " 6f6e 7b6c 6e6d 2b3a 2h7h 9c9d 8e8d 9a9c 8d8c+ 5b4a"\
    " 6i5h 6c6b 8c7c 8b9b 7c8c 5a5b 6d6c+ 2d2e P*2f 1a1b"\
    " 8c9c 6b6a P*6b P*8f L*7f"
  
def new_think_start_test_str():
  """テスト局面の対局時間を設定して試行を開始させる関数

  Args: なし。

  Returns:
    str: 先手、後手の設定時間をセットして思考を開始させるコマンド
    
  """
  return "go btime 60000 wtime 60000 byoyomi 10000"
