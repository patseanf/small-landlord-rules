export const SITE_NAME = "Small Landlord Rules";
export const SITE_TAGLINE =
  "State landlord rules with statute citations, plus the real fees of landlord apps. Every number links to its official source and the date we checked it.";
export const CONTACT_EMAIL = "patseanf11-5ybtg6@mail.grokbot.com";
export const DISCLOSURE =
  "Some links to landlord software may become affiliate links. If you sign up through one, we may earn a commission at no extra cost to you. It never changes which fees we show. We list fees exactly as each provider publishes them.";
export const LEGAL =
  "Not legal advice. This is a plain-English summary of statute text for general information. Laws change, and cities and counties can add their own rules. Check the linked official source or ask a licensed attorney in your state before you act.";

export function siteUrl() {
  return (process.env.NEXT_PUBLIC_SITE_URL ?? "https://small-landlord-rules.vercel.app").replace(/\/$/, "");
}

export function formatDate(iso: string) {
  return new Date(`${iso}T12:00:00Z`).toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric", timeZone: "UTC" });
}
