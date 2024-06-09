# admin/routes.py
from flask import render_template, request, redirect, url_for, flash, abort, jsonify
from flask_login import login_required, logout_user, current_user
from .forms import (AddCourseForm, ReservationForm, BookingForm, CustomerForm, PricingForm,
                    BookingForm, CustomerForm, PricingForm, AccountForm, CashFlowForm, InvoiceForm, SupplierForm,
                    SupplyForm, BankForm)
from sqlalchemy.exc import IntegrityError
from .models import Customer, Booking, Pricing, Reservation, Account, CashFlow, Invoice, Supplier, Supply, Bank
from . import admin_bp
from ..models import User
from datetime import datetime, timedelta
from sqlalchemy import or_, and_, cast, VARCHAR
from app import db, mail
from sqlalchemy import func
from flask_mail import Message
import jsonpickle


@admin_bp.route("/dashboard")
@login_required
def dashboard():
    current_year = datetime.now().year
    current_month = datetime.now().month
    total_rooms = 50

    monthly_income = get_monthly_income(current_year)
    sales_growth_last_month = get_sales_growth_last_month(current_year, current_month)
    reservations_by_type = get_reservations_by_type(current_year)
    occupancy_rate = get_occupancy_rate(current_year, current_month, total_rooms)
    customer_segments = get_customer_segments()
    income_by_customer_segment = get_income_by_customer_segment()
    cancellations_count = get_cancellations_count(current_year)


    return render_template('admin/home.html',
                           monthly_income=monthly_income,
                           sales_growth_last_month=sales_growth_last_month,
                           reservations_by_type=reservations_by_type,
                           occupancy_rate=occupancy_rate,
                           customer_segments=customer_segments,
                           income_by_customer_segment=income_by_customer_segment,
                           current_year=current_year,
                           current_month=current_month,
                           cancellations_count=cancellations_count,
                           get_month_name=get_month_name,
                           )


def get_month_name(month):
    month_names = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return month_names.get(month, "Mes Inválido")



@admin_bp.route("/dashboard/settings")
@login_required
def settings():
    if request.method == 'POST':
        # Aquí puedes manejar la actualización de la información del usuario
        current_user.firstname = request.form['firstname']
        current_user.lastname = request.form['lastname']
        current_user.email = request.form['email']
        current_user.phone = request.form['phone']
        current_user.save()  # Guardar los cambios en la base de datos
        return redirect(url_for('settings'))  # Redirigir a la misma página de configuración después de guardar

    return render_template('admin/settings.html', user=current_user)


@admin_bp.route('/dashboard/bookings')
def booking():
    search_term = request.args.get('search', '')
    status_filter = request.args.get('status', '')  # Obtén el valor del filtro de estado
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Aplica el filtro de estado si se selecciona
    if status_filter:
        # Filtra las reservas por estado y ordénalas primero por estado y luego por ID
        bookings = Booking.query.filter_by(status=status_filter).order_by(Booking.status, Booking.id.desc())
        # También aplicas la búsqueda si se ingresó algún término de búsqueda
        if search_term:
            bookings = bookings.join(Booking.customer).filter(Customer.fullname.ilike(f'%{search_term}%'))
        bookings = bookings.paginate(page=page, per_page=per_page)
    else:
        # Si no se selecciona un filtro de estado, realiza la búsqueda normal y ordénalas por ID
        if search_term:
            bookings = Booking.query.join(Booking.customer).filter(Customer.fullname.ilike(f'%{search_term}%')).order_by(Booking.id.desc()).paginate(page=page, per_page=per_page)
        else:
            bookings = Booking.query.order_by(Booking.status, Booking.id.desc()).paginate(page=page, per_page=per_page)

    return render_template('admin/booking.html', bookings=bookings)


@admin_bp.route('/dashboard/bookings/get_customer_name', methods=['GET'])
def get_customer_name():
    identifier = request.args.get('identifier', '', type=str)
    customer = Customer.query.filter_by(identifier=identifier).first()
    if customer:
        return jsonify(fullname=customer.fullname, cid=customer.cid)
    else:
        return jsonify(fullname='', cid='')


@admin_bp.route('/dashboard/bookings/add_booking', methods=['GET', 'POST'])
@login_required
def add_booking():
    form = BookingForm()
    form.cid.choices = [(customer.cid, customer.identifier, customer.fullname) for customer in Customer.query.all()]
    if form.validate_on_submit():
        booking = Booking(
            cid=form.cid.data,
            status=form.status.data,
            notes=form.notes.data
        )
        booking.save()
        flash('Nueva reserva creada con éxito', 'success')
        return redirect(url_for('admin.booking'))
    return render_template('admin/new_booking.html', form=form)


@admin_bp.route('/dashboard/bookings/<int:booking_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_bookings(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = BookingForm(obj=booking)
    form.cid.choices = [(customer.cid, customer.identifier, customer.fullname) for customer in Customer.query.all()]
    if form.validate_on_submit():
        booking.cid = form.cid.data
        booking.status = form.status.data
        booking.notes = form.notes.data
        booking.save()
        flash('Reserva actualizada con éxito', 'success')
        return redirect(url_for('admin.booking'))
    return render_template('admin/edit_booking.html', form=form, booking=booking)


@admin_bp.route('/dashboard/bookings/<int:booking_id>/delete', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.find_by_id(booking_id)
    if booking:
        booking.delete()
        flash('Bookings eliminado con éxito', 'success')
    else:
        flash('Bookings no encontrado', 'danger')
    return redirect(url_for('admin.booking'))


@admin_bp.route('/dashboard/reservations')
def reservations():
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_term:
        # Utiliza join para obtener la información del cliente asociado a cada reserva
        reservations = Reservation.query \
            .join(Booking) \
            .join(Customer) \
            .filter(or_(Reservation.booking_id.ilike(f'%{search_term}%'),
                        Customer.fullname.ilike(f'%{search_term}%'))) \
            .paginate(page=page, per_page=per_page)
    else:
        # Utiliza join para obtener la información del cliente asociado a cada reserva
        reservations = Reservation.query \
            .join(Booking) \
            .join(Customer) \
            .paginate(page=page, per_page=per_page)

    return render_template('admin/reservation.html', reservations=reservations)


@admin_bp.route('/dashboard/reservations/new', methods=['GET', 'POST'])
@login_required
def add_reservation():
    form = ReservationForm()
    bookings = Booking.query.all()

    if not bookings:
        flash('No hay reservas disponibles para crear una nueva reserva.', 'danger')
        return redirect(url_for('admin.reservations'))

    form.booking_id.choices = [
        (booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}") for
        booking in bookings
    ]

    if form.validate_on_submit():
        booking_id = form.booking_id.data
        booking = Booking.query.get(booking_id)
        if booking and booking.status == 'CONFIRMED':
            try:
                start_datetime_str = f"{form.start_date.data} {form.start_time.data}"
                end_datetime_str = f"{form.end_date.data} {form.end_time.data}"
                start_date = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M')
                end_date = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M')

                reservation = Reservation(
                    booking_id=booking_id,
                    start=start_date,
                    end=end_date,
                    type=form.type.data,
                    requirement=form.requirement.data,
                    adults=form.adults.data,
                    children=form.children.data,
                    requests=form.requests.data
                )
                db.session.add(reservation)
                db.session.commit( )
                flash('Nueva reserva creada con éxito', 'success')
                return redirect(url_for("admin.reservations"))
            except ValueError:
                flash('Por favor, ingresa las fechas y horas en el formato correcto.', 'danger')
        else:
            flash('La reserva asociada no está confirmada. No se puede crear una reserva.', 'danger')

    return render_template('admin/new_reservation.html', form=form)


@admin_bp.route('/dashboard/reservations/<int:reservation_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    form = ReservationForm(obj=reservation)
    bookings = Booking.query.all()

    if not bookings:
        flash('No hay reservas disponibles para editar.', 'danger')
        return redirect(url_for('admin.reservations'))

    form.booking_id.choices = [
        (booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}") for
        booking in bookings
    ]

    if form.validate_on_submit():
        try:
            if form.start_date.data and form.start_time.data and form.end_date.data and form.end_time.data:
                start_datetime_str = f"{form.start_date.data} {form.start_time.data}"
                end_datetime_str = f"{form.end_date.data} {form.end_time.data}"
                start_date = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M')
                end_date = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M')

                reservation.booking_id = form.booking_id.data
                reservation.start = start_date
                reservation.end = end_date
                reservation.type = form.type.data
                reservation.requirement = form.requirement.data
                reservation.adults = form.adults.data
                reservation.children = form.children.data
                reservation.requests = form.requests.data
                db.session.commit()

                flash('Reserva actualizada con éxito', 'success')
                return redirect(url_for('admin.reservations'))
            else:
                raise ValueError("Las fechas y horas no pueden estar vacías.")
        except ValueError as e:
            flash('Por favor, ingresa las fechas y horas en el formato correcto.', 'danger')
            print(f"Error: {e}")

    return render_template('admin/edit_reservation.html', form=form, reservation=reservation)


@admin_bp.route('/dashboard/reservations/<int:reservation_id>/delete', methods=['POST'])
@login_required
def delete_reservation(reservation_id):
    reservation = Reservation.find_by_id(reservation_id)
    if reservation:
        reservation.delete()
        flash('Reserva eliminada con éxito', 'success')
    else:
        flash('La reserva no se encontró', 'danger')
    return redirect(url_for('admin.reservations'))


# Clientes y Proveedores
@admin_bp.route('/dashboard/customers')
@login_required
def customers():
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_term:
        customers = Customer.query.filter(Customer.identifier.ilike(f'%{search_term}%')).paginate(page=page, per_page=per_page)
    else:
        customers = Customer.query.paginate(page=page, per_page=per_page)

    return render_template('admin/customer.html', customers=customers)


@admin_bp.route('/dashboard/customers/add', methods=['GET', 'POST'])
@login_required
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        identifier = form.identifier.data
        email = form.email.data
        fullname = form.fullname.data
        phone = form.phone.data

        # Verificar si el identificador o el email ya existe
        existing_customer = Customer.query.filter(
            (Customer.identifier == identifier) |
            (Customer.email == email)
        ).first()

        if existing_customer:
            flash('El cliente con este identificador o correo electrónico ya existe.', 'danger')
            return redirect(url_for('admin.add_customer'))

        # Crear un nuevo cliente
        customer = Customer(
            identifier=identifier,
            fullname=fullname,
            email=email,
            phone=phone
        )

        try:
            customer.save()
            flash('Cliente añadido con éxito', 'success')
            return redirect(url_for('admin.customers'))
        except IntegrityError:
            customer.rollback()
            flash('Error: Integridad de datos violada.', 'danger')
        except Exception as e:
            customer.rollback()
            flash(f'Error inesperado: {str(e)}', 'danger')

    return render_template('admin/new_customer.html', form=form)


@admin_bp.route('/dashboard/customers/<int:customer_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        customer.identifier = form.identifier.data
        customer.fullname = form.fullname.data
        customer.email = form.email.data
        customer.phone = form.phone.data
        customer.save()
        flash('Cliente actualizado con éxito', 'success')
        return redirect(url_for('admin.customers'))
    return render_template('admin/edit_customer.html', form=form, customer=customer)


@admin_bp.route('/dashboard/customers/<int:customer_id>/delete', methods=['POST'])
@login_required
def delete_customer(customer_id):
    customer = Customer.find_by_id(customer_id)
    if customer:
        customer.delete()
        flash('Cliente eliminado con éxito', 'success')
    else:
        flash('Cliente no encontrado', 'danger')
    return redirect(url_for('admin.customers'))


@admin_bp.route('/dashboard/suppliers')
@login_required
def suppliers():
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_term:
        suppliers = Supplier.query.filter(Supplier.identifier.ilike(f'%{search_term}%')).paginate(page=page, per_page=per_page)
    else:
        suppliers = Supplier.query.paginate(page=page, per_page=per_page)

    return render_template('admin/supplier.html', suppliers=suppliers)


@admin_bp.route('/dashboard/suppliers/add', methods=['GET', 'POST'])
@login_required
def add_supplier():
    form = SupplierForm()
    if form.validate_on_submit():
        supplier = Supplier(
            identifier=form.identifier.data,
            fullname=form.name.data,
            contact=form.contact.data,
            address=form.address.data
        )
        supplier.save()
        flash('Proveedor añadido con éxito', 'success')
        return redirect(url_for('admin.suppliers'))
    return render_template('admin/new_supplier.html', form=form)


@admin_bp.route('/dashboard/suppliers/<int:supplier_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    form = SupplierForm(obj=supplier)
    if form.validate_on_submit():
        supplier.identifier = form.identifier.data
        supplier.fullname = form.fullname.data
        supplier.contact = form.contact.data
        supplier.address = form.address.data
        supplier.save()
        flash('Proveedor actualizado con éxito', 'success')
        return redirect(url_for('admin.suppliers'))
    return render_template('admin/edit_supplier.html', form=form, supplier=supplier)


@admin_bp.route('/dashboard/suppliers/<int:supplier_id>/delete', methods=['POST'])
@login_required
def delete_supplier(supplier_id):
    supplier = Supplier.find_by_id(supplier_id)
    if supplier:
        supplier.delete()
        flash('Proveedor eliminado con éxito', 'success')
    else:
        flash('Proveedor no encontrado', 'danger')
    return redirect(url_for('admin.suppliers'))


# pricing y/u otros
@admin_bp.route('/dashboard/pricing')
def pricing():
    search_term = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_term:
        pricings = Pricing.query.filter(Pricing.booking_id.ilike(f'%{search_term}%')).paginate(page=page, per_page=per_page, error_out=False)
    else:
        pricings = Pricing.query.paginate(page=page, per_page=per_page, error_out=False)

    return render_template('admin/pricing.html', pricings=pricings)


@admin_bp.route('/dashboard/pricing/new', methods=['GET', 'POST'])
@login_required
def add_pricing():
    form = PricingForm()
    # Filtrar bookings que no tienen un precio asignado
    form.booking_id.choices = [
        (booking.id, f"ID: {booking.id} - Cliente: {booking.customer.fullname} - Estado: {booking.status}")
        for booking in Booking.query.outerjoin(Pricing, Booking.id == Pricing.booking_id).filter(Pricing.booking_id == None).all()
    ]

    if form.validate_on_submit():
        # Verificar si el booking_id ya tiene un precio asignado
        existing_pricing = Pricing.query.filter_by(booking_id=form.booking_id.data).first()
        if existing_pricing:
            flash('El booking_id ya tiene un precio asignado.', 'danger')
            return redirect(url_for('admin.add_pricing'))

        new_pricing = Pricing(
            booking_id=form.booking_id.data,
            nights=form.nights.data,
            total_price=form.total_price.data,
            booked_date=form.booked_date.data
        )
        db.session.add(new_pricing)
        db.session.commit()
        flash('Nuevo precio agregado con éxito', 'success')
        return redirect(url_for('admin.pricing'))

    return render_template('admin/new_pricing.html', form=form)


@admin_bp.route('/dashboard/pricing/<int:pricing_id>/edit', methods=['GET', 'POST'])
@login_required
def pricing_edit(pricing_id):
    pricing = Pricing.query.get_or_404(pricing_id)
    form = PricingForm(obj=pricing)

    # Obtener todas las reservas disponibles
    bookings = Booking.query.all( )

    if not bookings:
        flash('No hay reservas disponibles para asignar precios.', 'danger')
        return redirect(url_for('admin.pricing'))

    # Crear las opciones para el campo de selección
    form.booking_id.choices = [
        (booking.id, f"ID: {booking.id} - Cliente: {booking.customer.fullname} - Estado: {booking.status}")
        for booking in bookings
    ]

    if form.validate_on_submit( ):
        pricing.nights = form.nights.data
        pricing.total_price = form.total_price.data
        pricing.booked_date = form.booked_date.data
        pricing.save()
        flash('Precio actualizado con éxito', 'success')
        return redirect(url_for('admin.pricing'))

    return render_template('admin/edit_pricing.html', form=form, pricing=pricing)


@admin_bp.route('/dashboard/pricing/<int:pricing_id>/delete', methods=['POST'])
@login_required
def pricing_delete(pricing_id):
    pricing = Pricing.query.get_or_404(pricing_id)
    booking_id = pricing.booking_id
    pricing.delete()
    flash('Precio eliminado con éxito', 'success')
    return redirect(url_for('admin.pricing_edit', booking_id=booking_id))


@admin_bp.route('/dashboard/reports', methods=['GET'])
def reservations_report():
    search_term = request.args.get('search', '')
    status_filter = request.args.get('status', 'all')
    date_filter = request.args.get('date', 'all')
    page = request.args.get('page', 1, type=int)
    per_page = 15

    query = db.session.query(
        Booking,
        Reservation,
        Customer,
        Pricing
    ).outerjoin(
        Reservation, Booking.id == Reservation.booking_id
    ).outerjoin(
        Customer, Booking.cid == Customer.cid
    ).outerjoin(
        Pricing, Booking.id == Pricing.booking_id
    )

    if search_term:
        query = query.filter(or_(
            cast(Reservation.id, VARCHAR).ilike(f'%{search_term}%'),
            Customer.fullname.ilike(f'%{search_term}%'),
            Customer.email.ilike(f'%{search_term}%'),
            cast(Booking.status, VARCHAR).ilike(f'%{search_term}%'),
            cast(Pricing.total_price, VARCHAR).ilike(f'%{search_term}%')
        ))

    if status_filter != 'all':
        query = query.filter(Booking.status == status_filter)

    if date_filter != 'all':
        today = datetime.today()
        if date_filter == 'this-week':
            start_of_week = today - timedelta(days=today.weekday())
            query = query.filter(Reservation.start >= start_of_week)
        elif date_filter == 'this-month':
            start_of_month = today.replace(day=1)
            query = query.filter(Reservation.start >= start_of_month)

    reservations = query.paginate(page=page, per_page=per_page)

    return render_template('admin/report.html', reservations=reservations, search_term=search_term, status_filter=status_filter, date_filter=date_filter)

@admin_bp.route('/dashboard/kpis', methods=['GET'])
def kpi_data():
    # Obtener el año y mes actual
    current_year = datetime.now().year
    current_month = datetime.now().month

    # Asumir un número fijo de habitaciones en el hotel (por ejemplo, 50)
    total_rooms = 50

    # Obtener datos para el primer gráfico (ingresos mensuales)
    monthly_income = get_monthly_income(current_year)

    # Obtener datos para la segunda tarjeta (tasa de crecimiento de ventas del mes anterior)
    sales_growth_last_month = get_sales_growth_last_month(current_year, current_month)

    # Obtener datos para el gráfico de reservas por tipo de habitación
    reservations_by_type = get_reservations_by_type(current_year)

    # Obtener la tasa de ocupación para el mes actual
    occupancy_rate = get_occupancy_rate(current_year, current_month, total_rooms)

    # Obtener la segmentación de clientes por frecuencia de reserva
    customer_segments = get_customer_segments()

    # Obtener ingresos por segmento de cliente
    income_by_customer_segment = get_income_by_customer_segment()

    # Obtener el número de cancelaciones de reserva
    cancellations_count = get_cancellations_count(current_year)

    return render_template('admin/kpi.html',
                           monthly_income=monthly_income,
                           sales_growth_last_month=sales_growth_last_month,
                           reservations_by_type=reservations_by_type,
                           occupancy_rate=occupancy_rate,
                           customer_segments=customer_segments,
                           income_by_customer_segment=income_by_customer_segment,
                           current_year=current_year,
                           current_month=current_month,
                           cancellations_count=cancellations_count
                           )


def get_monthly_income(year):
    # Consulta para obtener el total de ingresos mensuales
    results = db.session.query(
        func.extract('month', Reservation.start).label('month'),
        func.sum(Pricing.total_price).label('total_price')
    ).join(
        Booking, Booking.id == Reservation.booking_id
    ).join(
        Pricing, Booking.id == Pricing.booking_id
    ).filter(
        func.extract('year', Reservation.start) == year
    ).group_by(
        func.extract('month', Reservation.start)
    ).order_by(
        'month'
    ).all()

    # Formatear los resultados en un diccionario
    monthly_income = dict(zip(range(1, 13), [0] * 12))
    for result in results:
        monthly_income[int(result.month)] = float(result.total_price)

    return monthly_income

def get_sales_growth_last_month(year, month):
    # Obtener el último mes del año anterior
    last_month = month - 1 if month > 1 else 12
    last_year = year if month > 1 else year - 1

    # Obtener los ingresos del último mes del año anterior
    last_month_income = get_monthly_income(last_year)[last_month]

    # Obtener los ingresos del mes actual
    current_month_income = get_monthly_income(year)[month]

    # Calcular la tasa de crecimiento de ventas del mes anterior
    growth_rate = ((current_month_income - last_month_income) / last_month_income) * 100 if last_month_income != 0 else 0

    return round(growth_rate, 2)


def get_reservations_by_type(year):
    results = db.session.query(
        func.extract('month', Reservation.start).label('month'),
        Reservation.type.label('type'),
        func.count(Reservation.id).label('count')
    ).filter(
        func.extract('year', Reservation.start) == year
    ).group_by(
        func.extract('month', Reservation.start),
        Reservation.type
    ).order_by(
        'month'
    ).all()

    # Formatear los resultados en un diccionario
    reservations_by_type = {month: {'Single': 0, 'Double': 0, 'Deluxe': 0} for month in range(1, 13)}
    for result in results:
        reservations_by_type[int(result.month)][result.type] = result.count

    return reservations_by_type


def get_occupancy_rate(year, month, total_rooms):
    # Obtener el primer y último día del mes
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month + 1, 1) - timedelta(days=1) if month < 12 else datetime(year, 12, 31)

    # Calcular el número total de noches en el mes
    total_nights_in_month = (last_day - first_day).days + 1
    total_available_nights = total_nights_in_month * total_rooms

    # Consulta para obtener el número total de noches reservadas en el mes
    results = db.session.query(
        Reservation.start,
        Reservation.end
    ).filter(
        Reservation.start <= last_day,
        Reservation.end >= first_day
    ).all()

    total_reserved_nights = 0
    for reservation in results:
        start_date = max(reservation.start, first_day)
        end_date = min(reservation.end, last_day)
        total_reserved_nights += (end_date - start_date).days + 1

    occupancy_rate = (total_reserved_nights / total_available_nights) * 100 if total_available_nights > 0 else 0

    return round(occupancy_rate, 2)

def get_customer_segments():
    # Consulta para obtener el conteo de reservas por cliente
    results = db.session.query(
        Booking.cid,
        func.count(Booking.id).label('total_reservations')
    ).group_by(
        Booking.cid
    ).all()

    # Categorizar clientes
    segments = {'Frecuentes': 0, 'Ocasionales': 0, 'Raros': 0}
    for result in results:
        if result.total_reservations >= 10:
            segments['Frecuentes'] += 1
        elif result.total_reservations >= 3:
            segments['Ocasionales'] += 1
        else:
            segments['Raros'] += 1

    return segments

def get_income_by_customer_segment():
    # Calcular el ingreso total por cliente
    customer_incomes = db.session.query(
        Booking.cid,
        func.sum(Pricing.total_price).label('total_income')
    ).join(
        Reservation, Booking.id == Reservation.booking_id
    ).join(
        Pricing, Booking.id == Pricing.booking_id
    ).group_by(
        Booking.cid
    ).all()

    # Contar el número de reservas por cliente para segmentarlos
    customer_reservations = db.session.query(
        Booking.cid,
        func.count(Booking.id).label('reservation_count')
    ).group_by(
        Booking.cid
    ).all()

    # Crear diccionarios para almacenar los ingresos y la segmentación
    income_by_segment = {
        'Frecuentes': 0,
        'Ocasionales': 0,
        'Raros': 0
    }

    # Definir los umbrales para la segmentación
    frequent_threshold = 10  # Ejemplo: clientes con más de 10 reservas son frecuentes
    occasional_threshold = 3  # Ejemplo: clientes con entre 4 y 10 reservas son ocasionales

    # Crear un diccionario para mapear los ingresos a cada segmento de clientes
    reservation_counts = {cid: count for cid, count in customer_reservations}
    for cid, total_income in customer_incomes:
        count = reservation_counts.get(cid, 0)
        if count > frequent_threshold:
            income_by_segment['Frecuentes'] += total_income
        elif count > occasional_threshold:
            income_by_segment['Ocasionales'] += total_income
        else:
            income_by_segment['Raros'] += total_income

    return income_by_segment


def get_cancellations_count(year):
    # Consulta para contar el número de reservas canceladas en el año actual
    cancellations_count = Booking.query.filter_by(status='CANCELLED').count()
    return cancellations_count



def send_report_email(to_email, search_term, status_filter, date_filter, reservations):
    msg = Message("Informe de Reservas", recipients=[to_email])
    msg.html = render_template('admin/report.html', reservations=reservations, search_term=search_term, status_filter=status_filter, date_filter=date_filter)
    mail.send(msg)

@admin_bp.route('/send_report_email', methods=['POST'])
def send_report_email_route():
    data = request.get_json()
    to_email = data['to_email']  # Obtener la dirección de correo electrónico del usuario de alguna manera
    search_term = data['search_term']
    status_filter = data['status_filter']
    date_filter = data['date_filter']
    # Serializar los datos de las reservas de manera adecuada
    reservations = data['reservations']  # Ajusta esto según cómo estén estructurados los datos en el lado del cliente
    send_report_email(to_email, search_term, status_filter, date_filter, reservations)
    return jsonify({'success': True})