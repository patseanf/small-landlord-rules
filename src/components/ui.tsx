import Link from "next/link";
import { DISCLOSURE, LEGAL, formatDate } from "@/lib/site";

export function LegalNote() {
  return (
    <aside role="note" className="rounded-md border border-amber-300 bg-amber-50 p-3 text-sm text-amber-950">
      <strong>Not legal advice.</strong> {LEGAL.replace(/^Not legal advice\. /, "")}
    </aside>
  );
}

export function AffiliateNote() {
  return (
    <aside role="note" className="rounded-md border border-slate-200 bg-slate-50 p-3 text-sm text-slate-700">
      <strong>Affiliate disclosure:</strong> {DISCLOSURE}
    </aside>
  );
}

export function Source({ url, name, checkedAt }: { url: string; name: string; checkedAt: string }) {
  return (
    <p className="text-xs text-slate-500">
      Source: <a href={url} className="underline decoration-slate-300 hover:text-slate-900" rel="noopener" target="_blank">{name}</a> · Checked {formatDate(checkedAt)}
    </p>
  );
}

export function Crumbs({ items }: { items: [string, string | null][] }) {
  return (
    <nav aria-label="Breadcrumb" className="mb-4 text-sm text-slate-500">
      {items.map(([label, href], i) => (
        <span key={label}>
          {i > 0 && <span className="mx-1.5 text-slate-300">/</span>}
          {href ? <Link href={href} className="hover:text-slate-900">{label}</Link> : <span className="text-slate-700">{label}</span>}
        </span>
      ))}
    </nav>
  );
}

export function Pill({ children, tone = "slate" }: { children: React.ReactNode; tone?: "slate" | "green" | "amber" }) {
  const c = { slate: "bg-slate-100 text-slate-700", green: "bg-emerald-50 text-emerald-800 ring-1 ring-emerald-200", amber: "bg-amber-50 text-amber-900 ring-1 ring-amber-200" }[tone];
  return <span className={`inline-block rounded px-1.5 py-0.5 text-xs font-medium ${c}`}>{children}</span>;
}
