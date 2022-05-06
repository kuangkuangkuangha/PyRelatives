class string(object):
    def __init__(self):
        self.string = ""

    def GetString(self):
        self.string = raw_input()

    def PutString(self):
        print(self.string)

s1 = string()
s1.GetString()
s1.PutString()