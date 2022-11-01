from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.form.get("action1"))
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print("heloo there tthis is button ")
            pass  # do something
        elif request.form.get('action2') == 'VALUE2':
            pass  # do something elss
        else:
            pass  # unknown

    elif request.method == 'GET':
        return render_template('home.html', form=form)

    return render_template("home.html")

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['File']
        f.save(secure_filename(f.filename))
        print("file uploaded successfully")
        return "File saved successfully"


if __name__ == '__main__':
    app.run(debug=True)
