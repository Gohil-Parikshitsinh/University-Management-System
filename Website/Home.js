document.addEventListener("DOMContentLoaded", function () {
    let aboutSection = document.querySelector(".about-section");

    window.addEventListener("scroll", function () {
        let sectionPosition = aboutSection.getBoundingClientRect().top;
        let screenPosition = window.innerHeight / 1.3;

        if (sectionPosition < screenPosition) {
            aboutSection.classList.add("visible");
        }
    });
});
