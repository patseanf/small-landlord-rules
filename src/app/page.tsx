import Link from "next/link";
import { StateFilter } from "@/components/StateFilter";
import { AffiliateNote } from "@/components/ui";
import { changelog, comparisons, queueCount, rules, states, toolHref, tools, verifiedStates } from "@/lib/data";
import { formatDate } from "@/lib/site";

export default function Home() {
  // One rule per state, newest check first, so the list spans states.
  const recent = verifiedStates.map((s) => rules.find((r) => r.state.slug === s.slug)!).sort((a, b) => b.checkedAt.localeCompare(a.checkedAt)).slice(0, 8);
  return (
    <div className="space-y-12">
      <section>
        <h1 className="max-w-3xl font-serif text-3xl font-semibold tracking-tight sm:text-4xl">Landlord rules by state, with the statute behind every number.</h1>
        <p className="mt-3 max-w-2xl text-slate-600">
          Deposit limits, return deadlines, late fees, entry notice and month-to-month notice, read from official state code sites. Plus the real fees of {tools.length} landlord apps.{" "}
          <a href="#fees" className="font-medium text-slate-900 underline">Jump to the fee table ↓</a>
        </p>
        <p className="mt-2 text-sm text-slate-500">
          {verifiedStates.length} states verified · {rules.length} rules · {tools.length} tools · {queueCount} pages in the verification queue
        </p>
      </section>

      <section aria-labelledby="find">
        <h2 id="find" className="mb-3 font-serif text-xl font-semibold">Find your state</h2>
        <StateFilter rows={states.map((s) => ({ slug: s.slug, name: s.name, code: s.code, verified: s.status === "verified", ruleCount: s.rules.length }))} />
      </section>

      <section aria-labelledby="recent">
        <h2 id="recent" className="mb-3 font-serif text-xl font-semibold">Recently verified</h2>
        <ul className="divide-y divide-slate-200 border-y border-slate-200">
          {recent.map((r) => (
            <li key={r.slug} className="flex flex-wrap items-baseline justify-between gap-2 py-2.5">
              <Link href={`/rules/${r.slug}`} className="font-medium hover:underline">{r.state.name}: {r.title}</Link>
              <span className="text-sm text-slate-500">{r.answer} · <span className="whitespace-nowrap">{formatDate(r.checkedAt)}</span></span>
            </li>
          ))}
        </ul>
        {changelog[0] && <p className="mt-2 text-xs text-slate-500">Latest update {formatDate(changelog[0].date)}: {changelog[0].title}</p>}
      </section>

      <section id="fees" aria-labelledby="fees-h" className="scroll-mt-6">
        <h2 id="fees-h" className="mb-1 font-serif text-xl font-semibold">Landlord app fees</h2>
        <p className="mb-3 text-sm text-slate-600">Copied from each provider&apos;s own pricing page. &ldquo;Check provider&rdquo; means the provider doesn&apos;t publish it clearly.</p>
        <div className="overflow-x-auto">
          <table className="w-full min-w-[720px] text-left text-sm">
            <thead className="border-b-2 border-slate-900 text-xs uppercase tracking-wide text-slate-500">
              <tr><th className="py-2 pr-3">Tool</th><th className="py-2 pr-3">Plans</th><th className="py-2 pr-3">Screening</th><th className="py-2 pr-3">ACH rent</th><th className="py-2">Card</th></tr>
            </thead>
            <tbody>
              {tools.map((t) => (
                <tr key={t.slug} className="border-b border-slate-200 align-top">
                  <td className="py-2.5 pr-3"><Link href={`/tools/${t.slug}`} className="font-medium hover:underline">{t.name}</Link><div className="text-xs text-slate-500">{t.category}</div></td>
                  <td className="py-2.5 pr-3">{t.plans.map((p) => <div key={p.name}>{p.name}: {p.price}</div>)}</td>
                  <td className="py-2.5 pr-3">{t.screening}</td>
                  <td className="py-2.5 pr-3">{t.ach}</td>
                  <td className="py-2.5">{t.card}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-2 text-xs text-slate-500">All fees checked {formatDate(tools[0].checkedAt)}. Official sites: {tools.map((t, i) => <span key={t.slug}>{i > 0 && ", "}<a href={toolHref(t.slug)} rel="noopener sponsored" className="underline">{t.name}</a></span>)}.</p>
        <div className="mt-4"><AffiliateNote /></div>
      </section>

      <section aria-labelledby="cmp">
        <h2 id="cmp" className="mb-3 font-serif text-xl font-semibold">Head-to-head</h2>
        <ul className="grid gap-3 sm:grid-cols-3">
          {comparisons.map((c) => (
            <li key={c.slug}><Link href={`/compare/${c.slug}`} className="block rounded-md border border-slate-200 bg-white p-4 hover:border-slate-900"><span className="font-medium">{c.title}</span><span className="mt-1 block text-sm text-slate-600">{c.summary}</span></Link></li>
          ))}
        </ul>
      </section>
    </div>
  );
}
