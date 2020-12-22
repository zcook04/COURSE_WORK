var progress = document.getElementById('progress');
var prev = document.getElementById('prev');
var next = document.getElementById('next');
var circles = document.querySelectorAll('.circle');
var currentActiveCircle = 1;
next.addEventListener('click', function () {
    currentActiveCircle++;
    if (currentActiveCircle > circles.length) {
        currentActiveCircle = circles.length;
    }
    update();
});
prev.addEventListener('click', function () {
    currentActiveCircle--;
    if (currentActiveCircle < 1) {
        currentActiveCircle = 1;
    }
    update();
});
var update = function () {
    circles.forEach(function (circle, index) {
        if (index < currentActiveCircle) {
            circle.classList.add('active');
        }
        else {
            circle.classList.remove('active');
        }
    });
    var actives = document.querySelectorAll('.active');
    progress.style.width = ((actives.length - 1) / (circles.length - 1)) * 100 + '%';
    if (currentActiveCircle === 1) {
        prev.disabled = true;
    }
    else if (currentActiveCircle === circles.length) {
        next.disabled = true;
    }
    else {
        prev.disabled = false;
        next.disabled = false;
    }
};
