# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-08 01:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zec | 24.80% | $711,037,438 | $318.7400 |
| 2 | zro | 18.22% | $89,451,970 | $2.0700 |
| 3 | fartcoin | 17.12% | $79,006,034 | $0.1958 |
| 4 | rain | 17.06% | $18,839,415 | $0.0076 |
| 5 | edge | 15.79% | $49,825,177 | $1.0770 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | -12.59% | $25,256,076 | $7.7000 |
| 2 | river | -12.01% | $25,513,136 | $11.6000 |
| 3 | zano | -9.18% | $1,419,631 | $9.0600 |
| 4 | kite | -6.39% | $81,532,306 | $0.1477 |
| 5 | siren | -3.79% | $28,092,916 | $0.5892 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $87,903,357,505 | $0.9999 |
| 2 | btc | 4.30% | $56,746,511,214 | $71,532.0000 |
| 3 | eth | 6.18% | $23,346,768,852 | $2,238.1200 |
| 4 | usdc | -0.00% | $14,239,248,799 | $0.9998 |
| 5 | sol | 6.03% | $4,795,367,574 | $84.7800 |


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
