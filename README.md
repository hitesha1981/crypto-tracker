# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-25 00:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | 46.56% | $76,988,959 | $0.2191 |
| 2 | kag | 23.60% | $1,979 | $62.3600 |
| 3 | meta | 23.11% | $4,732,463 | $6.1500 |
| 4 | dog | 21.82% | $4,979,079 | $0.0012 |
| 5 | drv | 15.76% | $27,656,182 | $0.1505 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sand | -7.00% | $24,220,098 | $0.0422 |
| 2 | trac | -6.68% | $23,046,214 | $0.3708 |
| 3 | pump | -6.49% | $280,329,907 | $0.0048 |
| 4 | morpho | -5.90% | $63,454,696 | $2.6200 |
| 5 | trump | -4.56% | $589,646,729 | $2.4500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $87,235,973,453 | $0.9998 |
| 2 | btc | 2.94% | $52,042,743,781 | $79,583.0000 |
| 3 | usdc | 0.00% | $23,238,216,695 | $0.9999 |
| 4 | eth | 1.90% | $20,497,570,927 | $2,496.1000 |
| 5 | sol | 7.73% | $6,254,169,447 | $101.9400 |


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
