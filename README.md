# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-17 02:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | br | 185.66% | $54,833,843 | $0.6701 |
| 2 | drv | 74.65% | $108,661,635 | $0.2417 |
| 3 | zcat | 66.80% | $5,179,032 | $0.1369 |
| 4 | stonk | 35.67% | $15,447,033 | $0.2101 |
| 5 | lsk | 33.43% | $251,771,439 | $0.5166 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -24.17% | $44,224,139 | $0.0217 |
| 2 | mcat | -14.99% | $6,188,553 | $0.2486 |
| 3 | stable | -10.78% | $10,008,991 | $0.0240 |
| 4 | b | -9.91% | $4,348,676 | $0.1867 |
| 5 | rain | -8.13% | $31,107,578 | $0.0129 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $60,711,275,090 | $0.9993 |
| 2 | btc | 0.62% | $31,202,859,406 | $76,385.0000 |
| 3 | usdc | -0.00% | $18,383,456,188 | $0.9996 |
| 4 | eth | 1.09% | $16,206,574,872 | $2,430.7800 |
| 5 | xrp | 0.74% | $3,821,180,597 | $1.3000 |


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
