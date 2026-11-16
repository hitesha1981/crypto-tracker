# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-16 04:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ultima | 34.87% | $5,116,742 | $1,200.8700 |
| 2 | drv | 12.09% | $15,667,433 | $0.2843 |
| 3 | ff | 10.64% | $14,654,053 | $0.1010 |
| 4 | pearl | 6.30% | $19,952,079 | $1.6200 |
| 5 | strcx | 6.20% | $482,273 | $108.6200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -32.36% | $9,216,904 | $0.4791 |
| 2 | ake | -12.14% | $107,140,293 | $0.0094 |
| 3 | lit | -7.70% | $44,335,946 | $2.7600 |
| 4 | beam | -5.46% | $6,044,695 | $0.0039 |
| 5 | aero | -4.63% | $14,870,184 | $0.4197 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $47,770,825,436 | $0.9994 |
| 2 | btc | 0.33% | $32,190,392,545 | $64,967.0000 |
| 3 | eth | 0.31% | $11,804,505,455 | $1,821.9300 |
| 4 | usdc | -0.00% | $11,521,619,476 | $0.9997 |
| 5 | sol | 0.88% | $3,225,334,055 | $71.8700 |


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
