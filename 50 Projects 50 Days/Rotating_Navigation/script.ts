const openBtn: HTMLElement = document.getElementById('open')
const closeBtn: HTMLElement = document.getElementById('close')
const container: HTMLElement = document.querySelector('.container')

openBtn.addEventListener('click', (): void => {
    container.classList.add('show-nav')
})

closeBtn.addEventListener('click', (): void => {
    container.classList.remove('show-nav')
})