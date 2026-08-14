# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-14 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 67.20% | $85,761,223 | $0.0069 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | fgrs | 22.00% | $891,789 | $31.7000 |
| 4 | h | 18.00% | $7,513,229 | $0.1066 |
| 5 | ethfi | 16.30% | $56,613,722 | $0.4410 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cys | -31.00% | $49,456,376 | $1.1600 |
| 2 | apr | -24.30% | $44,090,064 | $0.4685 |
| 3 | beat | -18.30% | $39,741,212 | $0.8591 |
| 4 | tel | -5.50% | $911,799 | $0.0015 |
| 5 | crv | -5.10% | $48,636,721 | $0.2529 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $29,466,278,368 | $0.9992 |
| 2 | btc | 0.10% | $18,837,308,838 | $63,460.0000 |
| 3 | usdc | 0.00% | $7,693,981,321 | $0.9996 |
| 4 | eth | 0.50% | $6,028,474,402 | $1,884.9200 |
| 5 | sol | 0.60% | $1,174,223,896 | $75.8800 |


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
