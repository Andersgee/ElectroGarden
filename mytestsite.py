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
    def index(self, x1=0, x2=0, x3=0, x4='', x5='a', x6='b'):
        yield hs.header('TestPage')
        yield hs.topnav(3)

        yield hs.div_section()
        yield 'NUMBER form ( CoolFunc(x) = x*3/2+0.1 )'
        yield hs.POSTform_number('./', 'x1')
        if x1:
            yield '<p>Running that number through CoolFunc gives %.3f</p>' % (CoolFunc(float(x1)))
        yield hs.div_end()

        yield hs.div_section()
        yield 'NUMBER form ( Fibonacci_numbers_below(x) )'
        yield hs.POSTform_number('./', 'x2')
        if x2:
            yield '<p>fibonacci numbers up to %i: <br> %s</p>' % (float(x2), fib_max(float(x2)))
        yield hs.div_end()

        yield hs.div_section()
        yield 'SLIDER form'
        yield hs.POSTform_slider('./', 'x3')
        if x3:
            yield '<p>here is the x3 value: %s </p>' % (mystrFunc(x3))
        yield hs.div_end()

        yield hs.div_section()
        yield 'RADIO form'
        yield hs.POSTform_radio('./', 'x4')
        if x4:
            yield '<p>here is the x4 value: %s </p>' % (mystrFunc(x4))
        yield hs.div_end()

        yield hs.div_section()
        yield 'CHECKBOX form'
        yield hs.POSTform_checkbox('./', 'x5', 'x6')
        yield '<p>here is the values: %s, %s </p>' % (x5, x6)
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
