# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-06 02:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qait | 65.77% | $25,465,646 | $0.0337 |
| 2 | btw | 14.82% | $34,967,886 | $0.0511 |
| 3 | beat | 10.59% | $42,018,177 | $1.7400 |
| 4 | vvv | 10.34% | $125,438,835 | $17.9800 |
| 5 | skyai | 7.80% | $18,276,458 | $0.1910 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | -18.55% | $18,671,845 | $0.6623 |
| 2 | stable | -18.50% | $21,717,968 | $0.0308 |
| 3 | xpl | -18.28% | $149,056,399 | $0.0666 |
| 4 | lab | -18.02% | $109,505,501 | $9.2900 |
| 5 | twt | -16.82% | $15,715,032 | $0.3702 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.08% | $120,786,158,074 | $0.9997 |
| 2 | btc | -3.04% | $72,681,998,397 | $60,818.0000 |
| 3 | eth | -9.41% | $39,219,477,532 | $1,572.9800 |
| 4 | usdc | -0.00% | $27,764,712,460 | $0.9997 |
| 5 | sol | -6.21% | $6,837,017,354 | $63.5500 |


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
