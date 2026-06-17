# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-17 02:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 43.06% | $58,662,023 | $13.7100 |
| 2 | h | 27.58% | $83,586,211 | $0.3196 |
| 3 | uni | 26.23% | $666,832,947 | $3.5200 |
| 4 | skyai | 24.62% | $44,858,714 | $0.4615 |
| 5 | bp | 23.98% | $6,455,152 | $0.5312 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -36.20% | $15,562,351 | $0.0582 |
| 2 | beat | -35.88% | $67,467,893 | $2.6700 |
| 3 | gwei | -17.21% | $7,323,313 | $0.1207 |
| 4 | hash | -9.88% | $20,127 | $0.0086 |
| 5 | pieverse | -4.54% | $8,602,462 | $0.7042 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $49,636,107,092 | $0.9991 |
| 2 | btc | 0.21% | $26,293,819,316 | $65,817.0000 |
| 3 | eth | 1.35% | $14,408,984,023 | $1,792.3200 |
| 4 | usdc | -0.01% | $11,368,551,583 | $0.9997 |
| 5 | hype | 11.06% | $2,315,237,556 | $74.7600 |


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
