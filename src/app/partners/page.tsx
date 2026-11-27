import type { Metadata } from "next";
import { Crumbs } from "@/components/ui";
import { CONTACT_EMAIL, DISCLOSURE } from "@/lib/site";

export const metadata: Metadata = { title: "Partners", description: "Partner with Small Landlord Rules: how listings, corrections and referral partnerships work.", alternates: { canonical: "/partners" } };

export default function PartnersPage() {
  return (
    <article className="max-w-2xl space-y-4">
      <Crumbs items={[["Home", "/"], ["Partners", null]]} />
      <h1 className="font-serif text-3xl font-semibold tracking-tight">Partners</h1>
      <p>Small Landlord Rules is a reference site for independent landlords: state rules with statute citations, and landlord-app fees copied from providers&apos; own pricing pages.</p>
      <h2 className="font-serif text-xl font-semibold">For software and service providers</h2>
      <ul className="list-disc space-y-1 pl-5">
        <li>We list published fees exactly as they appear on your pricing page, with a link and the date checked.</li>
        <li>If a fee is wrong or out of date, send us the official URL and we&apos;ll re-check it.</li>
        <li>We&apos;re open to referral partnerships. A partnership never changes the fees we show or how we rank anything.</li>
      </ul>
      <p className="rounded-md border border-slate-200 bg-white p-4">Contact: <a href={`mailto:${CONTACT_EMAIL}`} className="font-medium underline">{CONTACT_EMAIL}</a></p>
      <p className="text-sm text-slate-600"><strong>Disclosure:</strong> {DISCLOSURE}</p>
    </article>
  );
}
