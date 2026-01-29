# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-29 01:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stable | 23.04% | $49,543,225 | $0.0274 |
| 2 | wld | 20.80% | $644,453,782 | $0.5600 |
| 3 | kite | 16.43% | $159,311,047 | $0.1444 |
| 4 | xcn | 14.00% | $22,492,637 | $0.0073 |
| 5 | jst | 9.21% | $42,101,660 | $0.0448 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -35.00% | $99,589,737 | $47.1600 |
| 2 | ab | -25.93% | $15,706,566 | $0.0029 |
| 3 | pippin | -15.91% | $95,731,968 | $0.4051 |
| 4 | axs | -13.80% | $262,843,861 | $2.1200 |
| 5 | kaia | -11.20% | $32,002,747 | $0.0647 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $75,572,416,703 | $0.9986 |
| 2 | btc | -0.39% | $45,393,019,170 | $88,926.0000 |
| 3 | eth | -0.42% | $22,385,043,548 | $2,998.7000 |
| 4 | usdc | -0.01% | $9,774,213,602 | $0.9996 |
| 5 | sol | -1.79% | $3,803,796,039 | $124.7100 |


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
