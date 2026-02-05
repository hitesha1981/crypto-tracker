# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-05 01:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 17.06% | $55,352,011 | $14.6500 |
| 2 | mon | 7.94% | $139,261,851 | $0.0193 |
| 3 | h | 7.20% | $68,096,734 | $0.1173 |
| 4 | ray | 7.12% | $80,212,639 | $0.7386 |
| 5 | b | 7.04% | $5,550,594 | $0.1901 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zec | -10.51% | $460,372,614 | $250.1600 |
| 2 | stx | -9.37% | $35,537,794 | $0.2801 |
| 3 | bnb | -9.04% | $2,416,806,150 | $692.4200 |
| 4 | hash | -9.01% | $17,613 | $0.0195 |
| 5 | pendle | -8.89% | $54,949,681 | $1.4200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.08% | $126,092,983,712 | $0.9979 |
| 2 | btc | -5.57% | $73,917,351,063 | $72,355.0000 |
| 3 | eth | -6.12% | $44,888,906,794 | $2,136.9800 |
| 4 | usdc | -0.00% | $14,615,545,377 | $0.9997 |
| 5 | sol | -7.77% | $7,778,678,384 | $91.5700 |


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
