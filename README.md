# MVCactus
### Current Version: 0.0.4
MVCactus is a lightweight, robust, open-source web micro-framework tailored for developing compact web applications in Python. By providing an efficient and user-friendly interface, it streamlines the process of handling HTTP requests and generating dynamic HTML content.

The MVCactus micro-framework empowers developers to effortlessly define routes for managing distinct URLs, process GET and POST requests, and serve static files, including images, CSS files, and JavaScript files. Additionally, MVCactus incorporates a streamlined file uploader and validator, simplifying the handling of file uploads from HTML forms.

Engineered for adaptability and ease of use, MVCactus serves as an optimal choice for constructing small-scale web applications and prototypes, as well as for mastering the essentials of web development in Python. With an emphasis on security, MVCactus incorporates built-in security headers and CORS support.

### Getting started
To get started with MVCactus, follow these steps:

Install MVCactus using pip:

```pip install MVCactus```

Create a new Python file and import the MVCactus module:

```from MVCactus.MVCactus import MVCactus, MVCactusRun```

Inherit from ```MVCactus``` class, and define routes:

``` python
class MyApp(MVCactus):
    @MVCactus.route('/')
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
* CORS support with a wildcard value (*) for Access-Control-Allow-Origin, enabling cross-origin resource sharing for all origins.
* Enhanced security with several built-in security headers like X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy, and Feature-Policy.
* Configurable server IP address, allowing developers to specify custom IP addresses other than the default 'localhost'.

### Task list
- [x] HIGH: Fixing CSS support bug.
- [x] Add configurable IP address.
- [x] Add support for CORS and additional security headers.

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
