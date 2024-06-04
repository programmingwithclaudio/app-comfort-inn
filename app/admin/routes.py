# admin/routes.py
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user
from .forms import AddCourseForm, ReservationForm, BookingForm, CustomerForm
from .models import Customer, Booking, Pricing, Reservation
from . import admin_bp
from ..models import User


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


@admin_bp.route('/dashboard/booking')
def booking():
    # Página de inicio, muestra las reservas existentes
    bookings = Booking.query.all()
    return render_template('admin/booking.html', bookings=bookings)


@admin_bp.route('/dashboard/booking/add_booking', methods=['GET', 'POST'])
@login_required
def add_booking():
    form = BookingForm()
    form.cid.choices = [(customer.cid, customer.fullname) for customer in Customer.query.all()]
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


@admin_bp.route('/dashboard/booking/<int:booking_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_bookings(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    form = BookingForm(obj=booking)
    form.cid.choices = [(customer.cid, customer.fullname) for customer in Customer.query.all()]
    if form.validate_on_submit():
        booking.cid = form.cid.data
        booking.status = form.status.data
        booking.notes = form.notes.data
        booking.save()
        flash('Reserva actualizada con éxito', 'success')
        return redirect(url_for('admin.bookings'))
    return render_template('admin/edit_booking.html', form=form, booking=booking)


@admin_bp.route('/dashboard/reservations')
def reservations():
    # Mostrar todas las reservas en una tabla
    reservations = Reservation.query.all()
    return render_template('admin/reservation.html', reservations=reservations)


@admin_bp.route('/dashboard/reservations/new', methods=['GET', 'POST'])
@login_required
def add_reservation():
    form = ReservationForm()
    form.booking_id.choices = [(booking.id, f"Booking ID: {booking.id} - Customer: {booking.customer.fullname} - Status: {booking.status}") for booking in Booking.query.all()]
    if form.validate_on_submit():
        reservation = Reservation(
            booking_id=form.booking_id.data,
            start=form.start.data,
            end=form.end.data,
            type=form.type.data,
            requirement=form.requirement.data,
            adults=form.adults.data,
            children=form.children.data,
            requests=form.requests.data
        )
        reservation.save()
        flash('Nueva reserva creada con éxito', 'success')
        return redirect(url_for("admin.reservations"))
    return render_template('admin/new_reservation.html', form=form)


@admin_bp.route('/dashboard/reservations/<int:reservation_id>/edit', methods=['GET', 'POST'])
def edit_reservation(reservation_id):
    reservation = Reservation.find_by_id(reservation_id)
    form = ReservationForm(obj=reservation)
    form.booking_id.choices = [(booking.id, booking.name) for booking in Booking.query.all()]
    if form.validate_on_submit():
        reservation.booking_id = form.booking_id.data
        reservation.start = form.start.data
        reservation.end = form.end.data
        reservation.type = form.type.data
        reservation.requirement = form.requirement.data
        reservation.adults = form.adults.data
        reservation.children = form.children.data
        reservation.requests = form.requests.data
        reservation.save()
        return redirect(url_for('admin.reservations'))
    return render_template('admin/edit_reservation.html', form=form, reservation=reservation)


@admin_bp.route('/dashboard/reservations/<int:reservation_id>/delete', methods=['POST'])
def delete_reservation(reservation_id):
    reservation = Reservation.find_by_id(reservation_id)
    reservation.delete()
    return redirect(url_for('admin.reservations'))


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
