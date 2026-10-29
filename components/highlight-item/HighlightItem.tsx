'use client';
import { useLanguage } from '../LanguageProvider';
import type { HighlightItemBase } from '../../interfaces/HighlightItemBase';
import styles from './HighlightItem.module.css';

export interface HighlightItemProps extends HighlightItemBase {
  className?: string;
}

export default function HighlightItem({
  id,
  label,
  description,
  className,
}: HighlightItemProps) {
  const { t } = useLanguage();
  return (
    <div className={[styles.item, className].filter(Boolean).join(' ')} data-technology={id}>
      <strong className={styles.label}>{t(label)}</strong>
      {description && <span className={styles.description}>{t(description)}</span>}
    </div>
  );
}
