from MVCactus.MVCactus import *

PORT = 8000


# Example for file upload using MVCactus

class App(MVCactus):
    CSS_PATH = 'main.css'

    @MVCactus.route('^/$')
    def home(self, match):
        context = {'title': 'First thing', 'second': 'Second thing'}
        self.render_template('index.html', context=context)

    @MVCactus.post('/upload')
    def handle_upload(self, body):
        content_type = self.headers['Content-Type']

        if 'multipart/form-data' in content_type:
            fields = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': content_type,
            })

            if 'file' in fields:
                file_item = fields['file']
                filename = os.path.join('uploads', file_item.filename)
                with open(filename, 'wb') as f:
                    f.write(file_item.file.read())
                    context = {'title': 'UPLOAD SUCCESS', 'second': 'SUCCESS'}
                self.render_template('upload_success.html', context=context)
                return

        self.send_error(400, 'Invalid request')

    @MVCactus.route(r'^/files$')
    def file_list(self, match):
        files = os.listdir('uploads')
        self.render_template('file_list.html', context={'files': files})


if __name__ == '__main__':
    app = MVCactusRun(port=PORT)
    app.run(App)
