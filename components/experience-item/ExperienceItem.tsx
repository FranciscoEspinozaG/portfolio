
import './experience-item.css';
export interface ExperienceItemProps {
  years: string;
  company: string;
  roles: readonly string[];
}

export default function ExperienceItem({ years, company, roles }: ExperienceItemProps) {
  return (
    <li className="experience-item">
      <div className="timeline-mark" aria-hidden="true">
        <img src="/assets/dot.svg" alt="" />
        <div className="timeline-line"><img src="/assets/line.svg" alt="" /></div>
      </div>
      <div>
        <h3>{years}</h3>
        <p className="company">{company}</p>
        <p className="roles">{roles.map(role => <span key={role}>{role}</span>)}</p>
      </div>
    </li>
  );
}
