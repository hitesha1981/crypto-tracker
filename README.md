# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-15 02:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | br | 53.95% | $23,829,810 | $0.5074 |
| 2 | pons | 20.54% | $126,492,580 | $0.6332 |
| 3 | ai | 14.51% | $33,962,475 | $0.2837 |
| 4 | cards | 10.74% | $9,388,728 | $0.1359 |
| 5 | prl | 9.84% | $843,853 | $0.5596 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ff | -10.93% | $19,103,974 | $0.1266 |
| 2 | fil | -9.90% | $265,989,109 | $0.8955 |
| 3 | glm | -9.04% | $10,100,734 | $0.1178 |
| 4 | rain | -6.72% | $26,490,228 | $0.0142 |
| 5 | 牛来 | -6.15% | $47,376,764 | $0.1129 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $57,216,174,253 | $0.9998 |
| 2 | btc | 0.45% | $31,630,046,804 | $77,864.0000 |
| 3 | usdc | 0.01% | $17,983,792,629 | $0.9999 |
| 4 | eth | 0.24% | $16,104,420,305 | $2,512.2000 |
| 5 | xrp | 4.78% | $4,339,351,321 | $1.4300 |


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
