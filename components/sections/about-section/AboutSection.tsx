'use client';
import { useLanguage } from '../../LanguageProvider';
import { about, stats } from '../../../data/portfolio';
import HighlightItem from '../../highlight-item/HighlightItem';
export default function AboutSection() {
  const { t } = useLanguage();
    return <section tabIndex={0} aria-label={t("Acerca de mí")} id="acerca" className="muted about">
        <div className="content">
            <h2>{t("Acerca de mí")}</h2>
            <div className="stats">
                {stats.map(stat => (
                    <HighlightItem key={stat.id} {...stat} />
                ))}
            </div>
            <div className="copy about-copy">
                {about.map(p => 
                    <p key={p}>{t(p)}</p>
                )}
            </div>
        </div>
    </section>;
}
