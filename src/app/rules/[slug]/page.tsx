import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getRule, rules } from "@/lib/data";
import { Crumbs, LegalNote, Source } from "@/components/ui";
import { CONTACT_EMAIL } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() {
  return rules.map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({ params }: PageProps<"/rules/[slug]">): Promise<Metadata> {
  const r = getRule((await params).slug);
  if (!r) return {};
  return { title: `${r.state.name} ${r.title.toLowerCase()} (${r.citation.split(" (")[0]})`, description: `${r.answer}. ${r.detail}`.slice(0, 300), alternates: { canonical: `/rules/${r.slug}` } };
}

export default async function RulePage({ params }: PageProps<"/rules/[slug]">) {
  const r = getRule((await params).slug);
  if (!r) notFound();
  const siblings = r.state.rules.filter((x) => x.slug !== r.slug);
  return (
    <article className="max-w-3xl space-y-6">
      <Crumbs items={[["Home", "/"], ["States", "/states"], [r.state.name, `/states/${r.state.slug}`], [r.title, null]]} />
      <header>
        <p className="text-sm font-medium uppercase tracking-wide text-slate-500">{r.state.name}</p>
        <h1 className="font-serif text-3xl font-semibold tracking-tight">{r.title}</h1>
      </header>
      <LegalNote />
      <section className="rounded-md border border-slate-200 bg-white p-5">
        <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Short answer</p>
        <p className="mt-1 font-serif text-2xl leading-snug">{r.answer}</p>
        <p className="mt-3 text-slate-700">{r.detail}</p>
      </section>
      <section className="space-y-2">
        <h2 className="font-serif text-xl font-semibold">What the law says</h2>
        <blockquote className="border-l-4 border-slate-300 pl-4 font-serif text-slate-800">&ldquo;{r.quote}&rdquo;</blockquote>
        <p className="text-sm"><strong>Citation:</strong> {r.citation}</p>
        <Source url={r.sourceUrl} name={r.sourceName} checkedAt={r.checkedAt} />
      </section>
      <p className="text-sm text-slate-600">Local ordinances can be stricter. Spot an error or a law change? <a className="underline" href={`mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(`Correction: ${r.slug}`)}`}>Email a correction</a>.</p>
      {siblings.length > 0 && (
        <nav aria-label={`More ${r.state.name} rules`}>
          <h2 className="mb-2 font-serif text-lg font-semibold">More {r.state.name} rules</h2>
          <ul className="space-y-1 text-sm">{siblings.map((x) => <li key={x.slug}><Link href={`/rules/${x.slug}`} className="hover:underline">{x.title}: {x.answer}</Link></li>)}</ul>
        </nav>
      )}
    </article>
  );
}
