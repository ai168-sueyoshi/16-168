"""局面をセットした配列を返すモジュール"""

def new_startpos_lst():
  """平手をセットする関数

  ^:先手
  v:後手
  W:壁（侵入できない場所）

  Args: なし。

  Returns:
    lst: 平手をセットした配列

  """
  startpos_lst = [
    ["W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ],
    ["W" ,"Lv","Nv","Sv","Gv","Kv","Gv","Sv","Nv","Lv","W" ],
    ["W" ,""  ,"Rv",""  ,""  ,""  ,""  ,""  ,"Bv",""  ,"W" ],
    ["W" ,"Pv","Pv","Pv","Pv","Pv","Pv","Pv","Pv","Pv","W" ],
    ["W" ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,"W" ],
    ["W" ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,"W" ],
    ["W" ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,""  ,"W" ],
    ["W" ,"P^","P^","P^","P^","P^","P^","P^","P^","P^","W" ],
    ["W" ,""  ,"B^",""  ,""  ,""  ,""  ,""  ,"R^",""  ,"W" ],
    ["W" ,"L^","N^","S^","G^","K^","G^","S^","N^","L^","W" ],
    ["W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ,"W" ]
  ]
  return startpos_lst