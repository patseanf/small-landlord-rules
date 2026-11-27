import type { Metadata } from "next";
import { Crumbs, LegalNote } from "@/components/ui";
import { changelog, queueCount } from "@/lib/data";
import { CONTACT_EMAIL, DISCLOSURE, formatDate } from "@/lib/site";

export const metadata: Metadata = { title: "Methodology and corrections", description: "How Small Landlord Rules verifies state statutes and landlord app fees.", alternates: { canonical: "/methodology" } };

export default function MethodologyPage() {
  return (
    <article className="max-w-2xl space-y-4">
      <Crumbs items={[["Home", "/"], ["Methodology", null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">Methodology</h1>
      <LegalNote />
      <h2 className="font-serif text-xl font-semibold">State rules</h2>
      <ul className="list-disc space-y-1 pl-5">
        <li>We read the statute on an official government site (state legislature code sites, or a state attorney general publication when the code site can&apos;t be reached).</li>
        <li>Every rule shows the citation, a short quote, the source link and the date we checked it.</li>
        <li>If we can&apos;t verify a rule cleanly, we don&apos;t publish it. It stays in the verification queue (currently {queueCount} items).</li>
        <li>If a statute is silent on a topic, we don&apos;t claim &ldquo;no limit&rdquo; unless an official source says so.</li>
        <li>We cover state law. Cities and counties can add stricter rules.</li>
      </ul>
      <h2 className="font-serif text-xl font-semibold">Software fees</h2>
      <ul className="list-disc space-y-1 pl-5">
        <li>Fees come from each provider&apos;s own pricing, FAQ or help-center pages, with the date checked.</li>
        <li>&ldquo;Check provider&rdquo; means the provider doesn&apos;t publish that fee clearly. We don&apos;t estimate.</li>
      </ul>
      <h2 className="font-serif text-xl font-semibold">Affiliate disclosure</h2>
      <p>{DISCLOSURE}</p>
      <h2 className="font-serif text-xl font-semibold">Corrections</h2>
      <p>Email <a className="underline" href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a> with the official source and we&apos;ll re-check it.</p>
      <h2 className="font-serif text-xl font-semibold">Changelog</h2>
      <ul className="list-disc pl-5 text-sm">{changelog.map((c) => <li key={c.date + c.title}>{formatDate(c.date)}: {c.title}</li>)}</ul>
    </article>
  );
}
