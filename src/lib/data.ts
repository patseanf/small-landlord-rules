import statesJson from "../../data/states.json";
import toolsJson from "../../data/tools.json";
import compJson from "../../data/comparisons.json";
import affJson from "../../data/affiliates.json";
import changelogJson from "../../data/changelog.json";
import queueJson from "../../data/nightly-queue.json";

export type Rule = {
  slug: string; topic: string; title: string; answer: string; detail: string; quote: string;
  citation: string; sourceUrl: string; sourceName: string; checkedAt: string;
};
export type State = {
  code: string; name: string; slug: string; status: "verified" | "queued";
  checkedAt: string | null; rules: Rule[]; pendingTopics: string[];
};
export type Plan = { name: string; price: string; note: string | null };
export type Tool = {
  slug: string; name: string; category: string; website: string; pricingUrl: string; plans: Plan[];
  screening: string; ach: string; card: string; notes: string[]; sources: { label: string; url: string }[];
  bestFor: string; checkedAt: string;
};
export type Comparison = { slug: string; a: string; b: string; title: string; summary: string; points: string[]; checkedAt: string };
export type AffiliateLink = { tool: string; name: string; url: string; affiliateUrl: string | null; affiliateStatus: string };

export const TOPICS = statesJson.topics as Record<string, string>;
export const states = statesJson.states as State[];
export const verifiedStates = states.filter((s) => s.status === "verified");
export const rules: (Rule & { state: State })[] = verifiedStates.flatMap((s) => s.rules.map((r) => ({ ...r, state: s })));
export const tools = toolsJson.tools as Tool[];
export const comparisons = compJson.comparisons as Comparison[];
export const changelog = changelogJson.entries as { date: string; type: string; title: string; paths: string[] }[];
export const queueCount = queueJson.items.length;

const links = affJson.links as AffiliateLink[];
/** Outbound link for a tool: affiliate link only once approved, otherwise the official site. */
export function toolHref(slug: string) {
  const l = links.find((x) => x.tool === slug);
  return l?.affiliateStatus === "active" && l.affiliateUrl ? l.affiliateUrl : (l?.url ?? tools.find((t) => t.slug === slug)?.website ?? "#");
}
export const getState = (slug: string) => states.find((s) => s.slug === slug);
export const getRule = (slug: string) => rules.find((r) => r.slug === slug);
export const getTool = (slug: string) => tools.find((t) => t.slug === slug);
export const getComparison = (slug: string) => comparisons.find((c) => c.slug === slug);
export const comparisonsFor = (toolSlug: string) => comparisons.filter((c) => c.a === toolSlug || c.b === toolSlug);
