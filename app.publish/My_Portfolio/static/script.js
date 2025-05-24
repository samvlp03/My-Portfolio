document.addEventListener('DOMContentLoaded', function () {
        const headings = document.querySelectorAll('.toggle-heading');

        headings.forEach(heading => {
        heading.addEventListener('click', function () {
            const content = this.nextElementSibling;
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        });
        });

    // Smooth scrolling for internal links
    const links = document.querySelectorAll('.navigation a');

        links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
        });
    });
    document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById('myModal');
    var modalImage = document.getElementById('modalImage');
    var closeBtn = document.querySelector('.close');

    document.querySelectorAll('.certificate img').forEach(function(img) {
        img.addEventListener('click', function () {
            modal.style.display = "flex"; // Show the modal
            modalImage.src = this.src; // Set the source of the modal image to the clicked image
        });
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = "none"; // Hide the modal
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
        modal.style.display = "none"; // Hide the modal if clicked outside
        }
    });
});
