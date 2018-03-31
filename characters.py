from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)

characters_list = convert_to_dict("characters.csv")

@app.route('/')
def index():
    ids_list = []
    char_list = []
    for character in characters_list:
        ids_list.append(character['ID'])
        char_list.append(character['Character'])
    pairs_list = zip(ids_list, char_list)
    return render_template('index.html', pairs=pairs_list, the_title="DC Directory of Characters")

@app.route('/char/<num>')
def detail(num):
    for character in characters_list:
        if character['ID'] == num:
            char_dict = character
            break
    return render_template('character.html', character=char_dict, the_title=char_dict['Character'])

if __name__ == '__main__':
    app.run(debug=True)
