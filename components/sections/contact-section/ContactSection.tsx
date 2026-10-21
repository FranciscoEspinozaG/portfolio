'use client';
import { useState } from 'react';
export default function ContactSection() {
    const [notice, setNotice] = useState('');
    return <section tabIndex={0} aria-label="Contacto" id="contacto" className="muted contact">
    <div className="content">
    <h2>Contacto</h2>
    <p>¡Hablemos!</p>
    <p>Te dejo mis medios de contacto para que conversemos, actualmente estoy <b>disponible para nuevos proyectos</b>.</p>
    <div className="contact-links">{process.env.NEXT_PUBLIC_LINKEDIN_URL ? <a href={process.env.NEXT_PUBLIC_LINKEDIN_URL} target="_blank" rel="noopener noreferrer">Linkedin</a> : <button onClick={() => setNotice('El enlace de LinkedIn estará disponible pronto.')}>Linkedin</button>}{process.env.NEXT_PUBLIC_CONTACT_EMAIL ? <a href={`mailto:${process.env.NEXT_PUBLIC_CONTACT_EMAIL}`}>Email</a> : <button onClick={() => setNotice('La dirección de email estará disponible pronto.')}>Email</button>}</div>
    <p role="status">{notice.startsWith('El enlace') || notice.startsWith('La dirección') ? notice : ''}</p>
    </div>
    </section>;
}
