from MVCactus.MVCactus import MVCactus, MVCactusRun
from random import randint

class MyApp(MVCactus):

    @MVCactus.route('/')
    def index(self, match):
        self.render_template('index.html')


if __name__ == '__main__':
    app = MyApp
    server = MVCactusRun(port=randint(1000, 9999))
    server.run(app)
