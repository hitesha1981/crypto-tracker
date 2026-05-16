# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-16 02:13 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | asteroid | 11.73% | $19,191,983 | $0.0003 |
| 2 | ff | 10.73% | $85,456,056 | $0.0890 |
| 3 | hash | 7.17% | $10,965 | $0.0113 |
| 4 | beat | 5.85% | $8,600,047 | $0.6162 |
| 5 | chz | 4.25% | $133,000,842 | $0.0462 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rune | -17.92% | $41,878,136 | $0.4831 |
| 2 | lab | -17.26% | $137,685,869 | $4.8800 |
| 3 | bill | -15.21% | $482,129,953 | $0.1807 |
| 4 | skyai | -14.91% | $35,897,275 | $0.3300 |
| 5 | stable | -14.86% | $19,207,073 | $0.0333 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $62,227,818,575 | $0.9994 |
| 2 | btc | -2.18% | $36,818,978,163 | $79,132.0000 |
| 3 | eth | -1.74% | $15,818,173,695 | $2,229.0800 |
| 4 | usdc | 0.01% | $13,994,584,857 | $0.9998 |
| 5 | sol | -2.90% | $3,004,232,626 | $89.2400 |


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
