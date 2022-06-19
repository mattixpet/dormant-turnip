def a(b,c):
    print(b,c)

class e():
    def __init__(self, callback, callback_args):
       self.callback = callback
       self.callback_args = callback_args
    def test(self):
       self.callback(*self.callback_args)


a(1,2)

e = e(a, [3,4])

e.test()