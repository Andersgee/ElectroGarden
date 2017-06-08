import os.path
import cherrypy
import HTMLsnippets as hs


class HomePage:
    def __init__(self):
        self.test = TestPage()

    @cherrypy.expose
    def index(self):
        yield hs.header('Nice Title woo')
        yield hs.topnav(0)
        yield hs.div_section()
        yield '<h5>combined webserver and gateway interface</h5>'
        yield 'This is the default method of the HomePage class.<br>'
        yield '<a href="/test/">A TestPage</a>'
        yield hs.div_end()
        yield hs.divider()
        yield hs.div_section()
        yield hs.div_row()
        yield hs.boxlink('/posts/post1/index.html', '/images/thumb_galaxy.png', 'LINK1')
        yield hs.boxlink('/posts/ble.html', '/images/thumb_galaxy.png', 'LINK2')
        yield hs.boxlink('/posts/ble.html', '/images/thumb_galaxy.png', 'LINK3')
        yield hs.boxlink('/posts/ble.html', '/images/thumb_galaxy.png', 'LINK4')
        yield hs.div_end()
        yield hs.div_end()
        yield hs.divider()
        yield hs.footer()

    @cherrypy.expose
    def Contact(self):
        yield hs.header('Contact')
        yield hs.topnav(1)
        yield hs.div_section()
        yield '<h5>This is the contactpage. A method of the class HomePage</h5>'
        yield hs.div_end()
        yield hs.divider()
        yield hs.footer()

    @cherrypy.expose
    def About(self):
        yield hs.header('About')
        yield hs.topnav(2)
        yield hs.div_section()
        yield '<h5>This is the aboutpage. A method of the class HomePage</h5>'
        yield hs.div_end()
        yield hs.divider()
        yield hs.footer()


class TestPage:
    @cherrypy.expose
    def index(self, x=0, y=0, z3=0, z4=''):
        yield hs.header('TestPage')
        yield hs.topnav(3)

        yield hs.div_section()
        yield 'NUMBER form ( CoolFunc(x) = x*3/2+0.1 )'
        yield hs.POSTform_number('./', 'x')
        if x:
            yield '<p>Running that number through CoolFunc gives %.3f</p>' % (CoolFunc(float(x)))
        yield hs.div_end()

        yield hs.div_section()
        yield 'NUMBER form ( Fibonacci_numbers_below(x) )'
        yield hs.POSTform_number('./', 'y')
        if y:
            yield '<p>fibonacci numbers up to %i: <br> %s</p>' % (float(y), fib_max(float(y)))
        yield hs.div_end()

        yield hs.div_section()
        yield 'SLIDER form'
        yield hs.POSTform_slider('./', 'z3')
        if z3:
            yield '<p>here is the z3 value: %s </p>' % (mystrFunc(z3))
        yield hs.div_end()

        yield hs.div_section()
        yield 'RADIO form'
        yield hs.POSTform_radio('./', 'z4')
        if z4:
            yield '<p>here is the z4 value: %s </p>' % (mystrFunc(z4))
        yield hs.div_end()

        yield hs.divider()
        yield hs.footer()


def CoolFunc(x):
    return x*3/2+0.1


def fib_max(x):
    mylist = []
    a, b = 0, 1
    while a < x:
        mylist.append(a)
        a, b = b, a+b
    return str(mylist)


def mystrFunc(x):
    return str(x)

# root = HomePage()
# root.test = TestPage()

config_path = os.path.join(os.path.dirname(__file__), 'myconf.conf')
if __name__ == '__main__':
    # cherrypy.quickstart(root, config=config_path)
    cherrypy.quickstart(HomePage(), config=config_path)
