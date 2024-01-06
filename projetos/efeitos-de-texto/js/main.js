for(let i = 1; i <= 20; i++){
    let box = document.createElement('div');
    box.classList.add('txtBox');
    box.innerHTML = "Justando <span>4</span>Textos";
    document.querySelector('.text').appendChild(box)
}
document.body.addEventListener("mousemove", e => {
    gsap.to('.txtBox', {
        x : e.clientX,
        y : e.clientY,
        stagger: -0.01,
        rotate: (i, target) => {
            return (i + 1) * 0.2
        }
    })
})