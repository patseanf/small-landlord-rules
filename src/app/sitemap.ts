import type { MetadataRoute } from "next";
import { comparisons, rules, tools, verifiedStates } from "@/lib/data";
import { siteUrl } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = siteUrl();
  const latest = [...rules.map((r) => r.checkedAt), ...tools.map((t) => t.checkedAt)].sort().at(-1);
  const page = (path: string, priority: number, lastModified = latest) => ({ url: `${base}${path}`, lastModified, priority });
  return [
    page("/", 1), page("/states", 0.9), page("/tools", 0.9),
    ...verifiedStates.map((s) => page(`/states/${s.slug}`, 0.8, s.checkedAt ?? latest)),
    ...rules.map((r) => page(`/rules/${r.slug}`, 0.7, r.checkedAt)),
    ...tools.map((t) => page(`/tools/${t.slug}`, 0.7, t.checkedAt)),
    ...comparisons.map((c) => page(`/compare/${c.slug}`, 0.7, c.checkedAt)),
    page("/methodology", 0.3), page("/partners", 0.2),
  ];
}
