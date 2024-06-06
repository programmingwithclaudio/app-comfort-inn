# admin/routes.py
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, logout_user, current_user
from .forms import (AddCourseForm, ReservationForm, BookingForm, CustomerForm, PricingForm,
                    BookingForm, CustomerForm, PricingForm, AccountForm, CashFlowForm, InvoiceForm, SupplierForm,
                    SupplyForm, BankForm)
from .models import Customer, Booking, Pricing, Reservation, Account, CashFlow, Invoice, Supplier, Supply, Bank
from . import admin_bp
from ..models import User
from datetime import datetime


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
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if search_term:
        # Aquí estoy asumiendo que 'fullname' es un campo en tu modelo Customer.
        # Necesitas ajustarlo según tu modelo real.
        bookings = Booking.query.join(Booking.customer).filter(Customer.fullname.ilike(f'%{search_term}%')).paginate(page=page, per_page=per_page)
    else:
        bookings = Booking.query.paginate(page=page, per_page=per_page)

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
    # Mostrar todas las reservas en una tabla
    reservations = Reservation.query.all()
    return render_template('admin/reservation.html', reservations=reservations)


@admin_bp.route('/dashboard/reservations/new', methods=['GET', 'POST'])
@login_required
def add_reservation():
    form = ReservationForm()
    form.booking_id.choices = [
        (booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}") for booking in Booking.query.all()
    ]

    if form.validate_on_submit():
        try:
            # Concatenar la fecha y la hora de las entradas del formulario
            start_datetime_str = f"{form.start_date.data} {form.start_time.data}"
            end_datetime_str = f"{form.end_date.data} {form.end_time.data}"

            # Convertir a objetos datetime
            start_date = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M')
            end_date = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M')

            reservation = Reservation(
                booking_id=form.booking_id.data,
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
        customer = Customer(
            identifier=form.identifier.data,
            fullname=form.fullname.data,
            email=form.email.data,
            phone=form.phone.data
        )
        customer.save()
        flash('Cliente añadido con éxito', 'success')
        return redirect(url_for('admin.customers'))
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
        pricings = Pricing.query.filter_by(booking_id=search_term).paginate(page=page, per_page=per_page)
    else:
        pricings = Pricing.query.paginate(page=page, per_page=per_page)

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


@admin_bp.route('/dashboard/pricing/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def pricing_edit(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = PricingForm()
    if form.validate_on_submit():
        pricing = Pricing(
            booking_id=booking_id,
            nights=form.nights.data,
            total_price=form.total_price.data,
            booked_date=form.booked_date.data
        )
        pricing.save()
        flash('Precio añadido con éxito', 'success')
        return redirect(url_for('admin.pricing_edit', booking_id=booking_id))
    pricings = Pricing.query.filter_by(booking_id=booking_id).all()
    return render_template('admin/pricing.html', booking=booking, form=form, pricings=pricings)


@admin_bp.route('/dashboard/pricing/<int:pricing_id>/delete', methods=['POST'])
@login_required
def pricing_delete(pricing_id):
    pricing = Pricing.query.get_or_404(pricing_id)
    booking_id = pricing.booking_id
    pricing.delete()
    flash('Precio eliminado con éxito', 'success')
    return redirect(url_for('admin.pricing_edit', booking_id=booking_id))