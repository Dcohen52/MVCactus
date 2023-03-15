# MiniMVC
MiniMVC is a lightweight, open-source web framework for building small web applications in Python. It provides a simple and intuitive interface for handling HTTP requests and generating dynamic HTML content.

With MiniMVC, you can define routes for handling different URLs, process GET and POST requests, and serve static files such as images, CSS files, and JavaScript files. MiniMVC also includes a simple file uploader and validator for processing file uploads from HTML forms.

MiniMVC is designed to be easy to use and easy to extend. It is suitable for building small web applications and prototypes, as well as for learning the basics of web development in Python.

### Getting started
To get started with MiniMVC, follow these steps:

Install MiniMVC using pip:

```pip install MiniMVC```

Create a new Python file and import the MiniMVC module:

```from MiniMVC.MiniMVC import MiniMVC, MiniMVCRun```

Inherit from ```MiniMVC``` class, and define routes:
```
class MyApp(MiniMVC):
    @MiniMVC.route('^/$') # Main page.
    def home(self, match):
        context = {'title': 'First thing', 'second': 'Second thing'}
        self.render_template('index.html', context=context)
```

Place your HTML files in a folder named ```/templates```.

Run your application:
```
if __name__ == '__main__':
    app = MiniMVCRun(port=PORT)
    app.run(MyApp)
```

### Features
* Follows the Model-View-Controller pattern for clear and organized code structure.
* Lightweight and efficient, making it a great fit for small-scale web development projects.
* Easy to use and easy to learn, with a simple and intuitive API.
* Provides built-in support for common web development features such as routing, templates, file upload and request/response handling.

### Working on
* Documentation.
* Easier syntax.
* More robust error-handling mechanism.

### Contributing
I welcome contributions from the community! If you have ideas for new features or improvements to MiniMVC, please open an issue or submit a pull request on GitHub.

### Website
https://pypi.org/project/MiniMVC/

### License
MiniMVC is licensed under the MIT License. See the LICENSE file for details.
