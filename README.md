# MVCactus
MVCactus is a lightweight, open-source web framework for building small web applications in Python. It provides a simple and intuitive interface for handling HTTP requests and generating dynamic HTML content.

With MVCactus, you can define routes for handling different URLs, process GET and POST requests, and serve static files such as images, CSS files, and JavaScript files. MVCactus also includes a simple file uploader and validator for processing file uploads from HTML forms.

MVCactus is designed to be easy to use and easy to extend. It is suitable for building small web applications and prototypes, as well as for learning the basics of web development in Python.

### Getting started
To get started with MVCactus, follow these steps:

Install MVCactus using pip:

```pip install MVCactus```

Create a new Python file and import the MVCactus module:

```from MVCactus.MVCactus import MVCactus, MVCactusRun```

Inherit from ```MVCactus``` class, and define routes:

``` python
class MyApp(MVCactus):
    @MVCactus.route('/') # Main page.
    def home(self, match):
        context = {'title': 'First thing', 'second': 'Second thing'}
        self.render_template('index.html', context=context)
```

Place your HTML files in a folder named ```/templates```.

Run your application:
``` python
if __name__ == '__main__':
    app = MVCactusRun(port=PORT)
    app.run(MyApp)
```

### Features
* Follows the Model-View-Controller pattern for clear and organized code structure.
* Lightweight and efficient, making it a great fit for small-scale web development projects.
* Easy to use and easy to learn, with a simple and intuitive API.
* Provides built-in support for common web development features such as routing, templates, file upload and request/response handling.

### Working on
* More robust error-handling mechanism.

## Changelog - 2023-04-28

### Added
* **Support for CORS header:** The `send_response_headers` method now includes the `Access-Control-Allow-Origin` header with a wildcard value `(*)`, allowing any origin to access the resource.
* **Additional security headers:** The `send_response_headers` method now sends several security headers, such as `X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`, `Referrer-Policy`, and `Feature-Policy`.
* **Configurable server IP address:** The `MVCactusRun` class now accepts an optional host parameter to allow specifying a custom IP address instead of the default 'localhost'.
* **Simplified route decorator:** The `route` decorator in the `MVCactus` class was modified to automatically add the `'^'` at the beginning and `'$'` at the end of the URL pattern. This allows users to define routes without explicitly using regex syntax.

These changes improve the usability and security of MVCactus, making it easier for developers to create web applications with secure default settings.


### Contributing
I welcome contributions from the community! If you have ideas for new features or improvements to MVCactus, please open an issue or submit a pull request on GitHub.

### Website
https://pypi.org/project/MVCactus/

### License
MVCactus is licensed under the MIT License. See the LICENSE file for details.
