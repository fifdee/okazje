function setModalProperties(slug, title, description, url, price, rating, rating_count) {
    const imageModal = document.getElementById('imageModal');
    imageModal.setAttribute('src', `${window.location.origin}/${slug}/image`);
    imageModal.toggleAttribute('hidden', true);

    const imageModalLoading = document.getElementById('imageModalLoading');
    imageModalLoading.toggleAttribute('hidden', false);

    imageModal.addEventListener('load', () => {
        imageModalLoading.toggleAttribute('hidden', true);
        imageModal.toggleAttribute('hidden', false);
    });

    rating = parseFloat(rating.replace(',', '.')).toFixed(2);
    let stars = `<div class="d-flex justify-content-center small text-warning mb-2">`;

    for (let i = 0; i < 5; i++) {
        if (rating >= i + 0.75){
            stars = stars.concat(`<div class="bi-star-fill"></div>`);
        } else if (rating < i + 0.75 && rating >= i + 0.25){
            stars = stars.concat('<div class="bi-star-half"></div>');
        } else {
            stars = stars.concat('<div class="bi-star"></div>');
        }
    }

    stars = stars.concat(`&nbsp(${rating})</div>`);

    const titleModal = document.getElementById('titleModal');
    titleModal.innerHTML = `${title}<br>${stars}`;

    const descriptionModal = document.getElementById('descriptionModal');
    descriptionModal.innerHTML = description;

    const buttonModal = document.getElementById('buttonModal');
    buttonModal.textContent = `Kup na Allegro.pl za ${parseFloat(price.replace(',', '.')).toFixed(2)} zł`;

    const hrefModal = document.getElementById('hrefModal');
    hrefModal.setAttribute('href', url);

    if (window.innerHeight >= window.innerWidth) {
        imageModal.style.maxWidth = `${0.9 * window.innerWidth}px`;
        imageModal.style.Height = 'auto';
    } else {
        imageModal.style.maxHeight = `${0.75 * window.innerHeight}px`;
        imageModal.style.Width = 'auto';
    }
}

// document.addEventListener('DOMContentLoaded', () => {
//     const images = document.querySelectorAll('.img-load');
//     images.forEach(el => {
//       el.addEventListener('load', () => {
//           document.getElementById(`${el.id}Loading`).toggleAttribute('hidden', true);
//           el.toggleAttribute('hidden', false);
//       });
//     });
// });