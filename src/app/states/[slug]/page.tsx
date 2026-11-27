import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getState, states, TOPICS } from "@/lib/data";
import { Crumbs, LegalNote, Source } from "@/components/ui";
import { CONTACT_EMAIL, formatDate } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() {
  return states.map((s) => ({ slug: s.slug }));
}

export async function generateMetadata({ params }: PageProps<"/states/[slug]">): Promise<Metadata> {
  const s = getState((await params).slug);
  if (!s) return {};
  if (s.status !== "verified") return { title: `${s.name} landlord rules (coming soon)`, robots: { index: false }, alternates: { canonical: `/states/${s.slug}` } };
  return {
    title: `${s.name} landlord-tenant laws: deposits, late fees, notice`,
    description: `${s.name} landlord rules with statute citations: ${s.rules.map((r) => `${r.title.toLowerCase()} (${r.answer})`).join("; ")}.`.slice(0, 300),
    alternates: { canonical: `/states/${s.slug}` },
  };
}

export default async function StatePage({ params }: PageProps<"/states/[slug]">) {
  const s = getState((await params).slug);
  if (!s) notFound();
  return (
    <article className="space-y-6">
      <Crumbs items={[["Home", "/"], ["States", "/states"], [s.name, null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">{s.name} landlord-tenant rules</h1>
      <LegalNote />
      {s.status === "verified" ? (
        <>
          <p className="text-sm text-slate-500">{s.rules.length} rules verified against official sources on {formatDate(s.checkedAt!)}.</p>
          <dl className="divide-y divide-slate-200 border-y border-slate-200">
            {s.rules.map((r) => (
              <div key={r.slug} className="grid gap-1 py-4 sm:grid-cols-[14rem_1fr] sm:gap-6">
                <dt className="font-medium"><Link href={`/rules/${r.slug}`} className="hover:underline">{r.title}</Link></dt>
                <dd className="space-y-1">
                  <p className="font-serif text-lg leading-snug">{r.answer}</p>
                  <p className="text-sm text-slate-600">{r.citation}</p>
                  <Source url={r.sourceUrl} name={r.sourceName} checkedAt={r.checkedAt} />
                </dd>
              </div>
            ))}
          </dl>
          {s.pendingTopics.length > 0 && (
            <p className="text-sm text-slate-600">Not yet verified for {s.name}: {s.pendingTopics.map((t) => TOPICS[t].toLowerCase()).join(", ")}. These are in our queue; we don&apos;t publish a rule until we&apos;ve read the official text.</p>
          )}
        </>
      ) : (
        <p className="text-slate-600">We haven&apos;t verified {s.name} yet. It&apos;s in the nightly verification queue, and we only publish a rule after reading the official statute. Know the source? <a className="underline" href={`mailto:${CONTACT_EMAIL}`}>Tell us</a>.</p>
      )}
      <p className="text-sm text-slate-500">Cities and counties can add stricter rules (for example rent control or just-cause ordinances). Always check local law too.</p>
    </article>
  );
}
