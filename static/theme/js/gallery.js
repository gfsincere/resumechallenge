// JavaScript to handle scroll and animation
document.addEventListener("scroll", function () {
    const galleryItems = document.querySelectorAll(".gallery-item");

    galleryItems.forEach(item => {
        const itemPosition = item.getBoundingClientRect().top;
        const screenPosition = window.innerHeight;

        // If the item is in the viewport, add the "show" class to trigger the animation
        if (itemPosition < screenPosition) {
            item.classList.add("show");
        }
    });
});