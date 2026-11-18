# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-18 05:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 21.42% | $24,632,893 | $0.4382 |
| 2 | sent | 12.54% | $14,330,026 | $0.0197 |
| 3 | pearl | 8.85% | $24,227,987 | $1.8400 |
| 4 | br | 7.50% | $2,238,164 | $0.4617 |
| 5 | pieverse | 7.35% | $22,479,284 | $2.1600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | -23.09% | $11,369,082 | $0.0047 |
| 2 | stable | -16.80% | $7,307,316 | $0.0203 |
| 3 | zro | -9.69% | $51,888,533 | $1.3600 |
| 4 | night | -8.89% | $23,985,283 | $0.0446 |
| 5 | anvl | -7.83% | $74,404 | $0.0014 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $51,515,023,083 | $0.9992 |
| 2 | btc | -0.38% | $33,104,807,237 | $64,684.0000 |
| 3 | usdc | -0.01% | $12,748,076,730 | $0.9995 |
| 4 | eth | -1.44% | $11,900,207,957 | $1,812.4400 |
| 5 | sol | 3.06% | $2,923,363,927 | $75.3100 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key

[coingecko-api-key-docs](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)

## Requirements to setup
## 1. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 2. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add pandas requests matplotlib python-dotenv
```


---

## 4. Update coingecko demo key in .env ( I have provided in .env.sample)
```bash
cat .env
CGK_API_DEMO_KEY="Your-coingecko-demo-api-key-here"
```

---

## 3. To manually run the script
```bash
python3.12 main.py
```
---
