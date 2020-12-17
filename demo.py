import asyncio
from wechaty  import Wechaty,Message

import os
os.environ[ 'WECHATY_PUPPET_HOSTIE_TOKEN'] = 'puppet_donut_e175d*****ff25de1'

class MyBot(Wechaty):
    async def on_message(self, msg: Message):
        talker=msg.talker()
        await talker.ready()
        if msg.text()== "你好":
            await talker.say( '请问有什么事？')
        elif msg.text()== "博客":
            await talker.say( '知乎：https://www.zhihu.com/people/liu-jian-60-54\n简书：https://www.jianshu.com/u/ba83fba00eef\nCSDN：https://blog.csdn.net/liujian197905187511')
        elif msg.text()== "你是谁":
            await talker.say( '个人简介')
async def main():
    bot = MyBot()
    await bot.start()

asyncio.run(main())