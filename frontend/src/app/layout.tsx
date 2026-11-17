import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "WareTwin | Warehouse Digital Twin",
  description: "Warehouse operations, AGV fleet and simulation dashboard"
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
