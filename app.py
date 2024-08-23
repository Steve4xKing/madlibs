from flask import Flask, request, render_template
from stories import Story 
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'whatever_my_secret_key_is' #this is a secret key that is used to encrypt the session cookie
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Show home page."""
    return render_template('main.html')

@app.route('/story1')
def story1():
    """Show story 1 form."""
    return render_template('story1.html')

@app.route('/story1_result')
def story1_result():
    """Show story 1 result."""
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('plural_noun')

    return render_template('story1_result.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)




@app.route('/story2')
def story2():
    """Show story 2 form."""
    return render_template('story2.html')

@app.route('/story2_result')
def story2_result():
    """Show story 2 result."""
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('plural_noun')

    return render_template('story2_result.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)




@app.route('/story3')
def story3():
    """Show story 3 form."""
    return render_template('story3.html')

@app.route('/story3_result')
def story3_result():
    """Show story 3 result."""
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('plural_noun')

    return render_template('story3_result.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)


