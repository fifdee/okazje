function setImage(slug, title, url) {
    const imageModal = document.getElementById('imageModal');
    imageModal.setAttribute('src', `${window.location.origin}/${slug}/image`);
    imageModal.toggleAttribute('hidden', true);

    const imageModalLoading = document.getElementById('imageModalLoading');
    imageModalLoading.toggleAttribute('hidden', false);

    imageModal.addEventListener('load', () => {
        imageModalLoading.toggleAttribute('hidden', true);
        imageModal.toggleAttribute('hidden', false);
    });

    const titleModal = document.getElementById('titleModal');
    titleModal.textContent = title;

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