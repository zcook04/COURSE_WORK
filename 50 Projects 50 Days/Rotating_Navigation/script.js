var openBtn = document.getElementById('open');
var closeBtn = document.getElementById('close');
var container = document.querySelector('.container');
openBtn.addEventListener('click', function () {
    container.classList.add('show-nav');
});
closeBtn.addEventListener('click', function () {
    container.classList.remove('show-nav');
});
