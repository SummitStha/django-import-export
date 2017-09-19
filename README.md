# django-import-export
This is a simple example which implements the django-import-export package.

The django-import-export library supports multiple formats, including xls, csv, json, yaml, and all other formats supported by tablib. It also have a Django admin integration, which is really convenient to use.

## Installation
Install the packages susing pip:

pip install django

pip install django-import-export


## Update your settings.py:

INSTALLED_APPS = (

    ...
    'import_export',
)

### Add an optional configuration:

IMPORT_EXPORT_USE_TRANSACTIONS = True
