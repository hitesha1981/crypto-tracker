# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-06 01:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 33.60% | $84,149,809 | $0.5516 |
| 2 | 2z | 9.97% | $26,244,440 | $0.0865 |
| 3 | xpl | 7.51% | $91,072,314 | $0.1224 |
| 4 | gekko | 7.09% | $73,225 | $0.0000 |
| 5 | b | 6.94% | $7,296,608 | $0.1852 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kite | -12.03% | $61,959,427 | $0.1375 |
| 2 | rain | -10.16% | $24,124,127 | $0.0066 |
| 3 | river | -9.33% | $14,642,631 | $10.6600 |
| 4 | qrl | -8.82% | $51,467 | $1.5500 |
| 5 | zk | -7.20% | $22,425,876 | $0.0151 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $42,952,266,532 | $0.9997 |
| 2 | btc | 2.57% | $27,319,732,375 | $68,827.0000 |
| 3 | eth | 2.86% | $11,585,356,557 | $2,116.6000 |
| 4 | usdc | -0.03% | $6,309,118,707 | $0.9998 |
| 5 | sol | 1.55% | $2,298,955,872 | $81.8600 |


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
