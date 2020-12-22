const progress: HTMLElement = document.getElementById('progress')
const prev: any = document.getElementById('prev')
const next: any = document.getElementById('next')
const circles: NodeListOf<HTMLElement> = document.querySelectorAll('.circle')

let currentActiveCircle: number = 1

next.addEventListener('click', (): void => {
    currentActiveCircle++

    if(currentActiveCircle > circles.length) {
        currentActiveCircle = circles.length
    }

    update()
})

prev.addEventListener('click', (): void => {
    currentActiveCircle--

    if(currentActiveCircle < 1) {
        currentActiveCircle = 1;
    }

    update()
})

const update = (): void => {
    circles.forEach((circle, index) => {
        if(index < currentActiveCircle) {
            circle.classList.add('active')
        } else {
            circle.classList.remove('active')
        }
    })

    const actives: NodeListOf<HTMLElement> = document.querySelectorAll('.active')
    progress.style.width = ((actives.length - 1)/(circles.length -1))*100 + '%'

    if(currentActiveCircle === 1) {
        prev.disabled = true;
    } else if(currentActiveCircle === circles.length) {
        next.disabled = true
    } else {
        prev.disabled = false;
        next.disabled = false;
    }
}