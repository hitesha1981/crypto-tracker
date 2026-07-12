# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-12 02:01 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | 34.74% | $38,153,953 | $0.2144 |
| 2 | ultima | 11.65% | $9,630,344 | $2,409.9900 |
| 3 | zano | 11.46% | $1,428,473 | $10.3600 |
| 4 | bc | 10.29% | $124,999 | $0.0143 |
| 5 | theta | 8.09% | $31,745,476 | $0.1518 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -51.22% | $90,405,609 | $0.1101 |
| 2 | lab | -37.89% | $96,027,389 | $0.5334 |
| 3 | beat | -14.57% | $33,217,486 | $2.2300 |
| 4 | btw | -9.76% | $8,432,295 | $0.0583 |
| 5 | edge | -9.45% | $9,741,180 | $0.3685 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $29,413,830,894 | $0.9993 |
| 2 | btc | 0.16% | $16,388,752,544 | $64,082.0000 |
| 3 | usdc | -0.01% | $7,418,095,138 | $0.9998 |
| 4 | eth | 0.89% | $6,398,911,815 | $1,805.1300 |
| 5 | sol | -0.99% | $1,404,863,187 | $76.7600 |


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
