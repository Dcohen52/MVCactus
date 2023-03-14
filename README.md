# MiniMVC
MiniMVC is an open-souce lightweight micro web framework that follows the Model-View-Controller pattern, providing developers with a clear structure for building fast and efficient web applications.

### Getting started
To get started with MiniMVC, follow these steps:

Install MiniMVC using pip:

```pip install minimvc```

Create a new Python file and import the MiniMVC module:

```from minimvc import MiniMVC```

Inherit from ```MiniMVC``` class, and define routes:
```
class MyApp(MiniMVC):
    @MiniMVC.route('^/$')
    def home(self, match):
        context = {'title': 'First thing', 'second': 'Second thing'}
        self.render_template('home.html', context=context)
```

Run your application:
```
if __name__ == '__main__':
    app = MiniMVCApp(port=PORT)
    app.run(MyApp)
```

### Features
* Follows the Model-View-Controller pattern for clear and organized code structure.
* Lightweight and efficient, making it a great fit for small-scale web development projects.
* Easy to use and easy to learn, with a simple and intuitive API.

Provides built-in support for common web development features such as routing, templates, file upload and request/response handling.

### Working on
* Documentation.
* More robust error-handling mechanism.

### Contributing
I welcome contributions from the community! If you have ideas for new features or improvements to MiniMVC, please open an issue or submit a pull request on GitHub.

### License
MiniMVC is licensed under the MIT License. See the LICENSE file for details.
