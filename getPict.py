# 画像ファイルから画素をCの配列形式で出力する
# getPict.py 画像ファイル名 [縦ドット数=72]
# 実効ファイル形式にしてあれば getPict 画像ファイル名 [縦ドット数=72]
# (ファイルアイコンに画像ファイルをDrag and Dropでも可
# 画像は縦ドット数が指定の値になるよう伸縮される

from PIL import Image
import sys
import os
import math

def getPict( fname , fout=0, height=72):
    if os.path.exists(fname):
        inPic = Image.open(fname)
        outPic = inPic.resize((int(math.floor(inPic.height*inPic.width/height)),height))
        if isinstance(fout,str) :
            outFile = open(fout,'w')
        else:
            outFile = sys.stdout
        outFile.write('[][{}][3]{{\n'.format(height))
        for x in range(outPic.width):
            outFile.write('\t{ ')
            for y in range(outPic.height):
                p = outPic.getpixel((x,y))
                outFile.write('{{{},{},{}}}, '.format(p[0],p[1],p[2]))
            outFile.write('},\n')
        outFile.write('}\n')

if __name__ == '__main__':
    args = sys.argv
    print("{} {}".format(args[0],args[1]))
    try:
        if len(args) <= 2:
            n=os.path.splitext(args[0])[0].split('_')
            height=int(n[len(n)-1])
        else:
            height=int(args[2])
    except ValueError:
        height=72
    if os.path.exists(args[1]):
        fout=os.path.splitext(args[1])[0]+'.h'
        print("{},{},{}".format(args[1],fout,height))
        getPict(args[1],fout,height)
    else:
        print('Error: File not found.', file=sys.stderr)
