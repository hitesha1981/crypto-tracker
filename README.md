# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-21 01:57 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bank | 26.73% | $171,947,844 | $0.2810 |
| 2 | ub | 16.53% | $10,979,579 | $0.1014 |
| 3 | bonk | 16.33% | $111,916,914 | $0.0000 |
| 4 | ldo | 11.93% | $41,721,668 | $0.3941 |
| 5 | b | 10.18% | $34,974,822 | $0.2459 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | night | -31.73% | $92,250,822 | $0.0183 |
| 2 | us | -14.79% | $11,279,264 | $0.0383 |
| 3 | adi | -6.99% | $8,238,632 | $6.7300 |
| 4 | tag | -6.17% | $4,110,595 | $0.0011 |
| 5 | rif | -5.85% | $8,464,051 | $0.1213 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $47,203,049,539 | $0.9992 |
| 2 | btc | 1.02% | $31,230,887,849 | $65,213.0000 |
| 3 | usdc | 0.00% | $12,131,018,530 | $0.9999 |
| 4 | eth | 2.13% | $10,372,268,769 | $1,906.9900 |
| 5 | sol | 1.86% | $1,929,745,398 | $77.8600 |


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
