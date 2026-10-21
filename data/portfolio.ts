export const about = ['Hola, soy Francisco.', 'Desarrollador Web | Full Stack & Tech Lead', 'Soy desarrollador web con más de 9 años de experiencia creando soluciones digitales, combinando mi formación como Diseñador Gráfico con el desarrollo de software y el liderazgo técnico.', 'A lo largo de mi carrera he trabajado en plataformas empresariales, comercio electrónico, integraciones de servicios y desarrollo de aplicaciones web, utilizando tecnologías como JavaScript, TypeScript, PHP, React, Angular, Vue, Magento y Liferay.', 'Mi experiencia se ha concentrado principalmente en el frontend, pero mi interés por comprender y construir soluciones completas me ha llevado a profundizar en el desarrollo backend, la arquitectura de software y las integraciones.', 'Actualmente curso Ingeniería en Informática en la Universidad Central de Chile, complementando mi experiencia profesional con nuevos conocimientos y fortaleciendo mi perfil Full Stack.', 'Me apasiona resolver problemas, aprender nuevas tecnologías y transformar ideas en soluciones funcionales, escalables y bien diseñadas.'];
export const experience = [{
    years: '2024 - 2026',
    company: 'Entelgy',
    roles: ['Senior Liferay Developer']
}, {
    years: '2022 - 2024',
    company: 'VASS',
    roles: ['Senior Liferay Developer', 'Senior Adobe Commerce Developer', 'Líder Técnico Adobe Commerce']
}, {
    years: '2019 - 2022',
    company: 'TEKPRO',
    roles: ['Adobe Commerce Developer', 'Líder Técnico Front Magento 1', 'Frontend developer Magento 2, Adobe Commerce']
},{
    years: '2019 - 2019',
    company: 'OQO',
    roles: ['Desarrollo de sitios para inmobiliarias integrando simuladores de cotización y formularios de contacto, optimizando e implementando flujos UX/UI.', 'Desarrollo e implementación de Woocommerce para tiendas.', 'Desarrollo de tótems digitales touch para salas de ventas.', 'Diseño e implementación de sitios desde 0 con herramientas como Adobe XD.', 'Implementación de herramientas para analítica y SEO.']
}];
export interface HighlightItemBase {
    id: string;
    label: string;
    description ? : string;
}
export const technologies: HighlightItemBase[] = [{
        id: 'javascript',
        label: 'Js'
    },
    {
        id: 'php',
        label: 'PHP'
    },
    {
        id: 'typescript',
        label: 'Ts'
    },
    {
        id: 'magento',
        label: 'Magento',
        description: 'Adobe Commerce'
    },
    {
        id: 'liferay',
        label: 'Liferay'
    },
    {
        id: 'java',
        label: 'Java'
    },
    {
        id: 'leadership',
        label: 'LT'
    },
    {
        id: 'css',
        label: 'CSS'
    },
];
export interface Project {
    id: string;
    title: string;
    image: {
        src: string;
        alt: string;
        width: number;
        height: number;
    };
    platform: string;
    role: string;
    url ? : string;
}
export const projects: Project[] = [
    {
        id: 'sentua',
        title: 'SENTUA',
        image: {
            src: '/assets/sentua.png',
            alt: 'Tienda online SENTUA, desarrollada en Adobe Commerce Cloud',
            width: 1071,
            height: 531,
        },
        platform: 'Adobe Commerce Cloud',
        role: 'Líder técnico.',
    },{
        id: 'SOUEAST',
        title: 'SOUEAST CHILE',
        image: {
            src: '/assets/soueastchile.png',
            alt: 'Página de marca en Chile para exponer vehículos, generar SEO y canal de cotización/contacto.',
            width: 1071,
            height: 531,
        },
        platform: 'Liferay DXP',
        role: 'Full stack developer'
    },{
        id: 'casaroyal',
        title: 'Casa Royal',
        image: {
            src: '/assets/casaroyal.png',
            alt: 'Tienda desarrollada en Adobe Commerce Cloud',
            width: 1071,
            height: 531,
        },
        platform: 'Adobe Commerce Cloud',
        role: 'Frontend developer'
    }
];
export const stats: HighlightItemBase[] = [
    {
        id: 'experience-years',
        label: '9+',
        description: 'Años de experiencia',
    },
    {
        id: 'web-development-start',
        label: '2017',
        description: 'Inicio en desarrollo web',
    },
    {
        id: 'tech-lead-years',
        label: '2+',
        description: 'Años de LT',
    },
];
export const sections = [{
        id: 'acerca',
        label: 'Acerca de mí'
    },
    {
        id: 'tecnologias',
        label: 'Tecnologías y habilidades'
    },
    {
        id: 'proyectos',
        label: 'Proyectos destacados'
    },
    {
        id: 'experiencia',
        label: 'Experiencia profesional'
    },
    {
        id: 'contacto',
        label: 'Contacto'
    },
];