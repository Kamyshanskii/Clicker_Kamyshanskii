import flask
import clicker


host = 'localhost'
port = 5000

app = flask.Flask("Clicker")
app.clicker = clicker.Clicker()


@app.route('/', methods=['GET'])
def greeting():
    app.clicker.AutoChange()
    return flask.render_template('page.html', chr=app.clicker.CountUpdate())


@app.route('/hand_change', methods=['POST'])
def hand_change():
    app.clicker.HandChange()
    return flask.redirect('/')


@app.route('/hand_upgrade', methods=['POST'])
def hand_upgrade():
    app.clicker.UpgradeFunction()
    return flask.redirect('/')


@app.route('/auto_upgrade', methods=['POST'])
def auto_upgrade():
    app.clicker.AutoUpgradeFunction()
    return flask.redirect('/')


if __name__ == '__main__':
    app.run(host, port)
