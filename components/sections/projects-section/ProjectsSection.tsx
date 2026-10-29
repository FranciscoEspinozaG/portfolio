'use client';
import { useLanguage } from '../../LanguageProvider';
import { projects } from '../../../data/portfolio';
import ProjectsCarousel from '../../projects-carousel/ProjectsCarousel';
export default function ProjectsSection() {
  const { t } = useLanguage();
    return (<section tabIndex={0} aria-label={t("Proyectos destacados")} id="proyectos" className="muted projects">
      <div className="content">
        <h2>{t("Proyectos")}<br />{t(" destacados")}</h2>
        <ProjectsCarousel projects={projects}/>
      </div>
    </section>);
}
