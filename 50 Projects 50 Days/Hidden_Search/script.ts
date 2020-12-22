const search: HTMLDivElement = document.querySelector('.search')
const btn: HTMLButtonElement = document.querySelector('.btn')
const input: HTMLInputElement = document.querySelector('.input')

btn.addEventListener('click', (): void => {
    search.classList.toggle('active')
    input.focus();
})