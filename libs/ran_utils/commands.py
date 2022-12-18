import os
from signal import SIGINT,SIGILL
import multiprocessing

BOT_PROCESS:multiprocessing.Process

class Command_parser:
    def __init__(self,command:str) -> None:
        self.parse_command(command)
        
    def parse_command(self,command:str):
        tasklist=command.split(" ")
        command=tasklist[0]
        if len(tasklist) > 1:
            args=tasklist[1:]
        else:
            args=[]
        if command not in dir(self):
            print("unknown command,use 'help' to get help")
        else:
            try:
                getattr(self,command)(*args)
            except Exception as e:
                print(e)
    def help(self):
        print(
            '''
             
↓RAN'S Command Help↓
            
1.help : use help to get some useless help
2.stop : use it to stop bot(may not work in windows)
3.restart : use it to stop bot and restart
4.start : use it to start nonebot
            
            '''
        )
    def stop(self):
        print("start stop thread...")
        os.kill(BOT_PROCESS.pid,SIGINT)
        print("start successfully")
    def start(self):
        pass