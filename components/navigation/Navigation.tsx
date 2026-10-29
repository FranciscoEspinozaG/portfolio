'use client';
import { useLanguage } from '../LanguageProvider';
import './navigation.css';

import { useEffect, useState } from 'react';
import { sections } from '../../data/portfolio';

export default function Navigation() {
  const { t, language, setLanguage } = useLanguage();
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
      <div className="language-switch" role="group" aria-label={language === 'en' ? 'Language' : 'Idioma'}>
        <button type="button" lang="es" aria-label="Español" aria-pressed={language === 'es'} onClick={() => setLanguage('es')}>ES</button>
        <span aria-hidden="true">/</span>
        <button type="button" lang="en" aria-label="English" aria-pressed={language === 'en'} onClick={() => setLanguage('en')}>EN</button>
      </div>
      <a className="skip-link" href="#acerca">{t("Saltar al contenido")}</a>
      <button className={`menu-toggle ${open ? 'is-open' : ''}`}
        aria-label={open ? t('Cerrar menú') : t('Abrir menú')} aria-expanded={open}
        aria-controls="navigation" onClick={() => setOpen(!open)}>
        <span /><span /><span />
      </button>
      {open && <button className="menu-backdrop" aria-label={t("Cerrar menú")} onClick={() => setOpen(false)} />}
      <nav id="navigation" aria-label={t("Navegación principal")} className={open ? 'navigation open' : 'navigation'}>
        {sections.map(({ id, label }) => (
          <a key={id} href={`#${id}`} className={active === id ? 'active' : ''}
            aria-current={active === id ? 'location' : undefined} onClick={() => setOpen(false)}>
            {t(label)}
          </a>
        ))}
      </nav>
    </>
  );
}
