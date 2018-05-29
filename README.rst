==========
PyForecast
==========


.. image:: https://img.shields.io/pypi/v/pyforecast.svg
        :target: https://pypi.python.org/pypi/pyforecast

.. image:: https://img.shields.io/travis/vafliik/pyforecast.svg
        :target: https://travis-ci.org/vafliik/pyforecast

.. image:: https://readthedocs.org/projects/pyforecast/badge/?version=latest
        :target: https://pyforecast.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Work In Progress
----------------
This project is currently under development. During sleepless nights, with two screaming kids :)

Please be patient. I would be grateful for any feedback & suggestions.


Introduction
------------

Python binding for `Forecast App <https://forecastapp.com>`_ (Harvest) API

Forecast is the fast and simple way to schedule your team across projects.

As per `Forecast FAQ <https://help.getharvest.com/forecast/faqs/faq-list/api/>`_ there is not a *public API* for the app. This project uses the exposed backend API (looks like Forecas guys are OK with that)


* Free software: Apache Software License 2.0
* Documentation: https://pyforecast.readthedocs.io. (do not go there yet, it is also WIP. Basic usage is described in this README)


Features
--------

Implemented
^^^^^^^^^^^
- Client
- Project
- Person
- Assignments
- Milestones
- Roles
- User Connections
- Placeholders

TO DO
^^^^^^^^^^^
- Who am I
- All PUT/POST requests (inserting/modifying data)
- **Documentation**


=====
Usage
=====

Create an Authorization token in Forecast App: https://id.getharvest.com/developers

Create an instance of the ``forecast.Api`` using the Account ID and Authorization token::

    >>> import forecast
    >>> api = forecast.Api(account_id='account_id', authorization_token='authorization_token')


To fetch a single user's public status messages, where ``user`` is a Twitter user's screen name::

    >>> for project in api.get_projects():
    >>>    print(project.name, project.id)
    Demo Project 101234
    Killer App 106555

    >>> person = api.get_person(42)
    >>> print(person.first_name, person.last_name, person.email)
    Pavel Pribyl pribyl.pavel@gmail.com

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
