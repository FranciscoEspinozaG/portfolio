'use client';

import './project-card.css';

import type { Project } from '../../data/portfolio';
export default function ProjectCard({ project }: {
    project: Project;
}) {
    return (<figure className="project" data-project={project.id}>
      <img className="project-image" src={project.image.src} alt={project.image.alt} width={project.image.width} height={project.image.height}/>
      <figcaption className="glass parallax-caption" data-swiper-parallax-x="60%" data-swiper-parallax-duration="650">
        <h3>{project.url ? <a href={project.url} target="_blank" rel="noopener noreferrer">{project.title}</a> : project.title}</h3>
        <p>Plataforma:<br />
    <b>{project.platform}</b>
    </p>
        <p>Rol:<br />
    <b>{project.role}</b>
    </p>
      </figcaption>
    </figure>);
}
