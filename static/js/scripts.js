/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function setImage(slug, title, url) {
    const imageModal = document.getElementById('imageModal');
    imageModal.setAttribute('src', `${window.location.origin}/${slug}/image`);

    const titleModal = document.getElementById('titleModal');
    titleModal.textContent = title;

    const hrefModal = document.getElementById('hrefModal');
    hrefModal.setAttribute('href', url);

    if(window.innerHeight >= window.innerWidth){
        imageModal.style.maxWidth = `${0.9 * window.innerWidth}px`;
        imageModal.style.Height = 'auto';
    } else {
        imageModal.style.maxHeight = `${0.75 * window.innerHeight}px`;
        imageModal.style.Width = 'auto';
    }

    console.log(`window.innerHeight: ${window.innerHeight}`)
    console.log(`window.innerWidth: ${window.innerWidth}`)
}