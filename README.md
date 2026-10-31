# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-31 03:32 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beam | 52.99% | $228,215,017 | $0.0050 |
| 2 | op | 19.79% | $119,693,157 | $0.1177 |
| 3 | hash | 17.66% | $36,983 | $0.0075 |
| 4 | eigen | 14.14% | $29,012,007 | $0.1888 |
| 5 | cvx | 12.16% | $18,070,983 | $2.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -41.22% | $30,361,202 | $0.0116 |
| 2 | q | -32.18% | $78,045,667 | $0.0341 |
| 3 | btw | -20.05% | $11,517,374 | $1.1700 |
| 4 | trx | -7.55% | $1,107,022,887 | $0.3264 |
| 5 | cards | -6.81% | $7,707,447 | $0.2534 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btc | -0.42% | $202,343,284,093 | $77,299.0000 |
| 2 | xaut | -2.66% | $167,232,541,590 | $3,881.9800 |
| 3 | usdt | 0.10% | $60,655,522,202 | $0.9993 |
| 4 | usdc | 0.09% | $15,078,980,171 | $0.9999 |
| 5 | eth | 1.04% | $14,479,993,378 | $2,242.7000 |


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
