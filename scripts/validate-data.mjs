// Fails the build if any published rule or tool lacks an official source + checkedAt date.
import { readFileSync } from "node:fs";
const j = (f) => JSON.parse(readFileSync(new URL(`../data/${f}`, import.meta.url)));
const errs = [];
const date = /^\d{4}-\d{2}-\d{2}$/;
for (const s of j("states.json").states) for (const r of s.rules) {
  for (const k of ["citation", "sourceUrl", "checkedAt", "quote", "answer"]) if (!r[k]) errs.push(`${r.slug}: missing ${k}`);
  if (!date.test(r.checkedAt ?? "")) errs.push(`${r.slug}: bad checkedAt`);
  if (!/^https?:\/\//.test(r.sourceUrl ?? "")) errs.push(`${r.slug}: bad sourceUrl`);
}
const tools = j("tools.json").tools;
for (const t of tools) {
  if (!t.sources?.length || !date.test(t.checkedAt ?? "")) errs.push(`${t.slug}: missing sources/checkedAt`);
  for (const k of ["screening", "ach", "card"]) if (!t[k]) errs.push(`${t.slug}: empty ${k} (use "Check provider")`);
}
const slugs = new Set(tools.map((t) => t.slug));
for (const c of j("comparisons.json").comparisons) if (!slugs.has(c.a) || !slugs.has(c.b)) errs.push(`${c.slug}: unknown tool`);
const q = j("nightly-queue.json").items;
if (new Set(q.map((i) => i.id)).size !== q.length) errs.push("nightly-queue: duplicate ids");
if (errs.length) { console.error(errs.join("\n")); process.exit(1); }
console.log(`data ok: ${tools.length} tools, ${q.length} queued`);
