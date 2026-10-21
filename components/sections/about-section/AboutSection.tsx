import { about, stats } from '../../../data/portfolio';
import HighlightItem from '../../highlight-item/HighlightItem';
export default function AboutSection() {
    return <section tabIndex={0} aria-label="Acerca de mí" id="acerca" className="muted about">
        <div className="content">
            <h2>Acerca de mí</h2>
            <div className="stats">
                {stats.map(stat => (
                    <HighlightItem key={stat.id} {...stat} />
                ))}
            </div>
            <div className="copy about-copy">
                {about.map(p => 
                    <p key={p}>{p}</p>
                )}
            </div>
        </div>
    </section>;
}
