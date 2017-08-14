def start_html():
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
    <link rel="stylesheet" href="/css/tablestyle.css">
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js"></script>
    </head>
    <body class="container">
    <div class="row">'''
    return HTML


def end_html():
    HTML = '''
    </div>
    </body>
    </html>'''
    return HTML


def start_card():
    HTML = '''
    <div class="col s12 m8 l8 center">
    <div class="card-panel">'''
    return HTML


def start_card2():
    HTML = '''
    <div class="col s12 m4 l4 center">
    <div class="card-panel">'''
    return HTML


def end_card():
    HTML = '''
    </div>
    </div>'''
    return HTML


#def start_table():
#    HTML = '''
#    <h4>ElectroGarden</h4>
#    <div style="overflow-x:auto;">
#    <table>
#    <tr><th>Amount</th><th>Time</th><th>Temp</th><th>Clouds</th><th>Humidity</th></tr>'''
#    return HTML

def start_table():
    HTML = '''
    <h4>ElectroGarden</h4>
    <table>
    <tr><th>ml</th><th>Time</th><th>Temp</th><th>Clouds</th><th>Humidity</th></tr>'''
    return HTML

def tablerow(A, t, T, C, H):
    HTML = '''
    <tr><td>%i</td><td>%s</td><td>%i&#8451</td><td>%i&#37</td><td>%i&#37</td></tr>''' % (A*14, t, T, C*100, H*100)
    return HTML


def end_table():
    HTML = '''
    </table>
    </div>'''
    return HTML


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
    <div class="switch"><label><b>Closed</b><input %s type="checkbox" %s onchange="document.getElementById('%s').submit()"><span class="lever"></span><b>Open</b></label></div>
    </div>
    </form>''' % (name, action, label, disabled_text, checked_text, name)
    return HTML
