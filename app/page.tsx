import Footer from '../components/footer/Footer';
import Navigation from '../components/navigation/Navigation';
import HeroSection from '../components/sections/hero-section/HeroSection';
import AboutSection from '../components/sections/about-section/AboutSection';
import TechnologiesSection from '../components/sections/technologies-section/TechnologiesSection';
import ProjectsSection from '../components/sections/projects-section/ProjectsSection';
import ExperienceSection from '../components/sections/experience-section/ExperienceSection';
import ContactSection from '../components/sections/contact-section/ContactSection';

export default function Portfolio() {
  return (
    <>
      <Navigation />
      <main>
        <HeroSection />
        <AboutSection />
        <TechnologiesSection />
        <ProjectsSection />
        <ExperienceSection />
        <ContactSection />
      </main>
      <Footer />
    </>
  );
}
