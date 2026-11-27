"use client";
import Link from "next/link";
import { useState } from "react";

type Row = { slug: string; name: string; code: string; verified: boolean; ruleCount: number };

export function StateFilter({ rows }: { rows: Row[] }) {
  const [q, setQ] = useState("");
  const [onlyVerified, setOnlyVerified] = useState(false);
  const needle = q.trim().toLowerCase();
  const shown = rows.filter(
    (r) => (!onlyVerified || r.verified) && (!needle || r.name.toLowerCase().includes(needle) || r.code.toLowerCase() === needle),
  );
  return (
    <div>
      <div className="flex flex-wrap items-center gap-3">
        <label htmlFor="state-q" className="sr-only">Find your state</label>
        <input id="state-q" type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Find your state (e.g. Texas or TX)"
          className="w-full max-w-sm rounded-md border border-slate-300 bg-white px-3 py-2 text-sm focus:border-slate-900 focus:outline-none" />
        <label className="flex items-center gap-2 text-sm text-slate-600">
          <input type="checkbox" checked={onlyVerified} onChange={(e) => setOnlyVerified(e.target.checked)} /> Verified only
        </label>
      </div>
      <ul className="mt-4 grid grid-cols-2 gap-x-6 gap-y-1 text-sm sm:grid-cols-3 lg:grid-cols-4">
        {shown.map((r) => (
          <li key={r.slug}>
            <Link href={`/states/${r.slug}`} className="flex items-baseline justify-between gap-2 border-b border-slate-100 py-1.5 hover:text-slate-900">
              <span className={r.verified ? "font-medium text-slate-900" : "text-slate-500"}>{r.name}</span>
              <span className="text-xs text-slate-400">{r.verified ? `${r.ruleCount} rules` : "queued"}</span>
            </Link>
          </li>
        ))}
        {shown.length === 0 && <li className="text-slate-500">No match.</li>}
      </ul>
    </div>
  );
}
