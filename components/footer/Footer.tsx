import './footer.css';

export default function Footer() {
  const linkedin = process.env.NEXT_PUBLIC_LINKEDIN_URL || 'https://www.linkedin.com/in/franciscoespinozag';
  const email = process.env.NEXT_PUBLIC_CONTACT_EMAIL || 'francisco_e3@hotmail.com';

  return (
    <footer className="site-footer" aria-label="Fin de página">
      <p>© {new Date().getFullYear()} Francisco Espinoza. Todos los derechos reservados.</p>
      <p>Desarrollado con Next.js · Diseñado con intención.</p>
      <nav aria-label="Redes y contacto">
        <a href={linkedin} target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
        <span aria-hidden="true">·</span>
        <a href="https://github.com/FranciscoEspinozaG" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
        <span aria-hidden="true">·</span>
        <a href={`mailto:${email}`}>Email ↗</a>
      </nav>
    </footer>
  );
}
