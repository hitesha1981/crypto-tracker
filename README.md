# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-11 03:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | strk | 59.00% | $755,734,260 | $0.1179 |
| 2 | chip | 28.78% | $67,864,314 | $0.0672 |
| 3 | tia | 26.75% | $195,243,319 | $0.6075 |
| 4 | shfl | 20.42% | $1,921,583 | $0.4865 |
| 5 | q | 17.43% | $10,788,755 | $0.0314 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | -14.51% | $2,850 | $0.0054 |
| 2 | kaia | -9.02% | $126,605,976 | $0.0538 |
| 3 | cap | -7.66% | $38,659,095 | $0.0908 |
| 4 | fil | -7.02% | $151,788,037 | $1.1000 |
| 5 | drv | -5.94% | $36,372,926 | $0.5129 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $29,285,731,552 | $0.9991 |
| 2 | btc | 0.45% | $14,025,364,139 | $82,894.0000 |
| 3 | usdc | -0.01% | $7,040,208,973 | $0.9997 |
| 4 | eth | 0.55% | $6,099,090,788 | $2,504.7200 |
| 5 | sol | -0.12% | $1,501,941,362 | $109.5600 |


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
