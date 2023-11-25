from MVCactus.MVCactus import MVCactus, MVCactusRun
from random import randint


class MyApp(MVCactus):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.change_placeholdr_syntax('[[', ']]')

    @MVCactus.route('/')
    def index(self, match):
        context = {
            "title": "Placeholdr Example",
        }
        self.render_template('index.html', 'css/styles.css', 'js/script.js', context)

if __name__ == '__main__':
    app = MyApp
    server = MVCactusRun(port=randint(1000, 9999))
    server.run(app)
