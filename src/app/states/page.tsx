import type { Metadata } from "next";
import Link from "next/link";
import { states, TOPICS, verifiedStates } from "@/lib/data";
import { Crumbs, LegalNote } from "@/components/ui";

export const metadata: Metadata = {
  title: "Landlord-tenant laws by state",
  description: "Security deposit limits, return deadlines, late fees, entry notice and month-to-month notice by state, each with a statute citation and official source link.",
  alternates: { canonical: "/states" },
};

export default function StatesPage() {
  const topicKeys = Object.keys(TOPICS);
  return (
    <div className="space-y-6">
      <Crumbs items={[["Home", "/"], ["States", null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">Landlord-tenant laws by state</h1>
      <p className="max-w-2xl text-slate-600">{verifiedStates.length} states verified so far. Other states are in the nightly queue and are published only after we read the official statute.</p>
      <LegalNote />
      <div className="overflow-x-auto">
        <table className="w-full min-w-[760px] text-left text-sm">
          <thead className="border-b-2 border-slate-900 text-xs uppercase tracking-wide text-slate-500">
            <tr><th className="py-2 pr-3">State</th>{topicKeys.map((t) => <th key={t} className="py-2 pr-3">{TOPICS[t]}</th>)}</tr>
          </thead>
          <tbody>
            {verifiedStates.map((s) => (
              <tr key={s.slug} className="border-b border-slate-200 align-top">
                <td className="py-2.5 pr-3"><Link href={`/states/${s.slug}`} className="font-medium hover:underline">{s.name}</Link></td>
                {topicKeys.map((t) => {
                  const r = s.rules.find((x) => x.topic === t);
                  return <td key={t} className="py-2.5 pr-3">{r ? <Link href={`/rules/${r.slug}`} className="hover:underline">{r.answer}</Link> : <span className="text-slate-400">Queued</span>}</td>;
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2 className="font-serif text-xl font-semibold">Queued states</h2>
      <p className="text-sm text-slate-600">{states.filter((s) => s.status === "queued").map((s, i) => <span key={s.slug}>{i > 0 && " · "}<Link href={`/states/${s.slug}`} className="hover:underline">{s.name}</Link></span>)}</p>
    </div>
  );
}
