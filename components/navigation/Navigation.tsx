'use client';

import './navigation.css';

import { useEffect, useState } from 'react';
import { sections } from '../../data/portfolio';

export default function Navigation() {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState('');

  useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, { rootMargin: '-35% 0px -35% 0px' });
    document.querySelectorAll('main > section').forEach(section => observer.observe(section));
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const previousOverflow = document.body.style.overflow;
    if (open) document.body.style.overflow = 'hidden';
    const escape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false);
    };
    window.addEventListener('keydown', escape);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener('keydown', escape);
    };
  }, [open]);

  return (
    <>
      <a className="skip-link" href="#acerca">Saltar al contenido</a>
      <button className={`menu-toggle ${open ? 'is-open' : ''}`}
        aria-label={open ? 'Cerrar menú' : 'Abrir menú'} aria-expanded={open}
        aria-controls="navigation" onClick={() => setOpen(!open)}>
        <span /><span /><span />
      </button>
      {open && <button className="menu-backdrop" aria-label="Cerrar menú" onClick={() => setOpen(false)} />}
      <nav id="navigation" aria-label="Navegación principal" className={open ? 'navigation open' : 'navigation'}>
        {sections.map(({ id, label }) => (
          <a key={id} href={`#${id}`} className={active === id ? 'active' : ''}
            aria-current={active === id ? 'location' : undefined} onClick={() => setOpen(false)}>
            {label}
          </a>
        ))}
      </nav>
    </>
  );
}
