import edge_tts,os,time,pygame,datetime
from g4f.client import Client

client =Client()#初始化gpt服务

def text_generation(model="gpt-3.5-turbo",messages=[],temperature=0.7):
    completion = client.chat.completions.create(model=model,messages=messages,temperature=temperature,)
    return completion.choices[0].message.content

def mainTK():#程序主函数
    usrSK = str(input("请输入任意一句话:"))
    ChatFile.write("user:"+usrSK+"\n")
    print("服务器正在响应...若长时间无反应，按下Ctrl+c退出程序"+"\n")
    messages =[{'role':'usr','content':usrSK}]#发送数据
    AIoutput = text_generation(messages=messages)#获取数据
    print("AI:"+AIoutput+"\n")#输出
    ChatFile.write("AI:"+AIoutput+"\n")

    if isPlay == True:#是否进行转语音播放
        com = edge_tts.Communicate(text=AIoutput,voice='zh-CN-XiaoxiaoNeural',rate='+0%',volume='+0%',pitch='+0Hz')#使用文字转语音
        com.save_sync("speak.wav")#储存
        time.sleep(1)
        sound = pygame.mixer.Sound("speak.wav")  # 加载音乐
        sound.play()


if __name__ == '__main__':
    pygame.init() # 初始化混音器模块
    CheckExit = True
    isPlay = True
    os.system("clear")#一键清屏

    ChatFile = open('ChatLog.txt','w')
    ChatFile.write(str(datetime.datetime.now())+":"+"\n")

    openplay = input('是否使用文字转语音功能(关闭能够加快运行速率)[y/n]:')
    if openplay == "y":
        isPlay = True
    elif openplay == "n":
        isPlay = False
    else:
        isPlay = False

    while CheckExit:#主函数循环
        mainTK()

