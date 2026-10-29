'use client';
import { useLanguage } from '../../LanguageProvider';
import { experience } from '../../../data/portfolio';
import ExperienceItem from '../../experience-item/ExperienceItem';

export default function ExperienceSection() {
  const { t } = useLanguage();
  return (
    <section tabIndex={0} aria-label={t("Experiencia profesional")} id="experiencia" className="experience">
      <div className="content">
        <h2>{t("Experiencia")}<br />{t(" profesional")}</h2>
        <ol className="timeline">
          {experience.map(job => <ExperienceItem key={job.company} {...job} />)}
        </ol>
      </div>
    </section>
  );
}
