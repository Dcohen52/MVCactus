# Change log

## [Unreleased - 0.0.5] (25.11.2023)
* Full integration with Placeholdr templating engine.
* Improvements to the rendering of CSS and JS files inside the `render_template` method - now you can specify the path to the CSS and JS files relative to the `static` directory: `self.render_template('index.html', 'css/styles.css', 'js/script.js', context)`
* General code improvements and bug fixes.

## [Unreleased - 0.0.3-4] (02.05.2023)

### Fixed
* Resolved a bug related to the linking of CSS files.

### Added
* **Support for CORS header:** The `send_response_headers` method now includes the `Access-Control-Allow-Origin` header with a wildcard value `(*)`, allowing any origin to access the resource.
* **Additional security headers:** The `send_response_headers` method now sends several security headers, such as `X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`, `Referrer-Policy`, and `Feature-Policy`.
* **Configurable server IP address:** The `MVCactusRun` class now accepts an optional host parameter to allow specifying a custom IP address instead of the default 'localhost'.
* **Simplified route decorator:** The `route` decorator in the `MVCactus` class was modified to automatically add the `'^'` at the beginning and `'$'` at the end of the URL pattern. This allows users to define routes without explicitly using regex syntax.

## [Unreleased - 0.0.1-2] (Initial release)

* Initial release. 
