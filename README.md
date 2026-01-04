# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-04 01:17 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | 59.98% | $145,361,887 | $6.3600 |
| 2 | render | 18.09% | $149,482,498 | $1.8100 |
| 3 | pippin | 14.72% | $32,786,983 | $0.4289 |
| 4 | wstx | 13.24% | $2,172 | $0.2988 |
| 5 | wlfi | 12.74% | $341,501,436 | $0.1747 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -26.15% | $33,550,235 | $13.7900 |
| 2 | stable | -8.99% | $44,680,279 | $0.0167 |
| 3 | lit | -4.78% | $16,411,034 | $2.5800 |
| 4 | hash | -4.22% | $6,279 | $0.0298 |
| 5 | dot | -3.05% | $155,182,254 | $2.1300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $47,200,176,687 | $0.9997 |
| 2 | btc | 1.17% | $26,557,114,183 | $91,228.0000 |
| 3 | eth | 0.80% | $14,104,555,274 | $3,154.7100 |
| 4 | usdc | 0.01% | $6,153,740,885 | $1.0000 |
| 5 | sol | 1.29% | $2,892,645,386 | $134.4600 |


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
