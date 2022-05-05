# Versawriter_Prototype Picture to Data converter
## Helper tool for Hand-held Versawriter
This is helper tool for Versa Writer using M5Atom matrix or M5Stick-C ( https://github.com/thorv/Versawriter_main )  
Picture to Data (C array) converter by Python3  
    Use Pillow library
## overview
It is a data conversion tool for displaying images on the Versa Writer.  
After normalizing the specified image file to 72 pixels vertically by default, it is converted to a text file in C array format in which each pixel is arranged and output.
It depends on how Python is installed, but usually as a startup command  
`python getPict.py image file name [vertical size]`  
It will be. The vertical size is 72 if omitted. If Python is properly installed, you should be able to handle it by dragging and dropping the image file to the getPict.py icon.

The output generates text in the following format with the file name of [Image file name body.h]. For example, if the image file is pic.png, the output file name will be pic.h
```
[] [72] [3] {
    {{R, G, B}, {R, G, B}, ... / * 72 pixels * /},
    // Data of the number of screen widths
}
```
In the source code of the Versa Writer, if the image file name is pic.png and the image array name used in the program is picArray, you can import the image data by writing as follows.
```
char picArray
#include "pic.h"
;
```

## 概要
バーサライタで画像を表示するためのデータ作成ツールです。
指定された画像ファイルを、デフォルトでは縦72ピクセルに正規化した後、各画素に展開したCの配列形式のテキストファイルに変換し、出力します。画像データのフォーマットは、PythonのPillowライブラリの対応フォーマットに依存します。  
Pythonのインストールの仕方にもよりますが、起動コマンドとしては  
`python getPict.py 画像ファイル名 [縦サイズ]`  
となります。縦サイズは省略された場合は72になります。Pythonが適切にインストールされていれば、getPict.pyのアイコンに画像ファイルをDrag & Dropすることでも処理ができるはずです。

出力は、以下の形式のテキストを、[画像ファイル名本体.h] のファイル名で生成します。例えば、画像ファイルがpic.pngであったなら、出力ファイル名はpic.hとなります
```
[][72][3]{
    { {R,G,B}, {R,G,B}, .../* 72 pixels */},
    // Data of the number of screen widths
}
```
バーサライタのソースコード側では、画像ファイル名がpic.png, プログラムで使用する画像配列名をpicArrayとした場合、以下のように記述することで画像データを取り込むことができます。
```
char picArray
#include "pic.h"
;
```
