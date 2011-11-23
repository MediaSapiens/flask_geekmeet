from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound
app = Flask(__name__)

@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def flask_geekmeet(page=None):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run()