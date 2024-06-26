document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(function(dropdown) {
        var button = dropdown.querySelector('.dropbtn');
        var dropdownContent = dropdown.querySelector('.dropdown-content');

        button.addEventListener('click', function() {
            dropdownContent.classList.toggle('show');
        });

        window.addEventListener('click', function(event) {
            if (!dropdown.contains(event.target)) {
                dropdownContent.classList.remove('show');
            }
        });
    });
});