"""単体テスト用"""

import sys
import engine_regist
import cmd_test_pos
import set_pos
import think_main
import pre_think
import mes
import convert_str

input = "position startpos moves P*8e N*3i 9g9f 8c8d 9f9e 8d8e"
#input = "position startpos"

# 局面を平手で設定する。
now_pos = set_pos.new_startpos_lst()

# コマンドを解析して配列に入れる
parsed_lst = pre_think.new_cmd_analysis_lst(input)

# コマンドから局面を変化させる。
output_lst = set_pos.make_pos_lst(parsed_lst, now_pos)

print(output_lst)

# 配列の中身を確認。２次元配列なので改行を使う。
#print(*output_lst, sep='\n')
