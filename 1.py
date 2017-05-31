# -*- coding:utf-8 -*-

import re

class ReplyTextProcess(object):

    @staticmethod
    def convertToRex(text):
        # text = re.escape(text)
        return re.compile(text)

    def get_text(self, file):
        reply_hash = {}

        from readxlsx import ReplyText
        items = ReplyText(file).get_allrows()
        for item in items:
            key = self.convertToRex(item[0])
            value = item[1]
            reply_hash[key] = value

        self.reply_dict = reply_hash

    def search(self, text):
        for key, value in self.reply_dict.items():
            match = key.search(text)
            if match:
                return value


reply = ReplyTextProcess()
reply.get_text("雅思资料.xlsx")
result = reply.search('有没有刘薇密码')
print(result)


#--------------------------------机器人操作逻辑-----------------------------------------------------
#--------------------------------机器人操作逻辑-----------------------------------------------------
#--------------------------------机器人操作逻辑-----------------------------------------------------


from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

@bot.register(chats=User, msg_types=PICTURE)
def process_img(msg):
    """
    处理图片内容
    """
    msg.reply("鸭哥收到一张图片，但是不知道是什么意思，待主人回来后回复你. 文件名为:%s" % msg.file_name)

@bot.register(chats=User, msg_types=TEXT)
def process_text(msg):
    """
    处理文字信息
    """
    # # DEBUG
    # if '测试' in msg.text:
    #     msg.reply_file(r"D:\视频播放方法-windows.docx")
    #     return

    # 处理EXCEL表格中的关键词
    match = reply.search(msg.text)
    if match:
        reply_list = [s for s in match.split('###') if s]
        for reply_text in reply_list:
            if reply_text.startswith('file='):
                filepath = reply_text[5:]

                # 判断是不是图片
                ext = filepath.split('.')[1]
                if ext in ('jpg', 'jpeg', 'png'):
                    msg.reply_image(filepath)
                    break

                else:
                    msg.reply_file(filepath)
            else:
                msg.reply(reply_text)
        return



def gen_lisence():
    """生成注册码"""
    pass


# 最后，堵塞线程，让程序持续运行下去
embed()