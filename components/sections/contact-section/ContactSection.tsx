'use client';
import { useLanguage } from '../../LanguageProvider';
import { useState } from 'react';
export default function ContactSection() {
  const { t } = useLanguage();
    const [notice, setNotice] = useState('');
    return <section tabIndex={0} aria-label={t("Contacto")} id="contacto" className="muted contact">
    <div className="content">
    <h2>{t("Contacto")}</h2>
    <p>{t("¡Hablemos!")}</p>
    <p>{t("Te dejo mis medios de contacto para que conversemos, actualmente estoy ")}<b>{t("disponible para nuevos proyectos")}</b>.</p>
    <div className="contact-links">{process.env.NEXT_PUBLIC_LINKEDIN_URL ? <a href={process.env.NEXT_PUBLIC_LINKEDIN_URL} target="_blank" rel="noopener noreferrer">Linkedin</a> : <button onClick={() => setNotice('El enlace de LinkedIn estará disponible pronto.')}>Linkedin</button>}{process.env.NEXT_PUBLIC_CONTACT_EMAIL ? <a href={`mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}`}>Email</a> : <button onClick={() => setNotice('La dirección de email estará disponible pronto.')}>Email</button>}</div>
    <p role="status">{t(notice)}</p>
    </div>
    </section>;
}
