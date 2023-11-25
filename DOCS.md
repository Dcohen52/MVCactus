# MVCactus Documentation
#### Current Version: 0.0.5

MVCactus is a lightweight Python web framework that makes it easy to create web applications using the Model-View-Controller (MVC) design pattern. It is built on top of the standard Python HTTP server and uses the Placeholdr templating engine to render HTML templates.
## Getting Started
To use `MVCactus`, create a new class that inherits from `MVCactus`, define your routes using the `route` decorator, and implement the corresponding Python functions. Then, create an instance of `MVCactusRun` and call its run method, passing in your app class as an argument.

## Installation
MVCactus is available via PyPI:
```
pip install MVCactus
```

## Example Usage
Here is a simple example of how to use MVCactus to create a basic web application:

```python
from MVCactus.MVCactus import MVCactus, MVCactusRun

class MyApp(MVCactus):

    @MVCactus.route('/')
    def home(self, match):
        self.render_template('index.html', 'css/home.css', 'js/home.js')

app_runner = MVCactusRun(port=8080)
app_runner.run(MyApp)
```

In this example, we create a new class called `MyApp` that inherits from `MVCactus`. We then define a route for the root URL path `/` and implement the corresponding function `home`. The `home` function renders the `index.html` template and sends it to the client.
---

## MVCactus Class
The main class that you'll use to create your web application. Inherit from this class to define your application's routes and behavior.
``` python
class MyApp(MVCactus):
```

## Class Methods and Decorators
* **route(cls, pattern):** A decorator for registering a URL pattern and callback function to handle requests for that pattern.
* **post(cls, path):** A decorator for registering a POST request handler with a given path.

``` python
@MVCactus.route('/')
def home(self, match):
    self.render_template('index.html')
```

## Serving Static Files
MVCactus provides a convenient method for serving static files in your web applications. Static files include CSS stylesheets, JavaScript files, images, and other assets that are typically not dynamically generated.

To serve static files in MVCactus, you need to place your static files in a directory called "static" in the root of your project. The static directory should be located in the same directory as your MVCactus server file.

For example, if your MVCactus server file is named "app.py", the directory structure should look like this:

```bash
    your_project_directory/
    │
    ├── MVCactus/             # Directory containing your MVCactus class
    │   └── ...
    │
    ├── templates/            # Directory containing your HTML templates
    │   ├── home.html
    │   ├── about.html
    │   └── ...
    │
    ├── static/               # Directory containing all static files like CSS, JS, images
    │   ├── css/              # Subdirectory for CSS files
    │   │   ├── home.css
    │   │   ├── about.css
    │   │   └── ...
    │   │
    │   ├── js/               # Subdirectory for JavaScript files
    │   │   ├── home.js
    │   │   ├── about.js
    │   │   └── ...
    │   │
    │   └── img/              # Subdirectory for images
    │       ├── logo.png
    │       └── ...
    │
    └── main.py               # Main Python file to run your web server

```

To serve these static files, you can access them using the "/static/" URL path. For instance, to access the "styles.css" file, you would use the URL "/css/styles.css".

MVCactus automatically handles requests for static files and serves the corresponding file from the "static" directory. It sets the appropriate content type headers based on the file's extension and sends the file's contents in the response.

MVCactus provides automatic handling for the "static" and "templates" folders in your project. If these folders are not found in the root directory of your project - MVCactus will create them for you.

Usage: 
``` html
<link rel="stylesheet" href="{{ styles_css }}">
<script src="{{ home_js }}"></script>
```

# MVCactusRun Class
A utility class to run an `MVCactus` application. Initializes the server with the specified port and application class.

Usage:
``` python
if __name__ == '__main__':
    app = MyApp
    server = MVCactusRun(port=PORT, address=ADDRESS)
    server.run(app)
```

## Instance Methods
* **run(self, app_class):** Runs the server with the specified application class on the provided port, serving requests indefinitely.

# Contributing
Contributions are welcome! If you have an idea for improving MVCactus, feel free to submit a pull request or open an issue on GitHub.
