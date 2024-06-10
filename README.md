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
pip install flask-bootstrap

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
pip freeze > requirements.txt

```
- docker
```bash
SELECT * FROM public.customer;
SELECT current_setting('data_directory') AS data_directory;
docker cp /home/crow/Descargas/customers.csv b35d2fccae0e:/var/lib/postgresql/data/customers.csv
docker exec -it b35d2fccae0e bash
ls /var/lib/postgresql/data
docker exec -it b35d2fccae0e bash
pg_dump -U postgres -d dbservice -F c -b -v -f /var/lib/postgresql/data/dbservice_backup.sql
docker cp b35d2fccae0e:/var/lib/postgresql/data/dbservice_backup.sql /home/crow/ti/basic-flask/dbservice_backup.sql

```
- docker modificate maal base de datos
```bash
SELECT * FROM public.customer;
SELECT current_setting('data_directory') AS data_directory;
DROP TABLE booking CASCADE;
DROP table public.customer;
CREATE TABLE customer (
    cid SERIAL PRIMARY KEY,
    identifier VARCHAR(25) NOT NULL UNIQUE,
    fullname VARCHAR(250) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(25)
);
COPY customer (cid, identifier, fullname, email, phone) FROM '/var/lib/postgresql/data/customers.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM pg_type WHERE typname = 'booking_status';
DROP TYPE IF EXISTS booking_status;
```
- Resoruces
``` 
https://dbdiagram.io/d/hotelsdb-64c9ef9b02bd1c4a5e17de58
https://github.com/tramyardg/hotel-mgmt-system/blob/master/image/screenshot/manage_booking.PNG
https://tablericons.com/
```
- Deploy profesional
``` 
pip install gunicorn
export CONFIG_ENV=config.dev
gunicorn -w 1 -b 127.0.0.1:8000 entrypoint:app
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


# CSS
- Cascade Style Sheets (hojas de estilo en cascada)
- Es un lenguaje que describe el renderizado de documentos estructurados como HTML o XML (SVG)
## 2. Historia de CSS

- La web nace en el 91 y CSS en el 96.
- Hubo varios intentos de crear un lenguaje de estilos
- El primer navegador en implementar CSS fue IE3

### Especificaciones de CSS

- **Dic 96 - CSS1**
  - https://www.w3.org/TR/REC-CSS1-961217
- **May 98 - CSS2**
  - https://www.w3.org/TR/REC-CSS2/
- **2011 - CSS 3**
  - Aquí se divide CSS en módulos (antes era un monolito).
  - [No existe CSS4](https://www.w3.org/TR/css-2023/#css-levels)
  - https://developer.mozilla.org/es/docs/Web/CSS/CSS3
- **HTML5**
  - https://www.w3.org/html/logo/
- **20 años de CSS**
  - https://www.w3.org/Style/CSS20/

    [A brief history of CSS until 2016](https://www.w3.org/Style/CSS20/history.html)

- **CSS snapshot (estado actual de CSS)**
  - https://www.w3.org/TR/CSS/
  - Aquí se ponen las cosas ya terminadas, porque CSS se sigue trabajando.
- Búscadores implmentan css;
```html
- Módulos CSS
- Borrador
- Borrador de la recomendación
- Implementación (safari malo)
```
- [css first](https://edteam.notion.site/1-Introducci-n-a-CSS-estudiantes-00ed53ac4e414f0fa0e61709ab4cca6a)
- [css second](https://edteam.notion.site/2-Selectores-estudiantes-21e47454f3304450bd19160fedd3e395)
- ciudado con los usr agent
- es key sencitive en etiquetas pero no en atributos
- normazile css
- selectores de clase
- [css specificity graph generator](https://jonassebastianohlsson.com/specificity-graph/)
- [google fonts](https://fonts.google.com/)
- [pexeles](https://www.pexels.com/es-es/)
```
  2.1 - Estilos del navegador EDteam.mp4
  2.2 - Selectores EDteam.mp4
  2.3 - Selectores simples etiqueta EDteam.mp4
  2.4 - Selectores simples clases EDteam.mp4
  2.5 - Selectores simples Id EDteam.mp4
  2.6 - Selectores compuestos agrupados EDteam.mp4
  2.7 - Selectores compuestos combinados EDteam.mp4
  2.8 - Selectores compuestos descendientes EDteam.mp4
  2.9 - Selectores de atributos EDteam.mp4
  Para formulario html [type], comodines enlaces
  2.10 - Selectores con operadores.mp4
  * universal, > hijo directo, + hermano directo, ~ her siguiente
```
- Los pilares Css
```
3.1 - ¿Cómo funciona CSS EDteam.mp4
La cascada (utilidad), especificidad (sol), herencia (arq).
3.2 - Especificidad EDteam.mp4
Etiquetas y pseudocodigo 1
Atributos y pseudocodigo 10
Id 100
Estilo en línea 1000

3.3 - Cascada EDteam.mp4
Lo que esta al final siempre le gana a lo que está antes
3.4 - Estilos computados EDteam.mp4
developers tols
3.5 - Herencia EDteam.mp4
usas container y heredas colores, centrado, (x posicionamiento)
3.6 - Layers CSS EDteam.mp4
organizar en capas el css @layer la declaracion manda en las cascadas
```
- Box Model
```
4.1 - Layout model EDteam.mp4
Todo es cajas skeleton
- Box model, Position, Flexbox, Grid - layoud RWD
4.2 - Elementos de línea y de bloque EDteam.mp4
<div> |<h1> hasta <h6> |<p> |<form> |<ul>, <ol>, <li> |<table>
width, height, margin, padding
<span> | <a>| <em>, <strong>| <img>| <input> NO (width, height)
4.3 - Propiedad display EDteam.mp4
display: block| display: inline| display: inline-block|display: none
display: flex|display: grid | table, table-row, table-cell
4.4 - Ejercicio Galería de imágenes EDteam.mp4
imágenes son inline block
4.5 - Propiedad margin EDteam.mp4
distancia entre elementos y elementos extraños
4.6 - ¿Cómo centrar un div EDteam.mp4
```
- Elemento de bloque
```css
div {
  width: 200px; /* Establecer un ancho */
  margin-left: auto;
  margin-right: auto;
}
```
```
4.7 - Propiedad padding EDteam.mp4
4.8 - Propiedad box-sizing EDteam.mp4
4.9 - Propiedades lógicas EDteam.mp4
Cambian el margin top, bottom, left, padding, right.
lógicas margin-block-start - padding-block-start
según el idioma cambian orientación al leer
```
- Bordes y Clases
```
5.1 - El border EDteam.mp4
5.2 - Border radius EDteam.mp4
5.3 - Outline EDteam.mp4
5.4 - Box shadow EDteam.mp4
```
- Pseudoclases
```
6.1 - ¿Qué son las pseudoclases EDteam.mp4
Selectores condicionales
6.2 - hover active visited EDteam.mp4
6.3 - target not empty EDteam.mp4
6.4 - first-child last-child first-of-type last-of-type EDte.mp4

6.5 - nth-child nth-of-type EDteam.mp4
```
- Fondos
```
7.1 - Background color EDteam.mp4
7.2 - Background size EDteam.mp4
rellenar un fondo la imagen que se corta
7.3 - Background position EDteam.mp4
7.4 - Background clip y Background origin EDteam.mp4
7.5 - Background attachment EDteam.mp4
- efectos en los fondo s d elas imagenes
7.6. - Background múltiples EDteam.mp4
7.7 - Shortand background EDteam.mp4
```
- Color
```
8.1 - Color Background EDteam.mp4
8.2 - Color keywords EDteam.mp4
8.3 - Modo RGB EDteam.mp4
8.4 - Notación Hexadecimal EDteam.mp4
8.5 - Modo HSL EDteam.mp4
8.6 - Degradados lineales EDteam.mp4
```
```css
body {
  color: #fff;
  background: linear-gradient(
    hsl(180, 80%, 60%),
    hsl(280, 80%, 60%),
    hsl(300, 90%, 70%)
  );
  min-height: 100vh;
}
```
```css
body {
  color: #fff;
  background: linear-gradient(
    100deg,
    hsl(180, 80%, 60%) 100px,
    hsl(300, 80%, 60%) 100px,
    hsl(300, 80%, 70%) 200px,
    hsl(60,100%,50%) 200px
  );
  min-height: 100vh;
}
```
```
8.7 - Degradados radiales EDteam.mp4
8.8 - Degradados repetidos EDteam.mp4
8.8 - Degradados repetidos EDteam.mp4
```
- Texto
```
9.1 - Conceptos básicos de tipografía EDteam.mp4
9.2 - Google fonts y font family EDteam.mp4
9.3 - Unidades de medida em y rem EDteam.mp4
9.4 - Estilos basicos de texto EDteam.mp4
```
## Figma
- [figma free](https://www.byol.com/fig)

---
## Eliminación cascada y manual
Para complementar la lógica de cascada de eliminación y permitir la eliminación de una reserva incluso si no tiene reservaciones asociadas, puedes ajustar la configuración de la relación entre `Booking` y `Reservation`. Actualmente, estás utilizando una relación de uno a muchos entre estas dos entidades, pero no has configurado la cascada de eliminación.

Aquí hay algunas opciones que puedes considerar:

1. **Agregar Cascada de Eliminación**: Puedes configurar la relación entre `Booking` y `Reservation` para que utilice la cascada de eliminación. Esto significa que cuando se elimina una reserva, todas las reservaciones asociadas también se eliminarán automáticamente. Esto se puede lograr agregando `cascade='all, delete-orphan'` a la relación en la definición de la clase `Booking`.

```python
reservations = db.relationship('Reservation', backref='booking', lazy=True, cascade='all, delete-orphan')
```

2. **Eliminar Manualmente las Reservaciones**: Si prefieres no usar la cascada de eliminación y permitir la eliminación manual de una reserva incluso si no tiene reservaciones asociadas, puedes agregar una lógica adicional al eliminar la reserva en tu función `delete_booking` en tus rutas.

```python
booking = Booking.query.get_or_404(booking_id)
# Verificar si hay reservaciones asociadas
if booking.reservations:
    # Eliminar manualmente las reservaciones
    for reservation in booking.reservations:
        db.session.delete(reservation)
# Eliminar la reserva
db.session.delete(booking)
db.session.commit()
```

- Con estas opciones, puedes elegir el enfoque que mejor se adapte a tus necesidades y preferencias en cuanto a la gestión de reservas y reservaciones en tu aplicación.
---
Para implementar controles de tesorería, incluyendo el manejo de ingresos, egresos y flujo de caja financiero, se pueden agregar las siguientes clases y relaciones al Diagrama de Clases UML:

```
+---------------+            +-------------+            +---------------+
|   Customer    |            |   Booking   |            |    Pricing    |
+---------------+            +-------------+            +---------------+
| -cid          |            | -id         |            | -pricing_id   |
| -identifier   |            | -cid        |            | -booking_id   |
| -fullname     |            | -status     |            | -nights       |
| -email        |            | -notes      |            | -total_price  |
| -phone        |            +-------------+            | -booked_date  |
+---------------+            |1    *|      |            +---------------+
     |1        *|            +-------------+                    |1
     +-----------------------+             |                    |
                                           |                    |
                                           |1                  *|
                                           |                    |
                                     +-------------+            |
                                     |Reservation  |            |
                                     +-------------+            |
                                     | -id         |<>----------+
                                     | -booking_id |
                                     | -start      |
                                     | -end        |
                                     | -type       |
                                     | -requirement|
                                     | -adults     |
                                     | -children   |
                                     | -requests   |
                                     | -timestamp  |
                                     | -hash       |
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |  Invoice    |
                                     +-------------+
                                     | -invoice_id |
                                     | -booking_id |
                                     | -issue_date |
                                     | -due_date   |
                                     | -subtotal   |
                                     | -taxes      |
                                     | -total      |
                                     | -status     |
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |  Supplier   |
                                     +-------------+
                                     | -supplier_id|
                                     | -name       |
                                     | -contact    |
                                     | -address    |
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |   Supply    |
                                     +-------------+
                                     | -supply_id  |
                                     | -supplier_id|
                                     | -item       |
                                     | -quantity   |
                                     | -cost       |
                                     | -date       |
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |CashFlow     |
                                     +-------------+
                                     | -flow_id    |
                                     | -date       |
                                     | -type       |
                                     | -amount     |
                                     | -description|
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |Account      |
                                     +-------------+
                                     | -account_id |
                                     | -name       |
                                     | -type       |
                                     | -balance    |
                                     +-------------+
                                           |1
                                           |
                                           |*
                                     +-------------+
                                     |Bank         |
                                     +-------------+
                                     | -bank_id    |
                                     | -name       |
                                     | -account_id |
                                     +-------------+
```

En este diagrama, se han agregado las siguientes clases:

1. **CashFlow**:
   - `flow_id`: Un identificador único para el movimiento de efectivo.
   - `date`: La fecha en la que se realizó el movimiento.
   - `type`: El tipo de movimiento (ingreso o egreso).
   - `amount`: El monto del movimiento.
   - `description`: Una descripción del movimiento.

2. **Account**:
   - `account_id`: Un identificador único para la cuenta.
   - `name`: El nombre de la cuenta.
   - `type`: El tipo de cuenta (por ejemplo, efectivo, bancaria, etc.).
   - `balance`: El saldo actual de la cuenta.

3. **Bank**:
   - `bank_id`: Un identificador único para el banco.
   - `name`: El nombre del banco.
   - `account_id`: El identificador de la cuenta bancaria asociada.

Las relaciones entre las clases son las siguientes:

- Una `Invoice` puede tener uno o más `CashFlow` asociados (relación 1 a *).
- Un `CashFlow` está asociado a una `Account` (relación 1 a 1).
- Una `Account` puede estar asociada a un `Bank` (relación 1 a 1).

**Implementación**:

1. **Ingresos**: Cuando se genera una factura (`Invoice`) para una reserva (`Booking`), se crea un movimiento de efectivo (`CashFlow`) de tipo "ingreso" con el monto total de la factura. Este ingreso se asocia a una cuenta de ingresos (`Account`) y se actualiza el saldo de dicha cuenta.

2. **Egresos**: Cuando se realiza un suministro (`Supply`), se crea un movimiento de efectivo (`CashFlow`) de tipo "egreso" con el costo del suministro. Este egreso se asocia a una cuenta de egresos (`Account`) y se actualiza el saldo de dicha cuenta.

3. **Flujo de Caja**: El flujo de caja se puede calcular sumando todos los ingresos y restando todos los egresos en un período de tiempo determinado. Se pueden crear informes de flujo de caja utilizando los movimientos de efectivo (`CashFlow`) y los saldos de las cuentas (`Account`).

4. **Cuentas Bancarias**: Las cuentas bancarias (`Bank`) pueden estar asociadas a cuentas de efectivo (`Account`) para representar los saldos de las cuentas bancarias.

**Patrones de Diseño**:

1. **Patrón de Fachada**: Se puede utilizar el patrón de fachada para proporcionar una interfaz simplificada para la gestión de tesorería. Una clase `TreasuryManagementFacade` podría encapsular la lógica de negocios relacionada con el manejo de ingresos, egresos, flujo de caja y cuentas bancarias, ocultando los detalles de implementación de las clases subyacentes.

2. **Patrón de Repositorio**: Se puede implementar el patrón de repositorio para abstraer la lógica de acceso a datos de los modelos `CashFlow`, `Account` y `Bank`. Se crearían repositorios separados que encapsulen las operaciones CRUD para cada uno de estos modelos.

3. **Patrón de Observador**: Si se requiere notificar a otros componentes del sistema cuando se realiza un movimiento de efectivo o se actualiza el saldo de una cuenta, se puede implementar el patrón de observador. Las clases `CashFlow` y `Account` podrían ser los sujetos observables, y otros componentes como el sistema de contabilidad o el sistema de reportes podrían suscribirse como observadores para recibir actualizaciones.

- Esta implementación sigue los principios de diseño orientado a objetos y los patrones de diseño relevantes, lo que facilita la extensibilidad, mantenibilidad y flexibilidad del sistema de gestión de tesorería y flujo de caja financiero.
---
