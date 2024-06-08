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
from datetime import datetime
from sqlalchemy import or_, and_, cast, VARCHAR
from app import db


@admin_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("admin/home.html")


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
    per_page = 6

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
    form.booking_id.choices = [
        (booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}") for booking in Booking.query.all()
    ]

    if form.validate_on_submit():
        booking_id = form.booking_id.data
        # Verifica si el estado de la reserva asociada está confirmado
        booking = Booking.query.get(booking_id)
        if booking and booking.status == 'CONFIRMED':
            try:
                # Concatenar la fecha y la hora de las entradas del formulario
                start_datetime_str = f"{form.start_date.data} {form.start_time.data}"
                end_datetime_str = f"{form.end_date.data} {form.end_time.data}"

                # Convertir a objetos datetime
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
                reservation.save()
                flash('Nueva reserva creada con éxito', 'success')
                return redirect(url_for("admin.reservations"))
            except ValueError:
                flash('Por favor, ingresa las fechas y horas en el formato correcto.', 'danger')
        else:
            # Si la reserva asociada no está confirmada, devolver un mensaje de error JSON
            return jsonify({'error': 'La reserva asociada no está confirmada. No se puede crear una reserva.'}), 400

    return render_template('admin/new_reservation.html', form=form)


@admin_bp.route('/dashboard/reservations/<int:reservation_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    form = ReservationForm(obj=reservation)
    form.booking_id.choices = [
        (booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}")
        for booking in Booking.query.all()
    ]

    if form.validate_on_submit():
        try:
            if form.start_date.data and form.start_time.data and form.end_date.data and form.end_time.data:
                # Concatenar la fecha y la hora de las entradas del formulario
                start_datetime_str = f"{form.start_date.data} {form.start_time.data}"
                end_datetime_str = f"{form.end_date.data} {form.end_time.data}"

                # Convertir a objetos datetime
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
                reservation.save()

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
    form.booking_id.choices = [
        (booking.id, f"ID: {booking.id} - Cliente: {booking.customer.fullname} - Estado: {booking.status}") for booking in Booking.query.all()
    ]

    if form.validate_on_submit():
        new_pricing = Pricing(
            booking_id=form.booking_id.data,
            nights=form.nights.data,
            total_price=form.total_price.data,
            booked_date=form.booked_date.data
        )
        new_pricing.save()
        flash('Nuevo precio agregado con éxito', 'success')
        return redirect(url_for('admin.pricing'))
    return render_template('admin/new_pricing.html', form=form)


@admin_bp.route('/dashboard/pricing/<int:pricing_id>/edit', methods=['GET', 'POST'])
@login_required
def pricing_edit(pricing_id):
    pricing = Pricing.query.get_or_404(pricing_id)
    form = PricingForm(obj=pricing)
    if form.validate_on_submit():
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
    page = request.args.get('page', 1, type=int)
    per_page = 15

    if search_term:
        # Filtrar las reservas según el término de búsqueda
        reservations = db.session.query(
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
        ).filter(or_(
            cast(Reservation.id, VARCHAR).ilike(f'%{search_term}%'),
            Customer.fullname.ilike(f'%{search_term}%'),
            Customer.email.ilike(f'%{search_term}%'),
            cast(Booking.status, VARCHAR).ilike(f'%{search_term}%'),
            cast(Pricing.total_price, VARCHAR).ilike(f'%{search_term}%')
        )).paginate(page=page, per_page=per_page)
    else:
        # Obtener todas las reservas
        reservations = db.session.query(
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
        ).paginate(page=page, per_page=per_page)

    return render_template('admin/report.html', reservations=reservations)