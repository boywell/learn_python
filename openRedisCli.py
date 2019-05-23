# coding = utf-8
# 使用python调用windows cmd
import os
if __name__ == '__main__':
    os.chdir("D:\\soft\\Redis-x64-3.2.100")
    os.system("redis-cli.exe -h 127.0.0.1 -p 6379")
