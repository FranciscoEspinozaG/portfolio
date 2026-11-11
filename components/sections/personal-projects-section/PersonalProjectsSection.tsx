'use client';

import { useLanguage } from '../../LanguageProvider';
import { personalProjects } from '../../../data/portfolio';
import './personal-projects-section.css';

export default function PersonalProjectsSection() {
  const { t } = useLanguage();

  return (
    <section tabIndex={0} aria-labelledby="personal-projects-title" id="proyectos-personales" className="personal-projects">
      <div className="content">
        <h2 id="personal-projects-title">{t('Proyectos personales')}</h2>
        <div className="personal-projects-list">
          {personalProjects.map(project => (
            <article key={project.id} className="personal-project" aria-labelledby={`personal-project-${project.id}`}>
              <h3 id={`personal-project-${project.id}`}>
                {project.url ? <a href={project.url} target="_blank" rel="noopener noreferrer">{t(project.title)}</a> : t(project.title)}
              </h3>
              <dl>
                <div><dt>{t('Plataforma')}</dt><dd>{project.platform}</dd></div>
                <div><dt>{t('Rol')}</dt><dd>{t(project.role)}</dd></div>
              </dl>
              {project.description && <p className="personal-project-description">{t(project.description)}</p>}
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
