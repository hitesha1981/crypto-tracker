# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-17 00:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 30.00% | $39,349,701 | $0.3963 |
| 2 | velvet | 23.80% | $28,586,529 | $1.0280 |
| 3 | drv | 10.70% | $18,519,563 | $0.0994 |
| 4 | q | 7.70% | $9,101,287 | $0.0249 |
| 5 | cap | 7.00% | $37,559,135 | $0.0688 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fgrs | -14.70% | $26,690 | $26.6900 |
| 2 | cashcat | -12.60% | $12,898,081 | $0.0995 |
| 3 | h | -7.50% | $40,654,800 | $0.1416 |
| 4 | zano | -6.90% | $1,135,469 | $8.0300 |
| 5 | ake | -6.00% | $16,620,181 | $0.0099 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $17,274,542,630 | $0.9992 |
| 2 | btc | -0.40% | $10,147,300,204 | $62,839.0000 |
| 3 | eth | -0.40% | $3,396,421,699 | $1,874.6900 |
| 4 | usdc | 0.00% | $3,161,719,059 | $0.9996 |
| 5 | sol | -1.30% | $734,940,324 | $74.5500 |


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
