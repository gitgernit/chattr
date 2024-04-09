### 0. Python preparation
```shell
python -m venv venv
. venv/bin/activate

pip install -r requirements/prod.txt
```

### 1. Configure environment variables
A postgres database and a user is required  
`cp .env.template .env`, configure the variables

### 2. Run migrations
```shell
cd chattr
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the server!
