import os
def startUI():
    os.system("clear")
    print(",------.,--.   ,--.,--------.       ,--.,--.\n|  .--. '\  `.'  / '--.  .--',--,--.|  ||  |,-.\n|  '--' | '.    /     |  |  ' ,-.  ||  ||     /  \n|  | --'    |  |      |  |  \ '-'  ||  ||  \  \  \n`--'        `--'      `--'   `--`--'`--'`--'`--' ")
    print("by MarkLiu07"+"\n"+"version:1.1.0")
    choose = int(input("请使用数字进行选择:\n[1]安装所需要的前置组件\n[2]进入pytalk主程序\n"))
    if choose == 2:
        print("正在打开...")
        os.system("python ptk.py")
        exit()
    elif choose ==1:
        os.system("python TKpre.py")
        exit()
    else:
        print("error!")

if __name__ == "__main__":
    startUI()
