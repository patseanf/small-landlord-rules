import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { comparisons, getComparison, getTool, toolHref } from "@/lib/data";
import { AffiliateNote, Crumbs } from "@/components/ui";
import { formatDate } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() {
  return comparisons.map((c) => ({ slug: c.slug }));
}

export async function generateMetadata({ params }: PageProps<"/compare/[slug]">): Promise<Metadata> {
  const c = getComparison((await params).slug);
  if (!c) return {};
  return { title: c.title, description: c.summary, alternates: { canonical: `/compare/${c.slug}` } };
}

export default async function ComparePage({ params }: PageProps<"/compare/[slug]">) {
  const c = getComparison((await params).slug);
  if (!c) notFound();
  const pair = [getTool(c.a)!, getTool(c.b)!];
  const rows: [string, (t: (typeof pair)[number]) => React.ReactNode][] = [
    ["Plans", (t) => t.plans.map((p) => <div key={p.name}>{p.name}: {p.price}{p.note && <span className="text-slate-500"> ({p.note})</span>}</div>)],
    ["Tenant screening", (t) => t.screening],
    ["ACH / bank transfer", (t) => t.ach],
    ["Card payments", (t) => t.card],
    ["Best for", (t) => t.bestFor],
  ];
  return (
    <article className="space-y-6">
      <Crumbs items={[["Home", "/"], ["Landlord app fees", "/tools"], [c.title, null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">{c.title}</h1>
      <p className="max-w-3xl text-lg text-slate-700">{c.summary}</p>
      <AffiliateNote />
      <div className="overflow-x-auto">
        <table className="w-full min-w-[600px] text-left text-sm">
          <thead className="border-b-2 border-slate-900"><tr><th className="w-40 py-2" />{pair.map((t) => <th key={t.slug} className="py-2 pr-4 font-serif text-lg"><Link href={`/tools/${t.slug}`} className="hover:underline">{t.name}</Link></th>)}</tr></thead>
          <tbody>{rows.map(([label, f]) => <tr key={label} className="border-b border-slate-200 align-top"><th className="py-2.5 pr-4 font-medium">{label}</th>{pair.map((t) => <td key={t.slug} className="py-2.5 pr-4">{f(t)}</td>)}</tr>)}</tbody>
        </table>
      </div>
      <section>
        <h2 className="mb-2 font-serif text-xl font-semibold">Key differences</h2>
        <ul className="list-disc space-y-1 pl-5">{c.points.map((p) => <li key={p}>{p}</li>)}</ul>
      </section>
      <p className="text-sm text-slate-600">
        Sources: {pair.flatMap((t) => t.sources).map((s, i) => <span key={s.url}>{i > 0 && " · "}<a href={s.url} className="underline" rel="noopener" target="_blank">{s.label}</a></span>)} · Checked {formatDate(c.checkedAt)}.
      </p>
      <p className="flex flex-wrap gap-3">{pair.map((t) => <a key={t.slug} href={toolHref(t.slug)} rel="noopener sponsored" className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-700">Visit {t.name} →</a>)}</p>
    </article>
  );
}
