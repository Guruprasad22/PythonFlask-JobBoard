from faslk import FLask,render_template

app = Falsk(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')