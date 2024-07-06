import AOS from 'aos';

document.addEventListener('DOMContentLoaded', () => {
    // const AOS = require('aos');
    AOS.init(
        {
            duration: 1000,
            once: true
        }
    );
})