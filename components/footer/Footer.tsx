'use client';
import { useLanguage } from '../LanguageProvider';
import './footer.css';

export default function Footer() {
  const { t } = useLanguage();
  const linkedin = process.env.NEXT_PUBLIC_LINKEDIN_URL || 'https://www.linkedin.com/in/franciscoespinozag';
  const email = process.env.NEXT_PUBLIC_CONTACT_EMAIL || 'francisco_e3@hotmail.com';

  return (
    <footer className="site-footer" aria-label={t("Fin de página")}>
      <p>© {new Date().getFullYear()} Francisco Espinoza. {t("Todos los derechos reservados.")}</p>
      <p>{t("Desarrollado con Next.js · Diseñado con intención.")}</p>
      <nav aria-label={t("Redes y contacto")}>
        <a href={linkedin} target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
        <span aria-hidden="true">·</span>
        <a href="https://github.com/FranciscoEspinozaG" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
        <span aria-hidden="true">·</span>
        <a href={`mailto:${email}`}>Email ↗</a>
      </nav>
    </footer>
  );
}
