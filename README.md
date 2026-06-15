# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-15 02:58 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 80.78% | $127,671,641 | $0.5248 |
| 2 | rif | 18.47% | $28,777,940 | $0.1285 |
| 3 | grass | 15.60% | $28,962,230 | $0.4507 |
| 4 | zec | 14.92% | $513,939,229 | $486.0300 |
| 5 | wld | 13.68% | $704,824,767 | $0.5776 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -26.29% | $58,830,569 | $5.4500 |
| 2 | velvet | -11.14% | $42,243,104 | $0.3713 |
| 3 | ff | -8.55% | $27,112,373 | $0.0714 |
| 4 | ub | -4.93% | $6,926,245 | $0.1222 |
| 5 | stable | -4.51% | $16,019,965 | $0.0355 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $39,873,882,607 | $0.9995 |
| 2 | btc | 1.46% | $23,383,964,531 | $65,414.0000 |
| 3 | eth | 2.02% | $8,711,548,085 | $1,715.8900 |
| 4 | usdc | -0.01% | $7,481,448,016 | $0.9997 |
| 5 | sol | 3.04% | $1,951,703,958 | $70.9100 |


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
