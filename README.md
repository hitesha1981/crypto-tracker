# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-20 02:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xtusd | 418.77% | $64 | $5.2600 |
| 2 | b | 28.08% | $48,021,444 | $0.2234 |
| 3 | pump | 23.50% | $110,391,592 | $0.0020 |
| 4 | trac | 16.29% | $45,087,164 | $0.3050 |
| 5 | kaito | 15.29% | $79,531,390 | $0.9662 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xec | -14.18% | $43,095,635 | $0.0000 |
| 2 | bp | -9.69% | $2,339,511 | $0.4358 |
| 3 | us | -8.37% | $11,471,695 | $0.0445 |
| 4 | hash | -6.44% | $2,942 | $0.0083 |
| 5 | edge | -6.39% | $4,285,551 | $0.4050 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $27,544,237,547 | $0.9992 |
| 2 | btc | -0.04% | $17,069,701,176 | $64,836.0000 |
| 3 | eth | 0.42% | $7,455,444,649 | $1,876.7000 |
| 4 | usdc | -0.01% | $5,722,829,477 | $0.9998 |
| 5 | sol | 1.05% | $1,385,960,655 | $76.8300 |


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
