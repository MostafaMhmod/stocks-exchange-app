# stocks-exchange-app

To Run the App:
1- `pipenv shell` (to activate and create the virtual enviroment for python)
2- `pipenv install` (to install project's dependencies)
3- `docker-compose up` (starts the streaming and the MQTT services)
4- `python manage.py runserver` (starts the backend application)
5- `python manage.py stocks_prices` (starts the MQQT events subscriber and reflects the changes from the stream to the Database)

## Implementations Notes:
- Ideally, creating a backend service with the need of a low latency Should Not be implemented by the Django library
  since the only compatible library with support to low latency connection (MQTT, webscockts etc.) which is the django channel librarry 
  which lack the documentation and the resources for the MQTT support,a better solution would be to use either the fastapi framework
  along with the fastapi-mqtt tool for the MQTT integration support.

- In here for the sake of simplicity I'm using the Django's managment commands to subscripe to the MQTT events 
- all the money values are set as an integer field, however this is not recommended and when using numbers which is used 
  in calculating monetary values, a Decimal Field must be selected.
- in the Database structure there's no Accounts model, instead... an account is a collection of multiple transactions  
