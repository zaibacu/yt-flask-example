import json
from flask import Flask, render_template, request

app = Flask('example')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        print('Got some data! {}'.format(data))
        first_name = data['first_name']
        last_name = data['last_name']

        with open('data/contact.jsonl', 'a') as f:
            f.write(json.dumps(data) + '\n')

        return render_template('thank-you.html',
                               name='{first_name} {last_name}'.format(
                                   first_name=first_name,
                                   last_name=last_name
                               ))
    else:
        return render_template('contact.html')


app.run(debug=True)
