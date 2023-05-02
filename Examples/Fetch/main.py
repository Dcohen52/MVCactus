import json
from MVCactus.MVCactus import MVCactus, MVCactusRun


class MyApp(MVCactus):
    @MVCactus.route('/')
    def index(self, match):
        self.render_template('index.html')

    @MVCactus.route('/api/data')
    def get_data(self, match):
        data = {"message": "Fetch from MVCactus!"}
        self.send_response_headers('application/json')
        self.wfile.write(json.dumps(data).encode('utf-8'))

    @MVCactus.post('/api/post_data')
    def handle_post_data(self, body):
        data = json.loads(body)
        response = {"status": "success", "message": "Data received"}
        self.send_response_headers('application/json')
        self.wfile.write(json.dumps(response).encode('utf-8'))


if __name__ == '__main__':
    app = MyApp
    server = MVCactusRun(port=8080)
    server.run(app)
