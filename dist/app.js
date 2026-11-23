const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() { navigation.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); menu.setAttribute('aria-label', 'Open navigation'); }
menu.addEventListener('click', () => { const open = navigation.classList.toggle('open'); menu.setAttribute('aria-expanded', String(open)); menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation'); });
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', e => { if(e.key === 'Escape') closeMenu(); });
document.addEventListener('click', e => { if(!e.target.closest('.header')) closeMenu(); });
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
 document.documentElement.classList.add('motion');
 const observer = new IntersectionObserver(entries => { entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); } }); }, {threshold: 0.08});
 document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}
const lightbox = document.querySelector('#lightbox');
document.querySelectorAll('.gallery-item').forEach(button => button.addEventListener('click', () => { lightbox.querySelector('img').src = button.dataset.image; lightbox.querySelector('img').alt = button.dataset.caption; lightbox.querySelector('p').textContent = button.dataset.caption; lightbox.showModal(); document.body.style.overflow = 'hidden'; }));
lightbox.querySelector('button').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', e => { if(e.target === lightbox) { const rect = lightbox.getBoundingClientRect(); if(e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom) lightbox.close(); } });
lightbox.addEventListener('close', () => { document.body.style.overflow = ''; });
document.querySelectorAll('.enquiry-form').forEach(form => form.addEventListener('submit', event => {
 event.preventDefault(); if (!form.reportValidity()) return;
 const values = new FormData(form);
 const body = ['Hello Runax Admissions,', '', 'I would like to enquire about studying at Runax.', '', ...Array.from(values, ([key, value]) => `${key.charAt(0).toUpperCase() + key.slice(1)}: ${String(value).trim()}`)].join('\n');
 window.location.href = `mailto:admission@runaxinstitute.com?subject=${encodeURIComponent('Admission enquiry: ' + values.get('program'))}&body=${encodeURIComponent(body)}`;
 form.querySelector('.form-status').textContent = 'Please send your draft from your email app. If no app opens, call +91 89616 29333 or email admission@runaxinstitute.com. Your enquiry has not been sent by this page.';
}));
document.querySelector('#year').textContent = new Date().getFullYear();
