import { useState, useEffect } from "react";

export default function App() {
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);

  // Fetch the JSON data bridge on component mount
  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}scraped_products.json`)
      .then((res) => res.json())
      .then((data) => {
        setProducts(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching scraped products:", err);
        setLoading(false);
      });
  }, []);

  // Filter products based on search input
  const filteredProducts = products.filter((item) =>
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
        <span className="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded-full border border-slate-700">
          {products.length} Items Live
        </span>

        <span className="text-xs bg-emerald-500/10 text-emerald-400 px-3 py-1 rounded-full border border-emerald-500/20 font-medium">
          {products.length} Active Openings
        </span>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-4xl w-full mx-auto p-4 flex flex-col gap-4">
        {/* Search Bar */}
        <div className="relative">
          <input
            type="text"
            placeholder="Search scraped data..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-slate-800/80 border border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all shadow-sm"
          />
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12 text-slate-400 animate-pulse">
            Loading your dashboard data...
          </div>
        )}

        {/* Empty State */}
        {!loading && filteredProducts.length === 0 && (
          <div className="text-center py-12 text-slate-400 bg-slate-800/40 rounded-xl border border-slate-800">
            No matching items found.
          </div>
        )}

        {/* Product Cards Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {!loading &&
            filteredProducts.map((item, index) => (
              <div
                key={index}
                className="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 flex flex-col justify-between gap-3 shadow-md hover:border-slate-600 transition-all"
              >
                <div className="flex flex-col gap-1">
                  <span className="text-xs font-semibold text-emerald-400 tracking-wider uppercase">
                    {item.Category || "Product"}
                  </span>
                  <h2 className="text-base font-medium text-slate-100 line-clamp-2">
                    {item.Title}
                  </h2>
                </div>

                <div className="flex items-center justify-between pt-2 border-t border-slate-700/40">
                  <span className="text-lg font-bold text-slate-50">
                    {item.Price_GBP}
                  </span>
                  {item.Link && (
                    <a
                      href={item.Link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs bg-emerald-500/10 text-emerald-400 hover:bg-emerald-500/20 px-3 py-1.5 rounded-lg border border-emerald-500/20 transition-all font-medium"
                    >
                      View Source
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
