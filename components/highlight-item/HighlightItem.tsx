import type { HighlightItemBase } from '../../data/portfolio';
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
  return (
    <div className={[styles.item, className].filter(Boolean).join(' ')} data-technology={id}>
      <strong className={styles.label}>{label}</strong>
      {description && <span className={styles.description}>{description}</span>}
    </div>
  );
}
