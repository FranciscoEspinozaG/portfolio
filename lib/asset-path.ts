/** Public assets need the deployment prefix when hosted below a repository path. */
export function assetPath(path: string): string {
  return `${process.env.NEXT_PUBLIC_BASE_PATH || ''}${path}`;
}
