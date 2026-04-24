# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-24 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | om | 313.22% | $6,492 | $0.0668 |
| 2 | stable | 57.45% | $62,266,969 | $0.0414 |
| 3 | spk | 34.96% | $766,333,222 | $0.0512 |
| 4 | skyai | 27.79% | $36,273,982 | $0.2128 |
| 5 | lunc | 21.42% | $41,403,623 | $0.0001 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | asteroid | -30.20% | $71,230,965 | $0.0003 |
| 2 | chip | -25.78% | $1,369,690,301 | $0.0996 |
| 3 | pieverse | -17.16% | $58,706,305 | $0.8576 |
| 4 | strk | -7.74% | $127,581,295 | $0.0426 |
| 5 | mon | -7.36% | $63,528,486 | $0.0315 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $67,672,866,936 | $1.0000 |
| 2 | btc | 0.12% | $40,106,589,458 | $78,450.0000 |
| 3 | eth | -1.42% | $17,597,756,311 | $2,333.2200 |
| 4 | usdc | 0.01% | $15,883,506,400 | $0.9999 |
| 5 | sol | -0.17% | $3,757,641,172 | $86.3000 |


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
