import { assetPath } from '../../../lib/asset-path';
export default function HeroSection() {
    return <section tabIndex={0} aria-label="Inicio" id="inicio" className="hero">
    <div className="content hero-content">
    <div className="portrait">
    <img src={assetPath("/assets/portrait.png")} alt="Francisco Espinoza" width="520" height="780"/>
    </div>
    <div className="hero-title">
    <h1>Francisco<br />Espinoza</h1>
    <p>Web developer <span>/</span> Graphic Designer</p>
    </div>
    </div>
    </section>;
}
