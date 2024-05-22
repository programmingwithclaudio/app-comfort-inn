# Chatbots

Inicio 19/05 
```python
pip install flask flask-wtf email-validator
pip install python-dotenv
pip install flask-login
pip install psycopg2-binary
pip install Flask-SQLAlchemy
pip install psycopg2
pip install Flask-Migrate

```
- docker
```bash 
docker volume create postgres-db
docker exec -it postgres-data bash
psql -U postgres
flask db init        # Inicializa un nuevo directorio de migraciones
flask db migrate     # Genera una nueva migración a partir de los cambios en los modelos
flask db upgrade     # Aplica la migración a la base de datos

flask db migrate -m "Aumentar la longitud del campo password a 256 caracteres"
flask db upgrade

```
- git
``` 
git init
git branch -M main
git checkout -b developer
git checkout -b production
git commit -am "add model"
git remote add origin <url_del_repositorio_remoto>
git push -u origin main
git push -u origin development

git log
git tag <nombre_del_tag> <hash_del_commit>
git push origin <nombre_del_tag>
```
- postgres-db
```bash 
INSTALL
sudo apt update
sudo apt install postgresql postgresql-contrib
GO TO SHELL
sudo -u postgres psql
CONNECT TO A DB
\c bd_name
SHOW DBS
\l
SHOW TABLES
\dt
CREATE AN USER
create user username password 'password' (account_pass);
alter role username superuser;
CREATE DB WITH A SPECIFIC USER
create database db_name with owner user_name;
RESTART
sudo service postgresql restart
DELETE DB
>> drop database db_name;
LIST USERS
\du | \dut (with description)
POSTGRES STATUS
pg_lsclusters
CHANGE USER PASSWORD
alter user psotgres db_user password 'new_password';
TO KNOW USERS DB
select * from pg_stat_activity (get pid);
CLOSE USERS SESSION FROM DB
select pg_cancel_backend(pid);
KILL SESSIONS FROM A DB
select pg_terminate_backend(pid) from pg_stat_activity where datname='db_name';
DISCONNECT USERS FROM DB (change db_name)
select count(*) as users_online from pg_stat_activity where datname='olddb_name';
DISCONNECT ALL USERS FROM A DB
select pg_terminate_backend(pid) from pg_stat_activity where datname='db_name'
and procpid<> pg_backend_pid();
```
