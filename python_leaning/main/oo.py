class Hello:
    def __init__(self,name):
        self._name = name

    def sayHello(self):
        print "Hello {0}".format(self._name)

class Hi(Hello):
#    def __init__(self,name):
#        Hello.__init__(self,name)

    def sayHi(self):
        print ("Hi {0}".format(self._name))

def name(request):
    print(request.get)

txt = "get http://www.jenkins.com"
name(txt)

h = Hello("tzm")
h.sayHello()

h1 = Hi("zhangsan")
h1.sayHi()