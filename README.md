# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-09 01:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 33.19% | $76,708,546 | $0.2507 |
| 2 | gomining | 14.99% | $10,861,693 | $0.3291 |
| 3 | h | 13.48% | $29,872,059 | $0.1410 |
| 4 | stable | 13.29% | $27,449,617 | $0.0193 |
| 5 | ccd | 11.89% | $2,201,163 | $0.0102 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | -29.18% | $16,043,817 | $1.3100 |
| 2 | 2z | -6.48% | $11,580,191 | $0.0890 |
| 3 | zano | -5.44% | $1,320,999 | $8.4200 |
| 4 | whitewhale | -5.21% | $13,397,803 | $0.1250 |
| 5 | s | -5.18% | $23,169,553 | $0.0425 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $67,116,077,938 | $0.9994 |
| 2 | btc | 2.38% | $43,416,232,140 | $70,762.0000 |
| 3 | eth | 0.57% | $19,363,300,354 | $2,095.4500 |
| 4 | usdc | 0.01% | $4,953,989,826 | $0.9999 |
| 5 | sol | -0.01% | $3,434,858,825 | $87.5700 |


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
