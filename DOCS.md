# MVCactus Documentation
#### Current Version 0.0.4
MVCactus is a lightweight web micro-framework for quickly developing and deploying web applications in Python. It uses the `Jinja2` templating engine for rendering templates (for now. i'm working on migration of [tempt](https://github.com/Dcohen52/MVCactus) and provides a set of convenient methods for handling HTTP requests and responses. MVCactus includes a routing system that allows users to map URLs to Python functions and supports both `GET` and `POST` requests. It also provides a method for serving static files and includes a basic file upload feature.

## Getting Started
To use `MVCactus`, create a new class that inherits from `MVCactus`, define your routes using the `route` decorator, and implement the corresponding Python functions. Then, create an instance of `MVCactusRun` and call its run method, passing in your app class as an argument.

## Installation
MVCactus is available via PyPI:
```
pip install MVCactus
```

## Example Usage
Here is a simple example of how to use MVCactus to create a basic web application:

``` python
from MVCactus.MVCactus import MVCactus, MVCactusRun

class MyApp(MVCactus):

    @MVCactus.route('/')
    def home(self, match):
        self.render_template('index.html')

    @MVCactus.route('/about')
    def about(self, match):
        self.render_template('about.html')

app_runner = MVCactusRun(port=8080)
app_runner.run(MyApp)
```

In this example, we define two routes: one for the `home page` and one for the `about page`. When a user visits either of these URLs, the corresponding function will be called, and the appropriate template will be rendered.

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

## Instance Methods
* **url_for_static(self, filename, port=None):** Generates a URL for serving a static file from the 'static' directory, given the filename and optional port number.
* **handle_error(self, status, message, template_name='upload.html', context=None):** Handles errors by sending the specified status and message as a response and rendering the specified template with the given context.
* **do_GET(self):** Handles GET requests sent to the server, serves static files, calls the corresponding callback function for matching URL patterns, or sends a 404 error response.
* **do_POST(self):** Handles POST requests sent to the server, saves uploaded files, calls the corresponding callback function for matching URL patterns and function names, or sends a 404 error response.
* **serve_static_file(self, path):** Serves a static file to the client with the given path.
* **validate_input(self, data, fields):** Validates the input data for a request, checking that all required fields are present.
* **render_template(self, template_name, context=None, css_url=None):** Renders a Jinja2 template with the given context and sends the resulting HTML to the client.

## Serving Static Files
MVCactus provides a convenient method for serving static files in your web applications. Static files include CSS stylesheets, JavaScript files, images, and other assets that are typically not dynamically generated.

To serve static files in MVCactus, you need to place your static files in a directory called "static" in the root of your project. The static directory should be located in the same directory as your MVCactus server file.

For example, if your MVCactus server file is named "app.py", the directory structure should look like this:

```
<project name>/
├── app.py
└── static/
    ├── css/
    │   └── styles.css
    │   js/
    │   └── script.js
    └── images/
        └── logo.png
```

To serve these static files, you can access them using the "/static/" URL path. For instance, to access the "styles.css" file, you would use the URL "/css/styles.css".

MVCactus automatically handles requests for static files and serves the corresponding file from the "static" directory. It sets the appropriate content type headers based on the file's extension and sends the file's contents in the response.

MVCactus provides automatic handling for the "static" and "templates" folders in your project. If these folders are not found in the root directory of your project - MVCactus will create them for you.

Usage: 
``` html
<link rel="stylesheet" href="{{ url_for_static('css/styles.css') }}">
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
