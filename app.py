from flask import Flask, request, render_template
import stories

app = Flask(__name__)

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
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']

    story = stories.story
    text = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})

    return render_template('story1_result.html', text=text)




@app.route('/story2')
def story2():
    """Show story 2 form."""
    return render_template('story2.html')

@app.route('/story2_result')
def story2_result():
    """Show story 2 result."""
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']

    story = stories.story
    text = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})

    return render_template('story2_result.html', text=text)




@app.route('/story3')
def story3():
    """Show story 3 form."""
    return render_template('story3.html')

@app.route('/story3_result')
def story3_result():
    """Show story 3 result."""
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']

    story = stories.story
    text = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})

    return render_template('story3_result.html', text=text)


