# CHATTR
There is a site that helps you to create anonymous text and video chats with your friends or colleagues.
Set your own parameters in settings and share link.

### 0.0. Python preparation
```shell
python -m venv venv # create virtual environment
```
```shell
. venv/bin/activate # start virtual environment
```
```shell
pip install -r requirements/prod.txt # install requirements
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
configure the variables

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
ython manage.py runserver
```
