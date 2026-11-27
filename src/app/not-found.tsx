import Link from "next/link";
export default function NotFound() {
  return <div className="py-16 text-center"><h1 className="font-serif text-2xl font-semibold">Page not found</h1><p className="mt-2"><Link href="/states" className="underline">Browse states</Link> or <Link href="/tools" className="underline">landlord app fees</Link>.</p></div>;
}
