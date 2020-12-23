var boxes = document.querySelectorAll('.box');
var checkBoxes = function () {
    var animationTrigger = (window.innerHeight - 50);
    boxes.forEach(function (box) {
        var boxTop = box.getBoundingClientRect().top;
        if (boxTop < animationTrigger) {
            box.classList.add('show');
        }
        else {
            box.classList.remove('show');
        }
    });
};
window.addEventListener('scroll', checkBoxes);
checkBoxes();
