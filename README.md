# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-22 03:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | 49.19% | $42,504,976 | $0.1200 |
| 2 | lab | 17.47% | $73,813,961 | $15.5200 |
| 3 | eigen | 13.94% | $100,155,811 | $0.2983 |
| 4 | 2z | 9.11% | $27,271,733 | $0.0767 |
| 5 | skyai | 8.33% | $16,247,411 | $0.3847 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -19.66% | $81,176,914 | $0.0989 |
| 2 | re | -12.84% | $239,437,355 | $0.8772 |
| 3 | axs | -12.01% | $48,724,012 | $1.0350 |
| 4 | bp | -9.49% | $10,965,116 | $0.6165 |
| 5 | dexe | -8.61% | $13,090,140 | $13.5300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $34,658,329,276 | $0.9988 |
| 2 | btc | -0.10% | $19,895,105,932 | $64,266.0000 |
| 3 | eth | -0.02% | $10,643,451,013 | $1,735.8200 |
| 4 | usdc | -0.01% | $6,676,067,798 | $0.9997 |
| 5 | sol | 0.32% | $2,293,550,813 | $73.8200 |


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
