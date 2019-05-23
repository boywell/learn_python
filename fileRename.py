# 文件批量增加后缀名
import os
import os.path
rootDir = "F:/my"
for file in os.listdir(rootDir):
    os.rename(os.path.join(rootDir,file),os.path.join(rootDir,file+'.mp4'))