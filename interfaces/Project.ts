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
    url?: string;
}
