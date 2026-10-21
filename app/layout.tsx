import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'Francisco Espinoza | Web Developer & Graphic Designer', description: 'Desarrollador Web, Full Stack y Tech Lead. Más de 9 años creando soluciones digitales, comercio electrónico y plataformas empresariales.' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="es" dir="ltr"><body>{children}</body></html>; }
