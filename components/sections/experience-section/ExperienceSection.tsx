import { experience } from '../../../data/portfolio';
import ExperienceItem from '../../experience-item/ExperienceItem';

export default function ExperienceSection() {
  return (
    <section tabIndex={0} aria-label="Experiencia profesional" id="experiencia" className="experience">
      <div className="content">
        <h2>Experiencia<br /> profesional</h2>
        <ol className="timeline">
          {experience.map(job => <ExperienceItem key={job.company} {...job} />)}
        </ol>
      </div>
    </section>
  );
}
