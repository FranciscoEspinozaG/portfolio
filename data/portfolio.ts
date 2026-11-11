import type { HighlightItemBase } from '../interfaces/HighlightItemBase';
import type { Project } from '../interfaces/Project';

export const about = [
    'Hola, soy Francisco.',
    'Desarrollador Web | Full Stack & Tech Lead',
    'Soy desarrollador web con más de 9 años de experiencia creando soluciones digitales, combinando mi formación como Diseñador Gráfico con el desarrollo de software y el liderazgo técnico.',
    'A lo largo de mi carrera he trabajado en plataformas empresariales, comercio electrónico, integraciones de servicios y desarrollo de aplicaciones web, utilizando tecnologías como JavaScript, TypeScript, PHP, React, Angular, Vue, Magento y Liferay.',
    'Mi experiencia se ha concentrado principalmente en el frontend, pero mi interés por comprender y construir soluciones completas me ha llevado a profundizar en el desarrollo backend, la arquitectura de software y las integraciones.',
    'Actualmente curso Ingeniería en Informática en la Universidad Central de Chile, complementando mi experiencia profesional con nuevos conocimientos y fortaleciendo mi perfil Full Stack.',
    'Me apasiona resolver problemas, aprender nuevas tecnologías y transformar ideas en soluciones funcionales, escalables y bien diseñadas.'];
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
},{
    years: '2017 - 2019',
    company: 'Andina del Sud',
    roles: ['SEO excecutive', 'Web developer']
}];
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
            src: '/assets/soueast-chile.png',
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
            src: '/assets/casa-royal.png',
            alt: 'Tienda desarrollada en Adobe Commerce Cloud',
            width: 1071,
            height: 531,
        },
        platform: 'Adobe Commerce Cloud',
        role: 'Frontend developer'
    },{
        id: 'MiSERMIG',
        title: 'MiSERMIG',
        image: {
            src: '/assets/MiSERMIG.png',
            alt: 'Plataforma para gestión de migrantes en Chile.',
            width: 1071,
            height: 531,
        },
        platform: 'Liferay',
        role: 'Frontend developer'
    },{
        id: 'Tienda LEGO',
        title: 'Tienda LEGO',
        image: {
            src: '/assets/tienda-lego.png',
            alt: 'E-Commerce.',
            width: 1071,
            height: 531,
        },
        platform: 'Magento 2',
        role: 'Frontend developer'
    }
];
export const personalProjects: Project[] = [
    {
        id: 'ubuntu-home-server',
        title: 'Servidor Ubuntu en casa',
        platform: 'Ubuntu Server',
        role: 'Arquitecto',
        description: 'Configuré un servidor en casa reutilizando un computador antiguo e instalando Ubuntu Server sin interfaz gráfica. Lo administro exclusivamente mediante SSH desde mi computador personal, a través de la red local. Gracias a Cloudflare Tunnel, publico mis proyectos en mi dominio probae.cl y gestiono sus subdominios desde Cloudflare. Cada proyecto se ejecuta en su propio entorno con Docker, lo que me permite utilizar distintas tecnologías y configuraciones en un mismo servidor.'
    },
    {
        id: 'plataforma-evaluaciones',
        title: 'Plataforma de evaluaciones',
        platform: 'Angular / Spring Boot',
        role: 'Desarrollador',
        description: 'Desarrollé y desplegué en este servidor una plataforma para ayudar a mi esposa a crear evaluaciones. La plataforma genera un informe por candidato con respuestas correctas e incorrectas y porcentajes de acierto y error por sección o área. Como producto mínimo viable (MVP), cuenta con una única cuenta de administrador definida en el código y enlaces únicos para cada evaluación. A futuro, planeo incorporar un agente de inteligencia artificial que analice los resultados siguiendo las instrucciones de la evaluadora y genere informes más completos.'
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
        id: 'experiencia',
        label: 'Experiencia profesional'
    },
    {
        id: 'proyectos',
        label: 'Proyectos destacados'
    },
    {
        id: 'proyectos-personales',
        label: 'Proyectos personales'
    },
    {
        id: 'contacto',
        label: 'Contacto'
    },
];
