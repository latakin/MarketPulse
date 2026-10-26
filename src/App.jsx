import { useState, useEffect } from "react";

export default function App() {
  const [jobs, setJobs] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);

  // Fetch the JSON data bridge on component mount with cache-busting timestamp
  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}scraped_products.json?t=${Date.now()}`)
      .then((res) => res.json())
      .then((data) => {
        setJobs(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching job listings:", err);
        setLoading(false);
      });
  }, []);

  // Filter job listings based on search input
  const filteredJobs = jobs.filter((item) =>
    Object.values(item).some((val) =>
      String(val).toLowerCase().includes(searchTerm.toLowerCase()),
    ),
  );

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans">
      {/* Sticky Header */}
      <header className="sticky top-0 z-10 bg-slate-950/80 backdrop-blur-md border-b border-slate-800 px-4 py-3 flex items-center justify-between">
        <h1 className="text-xl font-bold tracking-tight text-emerald-400">
          MarketPulse
        </h1>
        <span className="text-xs bg-emerald-500/10 text-emerald-400 px-3 py-1 rounded-full border border-emerald-500/20 font-medium">
          {jobs.length} Active Openings
        </span>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-4xl w-full mx-auto p-4 flex flex-col gap-4">
        {/* Search Bar */}
        <div className="relative">
          <input
            type="text"
            placeholder="Search titles, roles, locations, or skills..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-800/80 border border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all shadow-sm"
          />
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12 text-slate-400 animate-pulse">
            Loading job listings...
          </div>
        )}

        {/* Empty State */}
        {!loading && filteredJobs.length === 0 && (
          <div className="text-center py-12 text-slate-400 bg-slate-800/40 rounded-xl border border-slate-800">
            No matching technical roles found.
          </div>
        )}

        {/* Job Cards Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {!loading &&
            filteredJobs.map((item, index) => (
              <div
                key={index}
                className="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 flex flex-col justify-between gap-3 shadow-md hover:border-slate-600 transition-all"
              >
                <div className="flex flex-col gap-1.5">
                  <span className="text-xs font-semibold text-emerald-400 tracking-wider uppercase">
                    {item.Category || "Technical / Engineering"}
                  </span>
                  <h2 className="text-base font-medium text-slate-100 line-clamp-2">
                    {item.Title}
                  </h2>
                </div>

                <div className="flex items-center justify-between pt-2 border-t border-slate-700/40">
                  <span className="text-xs font-medium text-slate-400 flex items-center gap-1">
                    📍 {item.Price_GBP}
                  </span>
                  {item.Link && (
                    <a
                      href={item.Link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs bg-emerald-500/10 text-emerald-400 hover:bg-emerald-500/20 px-3 py-1.5 rounded-lg border border-emerald-500/20 transition-all font-medium"
                    >
                      View Role
                    </a>
                  )}
                </div>
              </div>
            ))}
        </div>
      </main>
    </div>
  );
}
