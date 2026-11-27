import type { Metadata, Viewport } from "next";
import { Inter, Source_Serif_4 } from "next/font/google";
import Link from "next/link";
import "./globals.css";
import { CONTACT_EMAIL, DISCLOSURE, SITE_NAME, SITE_TAGLINE, siteUrl } from "@/lib/site";

const inter = Inter({ variable: "--font-inter", subsets: ["latin"] });
const serif = Source_Serif_4({ variable: "--font-serif", subsets: ["latin"] });

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl()),
  verification: { google: "RLldSCuz5c0j9vn5a5Flb-N93SoGboyXzDmvB_eHs-c" },
  title: { default: `${SITE_NAME}: landlord laws by state & landlord app fees`, template: `%s | ${SITE_NAME}` },
  description: SITE_TAGLINE,
  openGraph: { siteName: SITE_NAME, type: "website", locale: "en_US" },
  alternates: { canonical: "/" },
};

export const viewport: Viewport = { themeColor: "#0f172a", width: "device-width", initialScale: 1 };

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={`${inter.variable} ${serif.variable} antialiased`}>
      <body className="flex min-h-screen flex-col font-sans">
        <header className="border-b border-slate-200 bg-white">
          <div className="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-x-6 gap-y-2 px-4 py-3">
            <Link href="/" className="flex items-center gap-2 font-serif text-lg font-semibold tracking-tight text-slate-900">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/icon.svg" alt="" width={24} height={24} className="h-6 w-6" />
              {SITE_NAME}
            </Link>
            <nav className="flex gap-5 text-sm text-slate-600">
              <Link href="/states" className="hover:text-slate-900">States</Link>
              <Link href="/tools" className="hover:text-slate-900">Landlord app fees</Link>
              <Link href="/methodology" className="hover:text-slate-900">Methodology</Link>
            </nav>
          </div>
        </header>
        <main className="mx-auto w-full max-w-5xl flex-1 px-4 py-8">{children}</main>
        <footer className="border-t border-slate-200 bg-white">
          <div className="mx-auto grid max-w-5xl gap-6 px-4 py-8 text-sm text-slate-600 sm:grid-cols-3">
            <div>
              <p className="font-serif font-semibold text-slate-900">{SITE_NAME}</p>
              <p className="mt-1">Not legal advice. Summaries of statute text and published fees, each linked to its official source with the date we checked it.</p>
            </div>
            <div className="flex flex-col gap-1">
              <Link href="/states" className="hover:text-slate-900">All states</Link>
              <Link href="/tools" className="hover:text-slate-900">Landlord app fees</Link>
              <Link href="/methodology" className="hover:text-slate-900">Methodology &amp; corrections</Link>
              <Link href="/partners" className="hover:text-slate-900">Partners</Link>
              <a href={`mailto:${CONTACT_EMAIL}`} className="hover:text-slate-900">Report an error</a>
            </div>
            <p><strong className="text-slate-800">FTC disclosure:</strong> {DISCLOSURE}</p>
          </div>
        </footer>
      </body>
    </html>
  );
}
