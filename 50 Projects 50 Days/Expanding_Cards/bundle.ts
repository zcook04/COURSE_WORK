const images: NodeListOf<Element> = document.querySelectorAll('.image')

images.forEach(image => {
    image.addEventListener('click', () => {
        //First Clear All Active Classes
        images.forEach(image => {
            image.classList.remove('active')
        })
        image.classList.add('active')
})})