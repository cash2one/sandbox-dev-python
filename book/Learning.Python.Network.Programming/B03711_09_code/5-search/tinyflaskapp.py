from flask import Flask, render_template, abort, request, Markup, escape
import re
app = Flask(__name__)
app.debug = True

objs = __builtins__.__dict__.items()
docstrings = {name.lower(): obj.__doc__ for name, obj in objs if
              name[0].islower() and hasattr(obj, '__name__')}

@app.route('/')
def index():
    return render_template('index.html', funcs=sorted(docstrings))

@app.route('/functions/<func_name>')
def show_docstring(func_name):
    func_name = func_name.lower()
    if func_name in docstrings:
        return render_template('docstring.html', func_name=func_name,
                               doc=docstrings[func_name])
    else:
        abort(404)

@app.route('/search')
def run_search():
    search_text = request.args.get('searchtext', '')
    results = []
    for func_name, docstring in docstrings.items():
        for line in docstring.splitlines():
            if search_text in line:
                line = escape(line)
                wrap_text = '<span class="hi">{}</span>'.format(search_text)
                hi = re.sub(search_text, wrap_text, line, flags=re.I)
                results.append((func_name, Markup(hi)))
                break
    return render_template('search.html', search_text=search_text,
                           results=results)

if __name__ == '__main__':
    app.run()
