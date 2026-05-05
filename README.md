# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-05 02:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | asteroid | 34.68% | $38,633,985 | $0.0004 |
| 2 | ton | 28.26% | $480,888,906 | $1.7500 |
| 3 | rave | 22.66% | $98,654,211 | $0.7588 |
| 4 | crclon | 19.58% | $13,329,573 | $125.1900 |
| 5 | pendle | 15.06% | $172,435,209 | $1.8500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | -32.84% | $89,296,247 | $1.7100 |
| 2 | bsb | -26.83% | $101,731,002 | $0.6190 |
| 3 | tag | -24.34% | $80,926,324 | $0.0013 |
| 4 | genius | -12.69% | $12,841,509 | $0.5474 |
| 5 | m | -10.45% | $57,044,798 | $2.6800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $83,520,346,967 | $0.9998 |
| 2 | btc | 0.86% | $47,999,765,809 | $80,471.0000 |
| 3 | eth | 0.59% | $20,739,300,608 | $2,369.6600 |
| 4 | usdc | 0.01% | $17,342,485,477 | $1.0000 |
| 5 | sol | -0.59% | $4,112,675,283 | $84.5000 |


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
