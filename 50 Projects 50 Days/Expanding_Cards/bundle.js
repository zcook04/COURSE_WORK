var images = document.querySelectorAll('.image');
images.forEach(function (image) {
    image.addEventListener('click', function () {
        //First Clear All Active Classes
        images.forEach(function (image) {
            image.classList.remove('active');
        });
        image.classList.add('active');
    });
});
