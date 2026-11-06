# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-06 04:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cap | 9.65% | $75,099,220 | $0.1077 |
| 2 | pieverse | 8.68% | $15,718,549 | $1.2900 |
| 3 | btw | 6.91% | $5,348,887 | $1.0990 |
| 4 | inj | 4.24% | $176,487,087 | $8.3400 |
| 5 | rain | 2.55% | $8,036,782 | $0.0061 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pons | -15.70% | $29,669,397 | $0.1888 |
| 2 | drv | -15.05% | $18,657,166 | $0.3197 |
| 3 | beam | -14.67% | $33,835,943 | $0.0040 |
| 4 | grass | -14.36% | $22,644,496 | $0.4883 |
| 5 | zro | -12.90% | $78,526,817 | $1.5800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $67,906,197,529 | $0.9989 |
| 2 | btc | -6.00% | $44,149,794,107 | $75,575.0000 |
| 3 | usdc | -0.03% | $18,529,120,559 | $0.9994 |
| 4 | eth | -8.03% | $17,391,807,171 | $2,227.8500 |
| 5 | sol | -7.07% | $4,604,072,073 | $89.2300 |


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
