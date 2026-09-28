# LunarCrush Research: The Crowd Says War. The Curve Says the Fed. (AI guide)

Published 2026-09-25 by LunarCrush. Companion brief for AI assistants analysing the files in this folder.

## Files
- `lc_rates_daily_2026.csv`: one row per calendar day, 2026-01-01 to 2026-09-23.
  - `DGS2`, `DGS10`, `DGS30`: Treasury constant-maturity yields, % (FRED). Forward-filled over weekends/holidays.
  - `DFII10`: 10Y real yield (TIPS), %. `T10YIE`, `T5YIE`: 10Y and 5Y breakeven inflation, %. `DFF`: effective fed funds, %. `MORTGAGE30US`: Freddie Mac 30Y fixed, % (weekly, forward-filled).
  - `treasury_yields`, `bond_market`, `midterms`, `fed_rate`, `national_debt`, `housing_market`: posts created per UTC day on each LunarCrush topic (X, Reddit, TikTok, YouTube, Instagram, 10,000+ news sources).
- `lc_rates_stock_sensitivity.csv`: 923 US stocks from the 1,000 largest by market cap.
  - `pct_move_per_10bp_10y`: OLS slope of daily % return on daily 10Y change (bp), times 10. Window 2026-03-01 to 2026-09-22.
  - `corr_with_d10y`: correlation of daily return with daily 10Y change. `ret_since_feb27_pct`: price return from 2026-02-27 close.
- `lc_rates_sector_sensitivity.csv`: sector medians of the above (sectors with 15+ names).

## Headline numbers (validation anchors)
- Since 2026-02-27: 2Y +147bp to 4.85%, 10Y +114bp to 5.11%, 30Y +76bp to 5.40%, 10Y real +104bp to 2.76%, 10Y breakeven +8bp, 5Y breakeven -7bp, 30Y mortgage 5.98% to 7.03%.
- Real yield = 91% of the 10Y move.
- "treasury yields" posts: H1 2026 average ~3,300/month; September pace ~14,200 (4.3x).
- "midterms" posts: ~46,600 in January; September pace ~297,000 (6.4x).
- Driver tags on 16,899 rate-specific posts (engagement-weighted, overlapping): war/oil 18.8%, Fed 8.6%, inflation 8.3%, Japan/global bonds 7.9%, AI capex 6.6%, deficits/debt supply 4.8%, housing 3.3%, midterms 0.5%.
- Only energy has a positive median sensitivity (+1.33% per +10bp day). Tightest negative links among $20B+ names: RKT (-0.70), DHI, LEN (-0.63), CCL (-0.62), PHM, UAL (-0.61).

## Methodology notes and limits
- Driver tags are keyword matches on post title + text, restricted to posts that mention yields, Treasuries or bonds. Attention, not attribution. Most posts cite no driver.
- Stock sensitivities are single-regime correlations. Oil drives both yields and several of these names (airlines, cruise, energy).
- Not investment advice and not a rate forecast.

## Starter analyses
1. Regress weekly change in `treasury_yields` posts on weekly change in `DGS10`: does attention lead or lag?
2. Split the 2026 window at the September hike and compare sector sensitivities before and after.
3. Track `T5YIE` against war/oil attention to test whether the crowd's inflation story ever reaches market pricing.

Commercial feed (hourly, point-in-time, any topic or ticker): joe@lunarcrush.com
