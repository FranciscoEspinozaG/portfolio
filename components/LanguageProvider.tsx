"use client";
import { createContext, useContext, useEffect, useState } from 'react';
import { english } from '../lib/translations';
type Language = 'es' | 'en';
const LanguageContext = createContext({ language: 'es' as Language, setLanguage: (_language: Language) => {}, t: (text: string): string => text });
export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguage] = useState<Language>('es');
  useEffect(() => {
    try { if (localStorage.getItem('portfolio-language') === 'en') setLanguage('en'); } catch {}
  }, []);
  useEffect(() => { document.documentElement.lang = language; }, [language]);
  const changeLanguage = (value: Language) => {
    setLanguage(value);
    try { localStorage.setItem('portfolio-language', value); } catch {}
  };
  return <LanguageContext.Provider value={{ language, setLanguage: changeLanguage, t: text => language === 'en' ? english[text] ?? text : text }}>{children}</LanguageContext.Provider>;
}
export const useLanguage = () => useContext(LanguageContext);
