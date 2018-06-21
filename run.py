from flask import Flask, render_template
import pyscreenshot
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_screenshot', methods=['POST'])
def get_screenshot():
    im = pyscreenshot.grab()
    random_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    file_name = 'static/img/{}.png'.format(random_id)
    im.save(file_name)
    return render_template('show.html', screenshot=file_name)


if __name__ == '__main__':
    app.run(debug=True)
