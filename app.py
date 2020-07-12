from imports import *
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello Flask!"


@application.route("/pic/<msg>")
def asdfer(msg):
    t = msg.split('^')
    v = t[0].split(' ')
    func = t[1]
    Plotter(v, func)
    with open('images.txt', mode='rt', encoding='utf-8') as txt:
        a = txt.read().split(' ')[-2]
    img = a + ".png"
    return render_template('image.html', image_file=img)


@application.route("/woleq/<msg>")
def asdfs(msg):
    try:
        try:
            a = []
            client = wolframalpha.Client('G45HAX-H76XQ2WVVA')
            res = client.query('Solution of ' + msg)
            for i in (res['pod'][1]['subpod']):
                 a.append(i['img']['@alt'])
            return str(a)[1:-1].replace("'", "")
        except TypeError:
            result = res['pod'][1]['subpod']['img']['@alt']
            return result
    except Exception as ex:
        return str(ex)


@application.route('/test/<asdf>')
def i(asdf):
    return asdf


@application.route('/latex/<equation>')
def ltxeq(equation):
    try:
        h = Ltx(equation)
        with open('images.txt', mode='rt', encoding='utf-8') as txt:
            a = txt.read().split(' ')[-2]
        img = a + ".png"
        return render_template('image.html', image_file=img)
    except Exception as ex:
        return "Error! > " + str(ex)

if __name__ == "__main__":
    Delete()
    application.run(host='192.168.219.105', port=5000)
