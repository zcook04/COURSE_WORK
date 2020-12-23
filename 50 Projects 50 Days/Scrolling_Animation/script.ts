const boxes: NodeListOf <HTMLDivElement> = document.querySelectorAll('.box')


const checkBoxes = (): void => {
    const animationTrigger: number = (window.innerHeight - 50)

    boxes.forEach((box: HTMLDivElement) => {
        const boxTop: number = box.getBoundingClientRect().top

        if (boxTop < animationTrigger) {
            box.classList.add('show')
        } else {
            box.classList.remove('show')
        }
    })
}

window.addEventListener('scroll', checkBoxes)

checkBoxes()