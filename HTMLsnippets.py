def topnav(x):
    # 0 = Home
    # 1 = Contact
    # 2 = About
    mystr = ['n', 'n', 'n', 'n']
    mystr[x] = 'active'
    HTML = '''
    <ul class="topnav">
      <div class="container">
        <li><a class="%s" href="/">Home</a></li>
        <li class="right"><a class="%s" href="/Contact">Contact</a></li>
        <li class="right"><a class="%s" href="/About">About</a></li>
      </div>
    </ul>
    ''' % (mystr[0], mystr[1], mystr[2])
    return HTML


def header(title):
    HTML = '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>%s</title>
        <link rel="stylesheet" href="/css/materialize.css">
        <link rel="stylesheet" href="/css/topnav.css">
        <link rel="stylesheet" href="/css/post.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" href="/images/icon-4x.png">
      </head>
      <body>
        <div class="container">
        <center>
    ''' % (title)
    return HTML


def footer():
    HTML = '''
    </center>
    </div>
    </body>
    </html>
    '''
    return HTML


def boxlink(ahref, imgsrc, text):
    HTML = '''
    <div class="col s12 m6 l3">
    <a href="%s">
    <p class="z-depth-3">
    <img src="%s"><br>
    %s
    </p>
    </a>
    </div>
    ''' % (ahref, imgsrc, text)
    return HTML


def divider():
    HTML = '''
    <div class="divider"></div>
    '''
    return HTML


def div_section():
    HTML = '''
    <div class="section">
    '''
    return HTML


def div_row():
    HTML = '''
    <div class="row">
    '''
    return HTML


def div_end():
    HTML = '''
    </div>
    '''
    return HTML


def POSTform_number(methodname, varname):
    HTML = '''
    <form action="%s" method="POST">
    <input type="number" name="%s" step="any">
    <input type="submit" value="GO">
    </form>
    ''' % (methodname, varname)
    return HTML


def POSTform4(methodname, varname):
    HTML = '''
    <form action="%s">
    <select name="%s">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat">Fiat</option>
        <option value="audi">Audi</option>
    </select>
    <br><br>
    <input type="submit" value="GO">
    </form>
    ''' % (methodname, varname)
    return HTML


def POSTform_slider(methodname, varname):
    HTML = '''
    <form action="%s" method="POST">
    value:
    <input type="range" name="%s" min="0" max="100">
    <input type="submit" value="GO">
    </form>
    ''' % (methodname, varname)
    return HTML


def POSTform_radio(methodname, varname):
    HTML = '''
    <form action="%s" method="POST">
    <input type="radio" name="%s" value="male" checked> Male<br>
    <input type="radio" name="%s" value="female"> Female<br>
    <input type="radio" name="%s" value="other"> Other<br><br>
    <input type="submit" value="GO">
    </form>
    ''' % (methodname, varname, varname, varname)
    return HTML


def POSTform_checkbox(methodname, varname1, varname2):
    HTML = '''
    <form action="%s">
    <input type="checkbox" name="%s" value="Bike">I have a bike
    <br>
    <input type="checkbox" name="%s" value="Car">I have a car
    <br><br>
    <input type="submit" value="GO">
    </form>
    ''' % (methodname, varname1, varname2)
    return HTML
