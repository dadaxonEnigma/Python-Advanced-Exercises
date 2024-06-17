class Acident(Exception):
    def __init__(self,msg) -> None:
        self.msg = msg
    def handle(self):
        print('accident occured. take detour')

try:
    raise Acident('crash between two cars')
except Acident as e:
    e.handle()
finally:
    print('Finish')