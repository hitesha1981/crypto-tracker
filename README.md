# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-22 04:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | a7a5 | 190.74% | $2,139 | $0.0119 |
| 2 | drv | 31.56% | $26,735,482 | $0.3312 |
| 3 | vvv | 25.88% | $67,711,605 | $24.8800 |
| 4 | geod | 25.49% | $3,329,838 | $0.2229 |
| 5 | pieverse | 21.54% | $42,317,987 | $3.4100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | -8.70% | $11,419,574 | $0.0034 |
| 2 | m | -6.52% | $2,261,797 | $0.7536 |
| 3 | cap | -4.23% | $13,300,926 | $0.0892 |
| 4 | anvl | -3.56% | $76,849 | $0.0012 |
| 5 | borg | -3.48% | $595,558 | $0.1261 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $62,302,467,047 | $0.9984 |
| 2 | btc | 6.17% | $46,994,671,808 | $59,190.0000 |
| 3 | eth | 7.05% | $14,316,069,364 | $1,659.1800 |
| 4 | usdc | -0.02% | $13,832,226,489 | $0.9993 |
| 5 | u | 0.08% | $4,055,219,556 | $0.9999 |


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
