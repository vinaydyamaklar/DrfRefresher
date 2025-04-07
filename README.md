#### Structure
* **models.py:** Where all models live.
* **views.py:** Where all views for web pages live.
* **urls.py:** Router for web pages views.
* **admin.py:** All Django admin related settings.


```
    CREATE DATABASE drfrefresher;
    CREATE USER drfrefresher WITH PASSWORD 'your_password_here';
    ALTER ROLE drfrefresheruser SET client_encoding TO 'utf8';
    ALTER ROLE drfrefresheruser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE drfrefresheruser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE drfrefresher TO drfrefresheruser;
    
    # for testing
    ALTER USER drfrefresher CREATEDB;
```

```
sudo apt-get update
sudo apt-get install python-pip python-dev python3.6-dev git
sudo apt-get install build-essential libssl-dev libffi-dev
sudo apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev

python -m venv venv
source venv/bin/activate

Go to Project dir wher you want the project to be cloned
git clone https://github.com/vinaydyamaklar/DrfRefresher.git

cd DrfRefresher
pip install -r requirements.txt


# MAKE MIGRATIONS ONLY IF YOU ARE MODIFYING THE MODELS
python manage.py makemigrations

python manage.py migrate
python manage.py runserver
```

