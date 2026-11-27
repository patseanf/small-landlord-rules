import type { Metadata } from "next";
import Link from "next/link";
import { comparisons, tools } from "@/lib/data";
import { AffiliateNote, Crumbs } from "@/components/ui";
import { formatDate } from "@/lib/site";

export const metadata: Metadata = {
  title: "Landlord app fees compared: screening, ACH, card and plan prices",
  description: "Published fees for TurboTenant, RentRedi, Avail, Innago, Baselane, Stessa, Rentec Direct, DoorLoop, Buildium and more, each linked to the provider's pricing page.",
  alternates: { canonical: "/tools" },
};

export default function ToolsPage() {
  return (
    <div className="space-y-6">
      <Crumbs items={[["Home", "/"], ["Landlord app fees", null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">Landlord app fees</h1>
      <p className="max-w-2xl text-slate-600">Plan prices and per-transaction fees as each provider publishes them, checked {formatDate(tools[0].checkedAt)}.</p>
      <AffiliateNote />
      <ul className="divide-y divide-slate-200 border-y border-slate-200">
        {tools.map((t) => (
          <li key={t.slug} className="grid gap-1 py-4 sm:grid-cols-[14rem_1fr] sm:gap-6">
            <div><Link href={`/tools/${t.slug}`} className="font-medium hover:underline">{t.name}</Link><div className="text-xs text-slate-500">{t.category}</div></div>
            <div className="text-sm text-slate-700">
              <p>{t.plans.map((p) => `${p.name}: ${p.price}`).join(" · ")}</p>
              <p className="text-slate-500">Screening: {t.screening} · ACH: {t.ach} · Card: {t.card}</p>
            </div>
          </li>
        ))}
      </ul>
      <h2 className="font-serif text-xl font-semibold">Comparisons</h2>
      <ul className="list-disc pl-5 text-sm">{comparisons.map((c) => <li key={c.slug}><Link href={`/compare/${c.slug}`} className="hover:underline">{c.title}</Link></li>)}</ul>
    </div>
  );
}
