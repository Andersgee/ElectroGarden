def myswitch(name='', action='', label='', enabled=0, checked=0):
    if checked and enabled:
        checked_text = 'checked'
    else:
        checked_text = ''
    if enabled:
        disabled_text = ''
    else:
        disabled_text = 'disabled'
    HTML = '''
    <form id="%s" action="%s" method="POST">
    <div class="row">
    <label>%s</label>
    <div class="switch"><label>Closed<input %s type="checkbox" %s onchange="document.getElementById('%s').submit()"><span class="lever"></span>Open</label></div>
    </div>
    </form>
    ''' % (name, action, label, disabled_text, checked_text, name)
    return HTML


def myheader():
    HTML = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>ElectroGarden</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="mobile-web-app-capable" content="yes">
    <link rel="icon" sizes="192x192" href="/images/stupid_icon.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/css/materialize.min.css">
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js"></script>
    </head>
    <body class="container">
    '''
    return HTML


def begincard():
    HTML = '''
    <div class="col s12 m6 l6 center">
    <div class="card-panel">'''
    return HTML


def endcard():
    HTML = '''
    </div>
    </div>'''
    return HTML


def mygreeting(text=''):
    HTML = '''
    <div class="col s12 m6 l6 center">
    <div class="card-panel green lighten-3">
    <h4>ElectroGarden</h4>
    <p>%s</p>
    </div>
    </div>
    ''' % (text)
    return HTML


def myfooter():
    HTML = '''
    </body>
    </html>
    '''
    return HTML
