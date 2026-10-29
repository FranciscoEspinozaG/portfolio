'use client';
import { useLanguage } from '../../LanguageProvider';
import { technologies } from '../../../data/portfolio';
import HighlightItem from '../../highlight-item/HighlightItem';
export default function TechnologiesSection() {
  const { t } = useLanguage();
    return <section tabIndex={0} aria-label={t("Tecnologías y habilidades")} id="tecnologias" className="skills">
    <div className="content">
    <h2>{t("Tecnologías y")}<br />{t(" habilidades")}</h2>
    <div className="technologies">{technologies.map(technology => <HighlightItem key={technology.id} {...technology}/>)}</div>
    <div className="copy columns">
    <div>
    <p>{t("A lo largo de mi trayectoria he trabajado con distintas tecnologías, frameworks y plataformas, adaptándome a las necesidades de cada proyecto.")}</p>
    <p>{t("Mi experiencia se concentra en el desarrollo web, las integraciones y las soluciones empresariales, combinando conocimientos técnicos con una visión orientada al diseño, la arquitectura y el liderazgo de equipos.")}</p>
    <p>{t("Gracias a mis habilidades de comunicación y liderazgo, he sido designado como mentor y encargado de onboarding para desarrolladores jr. y quienes ya cuentan con experiencia, pero son nuevos en estas plataformas de trabajo, como Magento y Liferay que son bastante acotadas y particulares en su desarrollo.")}</p>
    </div>
    <p>{t("Actualmente continúo ampliando mis conocimientos en desarrollo Full Stack, explorando nuevas tecnologías y fortaleciendo mis habilidades en backend, estoy constantemente tomando nuevos cursos y proyectos en los que pueda desarrollarme, abriendo las posibilidades de servicios que prestar.")}</p>
    </div>
    </div>
    </section>;
}
