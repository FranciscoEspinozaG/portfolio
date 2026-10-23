import type { Metadata } from 'next';
import { assetPath } from '../lib/asset-path';
import './globals.css';

const title = 'Francisco Espinoza | Web Developer & Graphic Designer';
const description = 'Desarrollador Web, Full Stack y Tech Lead. Más de 9 años creando soluciones digitales, comercio electrónico y plataformas empresariales.';
const socialImage = {
    url: assetPath('/assets/SEO-img.png'),
    width: 1200,
    height: 630,
    alt: title,
};

export const metadata: Metadata = {
    metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || 'https://franciscoespinozag.github.io'),
    title,
    description,
    openGraph: {
        type: 'website',
        locale: 'es_CL',
        title,
        description,
        images: [socialImage],
    },
    twitter: {
        card: 'summary_large_image',
        title,
        description,
        images: [socialImage],
    },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
    return <html lang="es" dir="ltr">

        <body>{children}</body>

    </html>;
}
