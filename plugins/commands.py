from khl import Bot, Message

def initCommands(bot: Bot) -> None:
    @bot.command(name='game',
                 aliases=['游戏'],
                 case_sensitive=False)
    async def cmdMain(msg: Message, *args: str):
        if not args: await msg.reply('无效输入。', use_quote=False)
        else:
            if args[0].lower() in ('ready', '准备'):
                if True: await msg.reply('没有游戏正在准备。', use_quote=False)
                else:
                    ...
            elif args[0].lower() in ('roulette', '轮盘赌'):
                ...
