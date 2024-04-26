# CHATTR
### Chattr is a service allowing you to anonymously create & join blazing-fast chatrooms in a few clicks.
A full installation instruction is provided below. Feel free 
to contribute to the project - 

### 0.0. Python preparation
```shell
python -m venv venv
```
```shell
. venv/bin/activate
```
```shell
pip install -r requirements/prod.txt 
```

### 0.1 React preparation   
Install Node.js, then run
```shell
cd .\chattr\chattr-react
```
```shell
npm install
```
```shell
npm run build
```

### 1. Configure environment variables
A postgres database, its owner (a user) and a Redis database are required  
```shell
cp .env.template .env
``` 
configure the corresponding values in your .env file

### 2. Run migrations
```shell
cd chattr
```
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

### 3. Run the server!
```shell
python manage.py runserver
```
