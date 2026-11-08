# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-08 03:43 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | met | 18.38% | $55,951,984 | $0.3263 |
| 2 | edge | 6.00% | $1,285,334 | $0.3299 |
| 3 | figr_heloc | 4.25% | $3,110,320 | $1.0660 |
| 4 | anvl | 3.69% | $91,945 | $0.0020 |
| 5 | dgai | 3.65% | $25,792,181 | $0.7706 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | geod | -14.79% | $16,510,052 | $0.2374 |
| 2 | pons | -12.14% | $14,737,195 | $0.1714 |
| 3 | ake | -11.40% | $94,471,633 | $0.0052 |
| 4 | npc | -6.06% | $1,687,288 | $0.0144 |
| 5 | nft | -6.04% | $9,318,728 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $18,928,754,423 | $0.9990 |
| 2 | btc | 0.05% | $10,823,156,597 | $75,784.0000 |
| 3 | usdc | -0.01% | $4,649,688,863 | $0.9996 |
| 4 | eth | -0.19% | $3,872,637,034 | $2,235.1300 |
| 5 | xrp | 0.62% | $1,114,179,351 | $1.1600 |


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
