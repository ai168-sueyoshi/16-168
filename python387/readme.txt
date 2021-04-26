**超軽量、超高速な配布用Python「embeddable python」 - Qiita**
https://qiita.com/mm_sys/items/1fd3a50a930dac3db299

最小構成
pythonNN.dll、pythonNN.zip、vcruntime140.dllがあればPythonは動作します。
python.exeは、pythonNN.dllへ引数を送るだけの実行ファイルですので、独自C++に組み込むときは必要ありません。
(pythonNN.zipは圧縮ファイルですが、このままで機能しますので解凍してはいけません。 フォルダ名さえ気をつけていれば解凍しても使えます。詳しくは下部の「エラー対応」項目を参照)

今回は他の構成ファイルを使うのでそのままにしておいてください。