from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from characters import app, characters_list

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def detail():
    for character in characters_list:
        yield { 'num': character['ID'] }

if __name__ == '__main__':
    freezer.freeze()
