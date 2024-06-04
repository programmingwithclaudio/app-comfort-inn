document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.querySelector('.panel__header input[type="search"]');
    const filterSelect = document.querySelector('.filter__select');
    const addNewButton = document.querySelector('.button.add');
    const tableBody = document.querySelector('.panel__table tbody');

    searchInput.addEventListener('input', filterTable);
    filterSelect.addEventListener('change', filterTable);
    addNewButton.addEventListener('click', addNewBooking);

    function filterTable() {
        const searchTerm = searchInput.value.toLowerCase();
        const filterValue = filterSelect.value;

        const rows = tableBody.querySelectorAll('tr');

        rows.forEach(row => {
            const cells = row.querySelectorAll('td');
            const guestName = cells[0].innerText.toLowerCase();
            const bookingStatus = cells[2].innerText.toLowerCase();

            const matchesSearch = guestName.includes(searchTerm);
            const matchesFilter = filterValue === 'all' || bookingStatus === filterValue.replace('-', ' ');

            if (matchesSearch && matchesFilter) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    function addNewBooking() {
        // Implement the logic to add a new booking
    }
});
