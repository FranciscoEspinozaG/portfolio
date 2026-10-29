'use client';
import { useLanguage } from '../LanguageProvider';
import { assetPath } from '../../lib/asset-path';


import './project-card.css';

import type { Project } from '../../interfaces/Project';
export default function ProjectCard({ project }: {
    project: Project;
}) {
  const { t } = useLanguage();
    return (<figure className="project" data-project={project.id}>
      <img className="project-image" src={assetPath(project.image.src)} alt={t(project.image.alt)} width={project.image.width} height={project.image.height}/>
      <figcaption className="glass parallax-caption" data-swiper-parallax-x="60%" data-swiper-parallax-duration="650">
        <h3>{project.url ? <a href={project.url} target="_blank" rel="noopener noreferrer">{project.title}</a> : project.title}</h3>
        <p>{t("Plataforma:")}<br />
    <b>{project.platform}</b>
    </p>
        <p>{t("Rol:")}<br />
    <b>{t(project.role)}</b>
    </p>
      </figcaption>
    </figure>);
}
