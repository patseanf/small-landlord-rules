import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { comparisonsFor, getTool, toolHref, tools } from "@/lib/data";
import { AffiliateNote, Crumbs } from "@/components/ui";
import { formatDate } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() {
  return tools.map((t) => ({ slug: t.slug }));
}

export async function generateMetadata({ params }: PageProps<"/tools/[slug]">): Promise<Metadata> {
  const t = getTool((await params).slug);
  if (!t) return {};
  return { title: `${t.name} fees and pricing`, description: `${t.name}: ${t.plans.map((p) => `${p.name} ${p.price}`).join(", ")}. Screening: ${t.screening}. Checked ${formatDate(t.checkedAt)}.`.slice(0, 300), alternates: { canonical: `/tools/${t.slug}` } };
}

export default async function ToolPage({ params }: PageProps<"/tools/[slug]">) {
  const t = getTool((await params).slug);
  if (!t) notFound();
  const rows: [string, string][] = [["Tenant screening", t.screening], ["ACH / bank transfer rent", t.ach], ["Card payments", t.card]];
  return (
    <article className="max-w-3xl space-y-6">
      <Crumbs items={[["Home", "/"], ["Landlord app fees", "/tools"], [t.name, null]]} />
      <header>
        <p className="text-sm font-medium uppercase tracking-wide text-slate-500">{t.category}</p>
        <h1 className="font-serif text-3xl font-semibold tracking-tight">{t.name} fees and pricing</h1>
        <p className="mt-2 text-slate-600">Best for: {t.bestFor}.</p>
      </header>
      <AffiliateNote />
      <section>
        <h2 className="mb-2 font-serif text-xl font-semibold">Plans</h2>
        <table className="w-full text-left text-sm">
          <tbody>
            {t.plans.map((p) => (
              <tr key={p.name} className="border-b border-slate-200"><th className="py-2 pr-4 font-medium">{p.name}</th><td className="py-2">{p.price}{p.note && <span className="block text-xs text-slate-500">{p.note}</span>}</td></tr>
            ))}
          </tbody>
        </table>
      </section>
      <section>
        <h2 className="mb-2 font-serif text-xl font-semibold">Per-use fees</h2>
        <table className="w-full text-left text-sm">
          <tbody>{rows.map(([k, v]) => <tr key={k} className="border-b border-slate-200"><th className="w-56 py-2 pr-4 font-medium">{k}</th><td className="py-2">{v}</td></tr>)}</tbody>
        </table>
        {t.notes.length > 0 && <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-slate-700">{t.notes.map((n) => <li key={n}>{n}</li>)}</ul>}
      </section>
      <section className="text-sm text-slate-600">
        <p>Sources: {t.sources.map((s, i) => <span key={s.url}>{i > 0 && " · "}<a href={s.url} className="underline" rel="noopener" target="_blank">{s.label}</a></span>)} · Checked {formatDate(t.checkedAt)}. &ldquo;Check provider&rdquo; means the provider doesn&apos;t publish that fee clearly; prices can change at any time.</p>
        <p className="mt-3"><a href={toolHref(t.slug)} rel="noopener sponsored" className="inline-block rounded-md bg-slate-900 px-4 py-2 font-medium text-white hover:bg-slate-700">Visit {t.name} →</a></p>
      </section>
      {comparisonsFor(t.slug).length > 0 && (
        <section><h2 className="mb-2 font-serif text-lg font-semibold">Compare</h2><ul className="list-disc pl-5 text-sm">{comparisonsFor(t.slug).map((c) => <li key={c.slug}><Link href={`/compare/${c.slug}`} className="hover:underline">{c.title}</Link></li>)}</ul></section>
      )}
    </article>
  );
}
