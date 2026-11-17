import Link from "next/link";

const metrics = [
  ["Active AGVs", "02", "Fleet connected"],
  ["Open tasks", "00", "Awaiting allocation"],
  ["Warehouse zones", "04", "Demo layout"],
  ["Simulation", "Ready", "Engine scaffold"]
];

export default function Home() {
  return <main>
    <header><div><div className="eyebrow">WareTwin / Operations platform</div><h1>Warehouse Digital Twin</h1><p>Observe warehouse activity, coordinate mobile robots, and test operational scenarios.</p></div><span className="pill">Development environment</span></header>
    <div className="layout">
      <nav className="card"><strong>Workspace</strong><Link href="/">Overview</Link><Link href="/dashboard/warehouse">Warehouse</Link><Link href="/dashboard/fleet">AGV Fleet</Link><Link href="/dashboard/tasks">Tasks</Link><Link href="/dashboard/analytics">Analytics</Link><Link href="/dashboard/scenarios">Scenarios</Link></nav>
      <section><div className="grid">{metrics.map(([label, value, note]) => <article className="card" key={label}><p>{label}</p><div className="metric">{value}</div><small>{note}</small></article>)}</div>
      <article className="card" style={{marginTop: 16}}><h2>System status</h2><p>Frontend shell is running. Connect the API and implement the domain workflows to populate live warehouse state.</p><span className="pill">Starter foundation</span></article></section>
    </div>
  </main>;
}
