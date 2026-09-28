"""Validate the public files against the anchors in the README. Run from the repo root: python analysis/verify.py"""
import pandas as pd

daily = pd.read_csv("data/lc_rates_daily_2026.csv", parse_dates=["date"]).set_index("date")
stocks = pd.read_csv("data/lc_rates_stock_sensitivity.csv")
sectors = pd.read_csv("data/lc_rates_sector_sensitivity.csv")

start, end = daily.loc["2026-02-27"], daily.iloc[-1]
bp = lambda col: round((end[col] - start[col]) * 100)
checks = {
    "daily rows": (len(daily), 266),
    "last date": (str(daily.index[-1].date()), "2026-09-23"),
    "stocks": (len(stocks), 923),
    "sectors": (len(sectors), 13),
    "10Y change since Feb 27 (bp)": (bp("DGS10"), 114),
    "10Y close on last date (%)": (round(end["DGS10"], 2), 5.11),
    "10Y real yield change (bp)": (bp("DFII10"), 104),
    "real-yield share of 10Y move (%)": (round(100 * bp("DFII10") / bp("DGS10")), 91),
    "sectors with positive median sensitivity": (sectors.loc[sectors.beta10 > 0, "sector"].tolist(), ["energy"]),
    "energy median % per +10bp": (round(sectors.set_index("sector").loc["energy", "beta10"], 2), 1.33),
}
ok = True
for name, (got, want) in checks.items():
    good = got == want
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  {name}: {got}" + ("" if good else f" (expected {want})"))
raise SystemExit(0 if ok else 1)
