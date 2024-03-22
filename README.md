# cookiecutter-flask-boring

*A "boring technology" template for the Flask microframework.*

This a a **minimalist's** **production-ready** [Flask](http://flask.pocoo.org) project
template with a set of all-importnat end-user features (authentication, user data
management, etc.) built with a boring technology.

This template builds on
[cookiecutter-flask-minimal](https://github.com/candidtim/cookiecutter-flask-minimal),
shares its minimalistic approach, and provides a feature-rich starting point
for a new web application. Just like its parent template, it attempts to impose
as few choices as possible, or proposes the most boring solutions where a
dependency is inevitable. It adds:

 - minimal working `Flask-SQLAlchemy` and `Flask-Migrate` setup
 - authentication with either of:
   * a minimal `Flask-Login` setup (build your own authentication on top)
   * a complete working authentication with [Auth0](https://auth0.com/)
     (authentication flow and user secrets are managed by Auth0)
 - minimalistic starter blueprint for the end-user web app, and a minimalistic
   blueprint for the front page; no web frameworks or libraries, but the most
   boring server-side HTML
 - optional `Flask-Admin` setup
 - optional [Stripe](https://stripe.com/) integration with a complete
   payment flow
 - optional [webpack](https://webpack.js.org/) configuration to properly
   package the static assets, with hot realod in the development mode
 - optional [HTMX](https://htmx.org/) setup

And the fetures inherited from the parent
[cookiecutter-flask-minimal](https://github.com/candidtim/cookiecutter-flask-minimal):

 - project set-up as per Flask documentation, including things like logging and
   config, testing and packaging
 - optional and off by deafult: flake8, black and mypy configuration
 - optional: [Poetry](https://python-poetry.org/) build tool, setuptools by defualt
 - preserves the pure joy of developing with Flask!

**Built for Flask 3 !**

## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pip install --user cookiecutter

Create your application from this template:

    cookiecutter https://github.com/candidtim/cookiecutter-flask-boring.git

# Contributions

... are welcome! Feel free to create a pull request to fix bugs or keep up to date.

If you think some additional feature is indispensable, feel free to create an
issue or a pull request, but bare in mind that the goal of this template is to
stay a "minimal" one. If you would like to add a feature, maybe best way to do
so is to make it optional and off by default then. One can use cookiecutter's
choice variables, and, ultimately, hooks, in order to create an optional
feature.

If you do a change, use `make test` from root directory to test the updated template.
