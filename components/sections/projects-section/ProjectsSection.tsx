import { projects } from '../../../data/portfolio';
import ProjectsCarousel from '../../projects-carousel/ProjectsCarousel';
export default function ProjectsSection() {
    return (<section tabIndex={0} aria-label="Proyectos destacados" id="proyectos" className="muted projects">
      <div className="content">
        <h2>Proyectos<br /> destacados</h2>
        <ProjectsCarousel projects={projects}/>
      </div>
    </section>);
}
