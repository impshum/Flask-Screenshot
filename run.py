from flask import Flask, render_template
import pyscreenshot


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_screenshot', methods=['POST'])
def get_screenshot():
    im = pyscreenshot.grab()
    im.save('static/img/ss.png')
    return render_template('show.html', screenshot='/static/img/ss.png')


if __name__ == '__main__':
    app.run(debug=True)
