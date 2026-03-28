# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-28 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xfloki | 233737.44% | $3,172,332 | $0.3024 |
| 2 | icnt | 16.90% | $7,809,907 | $0.4477 |
| 3 | qubic | 4.06% | $2,268,127 | $0.0000 |
| 4 | shfl | 3.61% | $2,377,921 | $0.2789 |
| 5 | dexe | 3.34% | $12,121,186 | $7.4200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -44.46% | $100,350,745 | $0.9464 |
| 2 | river | -18.44% | $41,217,879 | $13.1800 |
| 3 | kite | -15.71% | $65,010,190 | $0.1780 |
| 4 | wld | -14.63% | $186,544,630 | $0.2478 |
| 5 | sent | -14.38% | $18,924,676 | $0.0160 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $76,734,599,920 | $0.9993 |
| 2 | btc | -3.85% | $49,260,410,838 | $66,224.0000 |
| 3 | eth | -3.99% | $19,083,170,638 | $1,987.7700 |
| 4 | usdc | 0.00% | $11,616,371,443 | $0.9998 |
| 5 | sol | -4.75% | $3,476,560,385 | $82.5400 |


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
