NCDR Reference
==============

A viewer for the schema of the National Commissioning Data Repository

## Set Up

    1. git clone
    1. mkvirtualenv
    1. make setup
    1. pre-commit install
    1. python manage.py load_data

Load in all existing csvs (stored in data/csvs):

    ./manage.py load_data


When running the server locally, we are using sass. So installl sass and run

    sass --watch ncdr/static/css/styles.scss:ncdr/static/css/styles.css -->


## deployment
1. update hosts.dev (and use keys natch)
1. set your branch in deployment/group_vars/all
1. create .vault.txt and put the vault password in there
1. cd deployment
1. ansible-playbook setup-server.yml -i hosts.dev --vault-password-file .vault.txt

to view the encrypted variables
ansible-vault edit all --vault-password-file ~/.vault.txt


## loading in new files.
We currently accept 3 csv files.

1. Columns
A file that contains all the information about NCDR references. These are columns
that exist in multiple tables and carry the same information.

2. Database and Tables
These contain information about the details and tables. For example descriptions
and display names.

3. Mappings
These contain information about the Mappings and Groupings of different columns.


## TODO
change the csv loader into a form.
add in a search function, but lets find out which columns to query
make the table look more like https://data.england.nhs.uk/dataset?
