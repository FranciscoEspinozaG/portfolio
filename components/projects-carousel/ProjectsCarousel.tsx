'use client';

import './projects-carousel.css';
import { useId, useRef, useState } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { A11y, Keyboard, Parallax } from 'swiper/modules';
import type { Swiper as SwiperInstance } from 'swiper';
import type { Project } from '../../data/portfolio';
import ProjectCard from '../project-card/ProjectCard';
import 'swiper/css';
export default function ProjectsCarousel({ projects }: {
    projects: Project[];
}) {
    const id = useId();
    const swiper = useRef<SwiperInstance | null>(null);
    const [position, setPosition] = useState({ index: 0, beginning: true, end: projects.length <= 1 });
    const update = (instance: SwiperInstance) => {
        setPosition({ index: instance.activeIndex, beginning: instance.isBeginning, end: instance.isEnd });
    };
    if (!projects.length)
        return <p>Próximamente nuevos proyectos.</p>;
    return (<div className="projects-carousel" role="region" aria-label="Proyectos destacados" aria-roledescription="carrusel">
      <Swiper id={id} modules={[A11y, Keyboard, Parallax]} parallax watchSlidesProgress speed={650} slidesPerView={1} spaceBetween={24} keyboard={{ enabled: true, onlyInViewport: true }} watchOverflow a11y={{ slideLabelMessage: 'Proyecto {{index}} de {{slidesLength}}' }} onSwiper={instance => { swiper.current = instance; update(instance); }} onSlideChange={update} onUpdate={update}>
        {projects.map(project => (<SwiperSlide key={project.id}>
            <ProjectCard project={project}/>
          </SwiperSlide>))}
      </Swiper>
      <div className="project-controls">
        <img src="/assets/arrows.svg" alt=""/>
        <button type="button" aria-label="Proyecto anterior" aria-controls={id} disabled={position.beginning} onClick={() => swiper.current?.slidePrev()}/>
        <button type="button" aria-label="Proyecto siguiente" aria-controls={id} disabled={position.end} onClick={() => swiper.current?.slideNext()}/>
      </div>
      <p role="status" aria-live="polite" className="project-status">
        {position.index + 1} / {projects.length}
      </p>
    </div>);
}
