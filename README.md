REST APIs for Providers and Service Areas
==============================
REST APIs to perform CRUD operations on transport providers, and give them the ability to add their service areas with pricing.

Built using
----------------------
* Python (Preferred 3.6)
* Django
* Postgresql

Getting Started
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL 9.3 or superior with Postgis Extension

First make sure to create and activate a virtualenv, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

Then, create a PostgreSQL database and add the database configuration to the settings.py file


You can now run the usual Django ``migrate`` and ``runserver`` command to start up the project::

    $ python manage.py migrate

    $ python manage.py runserver

The API documentation would by default be available on :: ``http://localhost:8000/docs/``
