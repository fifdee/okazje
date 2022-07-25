let col1 = '#ff5e5e';
let col2 = '#fab825';
let col3 = '#FFFFFF';
let col4 = '#FFFFFF'; // site bg

function invertColor(hex, bw) {
    if (hex.indexOf('#') === 0) {
        hex = hex.slice(1);
    }
    // convert 3-digit hex to 6-digits.
    if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
    }
    if (hex.length !== 6) {
        throw new Error('Invalid HEX color.');
    }
    var r = parseInt(hex.slice(0, 2), 16),
        g = parseInt(hex.slice(2, 4), 16),
        b = parseInt(hex.slice(4, 6), 16);
    if (bw) {
        // https://stackoverflow.com/a/3943023/112731
        return (r * 0.299 + g * 0.587 + b * 0.114) > 186
            ? '#000000'
            : '#FFFFFF';
    }
    // invert color components
    r = (255 - r).toString(16);
    g = (255 - g).toString(16);
    b = (255 - b).toString(16);

    return "#" + (r) + (g) + (b);
}

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
    let stars = `<div class="d-flex justify-content-center small text-warning mt-2">`;

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
    buttonModal.textContent = `Idż do oferty (${parseFloat(price.replace(',', '.')).toFixed(2)} zł)`;

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

document.addEventListener('DOMContentLoaded', () => {
    // const images = document.querySelectorAll('.img-load');
    // images.forEach(el => {
    //   el.addEventListener('load', () => {
    //       document.getElementById(`${el.id}Loading`).toggleAttribute('hidden', true);
    //       el.toggleAttribute('hidden', false);
    //   });
    // });

    const col1_fill_elements = document.querySelectorAll('.col1_fill');
    col1_fill_elements.forEach(el => {
        el.style.fill = col1;
    });

    const col1_border_elements = document.querySelectorAll('.col1_border');
    col1_border_elements.forEach(el => {
        el.style.borderColor = col1;
    });

    const col1_bg_elements = document.querySelectorAll('.col1_bg');
    col1_bg_elements.forEach(el => {
        el.style.backgroundColor = col1;
    });

    const col2_border_elements = document.querySelectorAll('.col2_border');
    col2_border_elements.forEach(el => {
       el.style.borderColor = col2;
    });

    const col2_bg_elements = document.querySelectorAll('.col2_bg');
    col2_bg_elements.forEach(el => {
       el.style.backgroundColor = col2;
    });

    const col2_fill_elements = document.querySelectorAll('.col2_fill');
    col2_fill_elements.forEach(el => {
       el.style.fill = col2;
    });

    const col3_fill_elements = document.querySelectorAll('.col3_fill');
    col3_fill_elements.forEach(el => {
        el.style.fill = col3;
    });

    const col4_bg_elements = document.querySelectorAll('.col4_bg');
    col4_bg_elements.forEach(el => {
       el.style.backgroundColor = col4;
    });

    const text_on_col2 = document.querySelectorAll('.text-on-col2');
    text_on_col2.forEach(el => {
        el.style.color = invertColor(col2, false);
    });

    const text_on_col1 = document.querySelectorAll('.text-on-col1');
    text_on_col1.forEach(el => {
        el.style.color = invertColor(col1, false);
    });
});