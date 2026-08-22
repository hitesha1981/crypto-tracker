# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-22 00:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stx | 32.40% | $46,209,011 | $0.1953 |
| 2 | ens | 30.70% | $71,874,961 | $6.3100 |
| 3 | bch | 29.30% | $849,365,285 | $293.0500 |
| 4 | pepe | 28.70% | $921,481,263 | $0.0000 |
| 5 | zec | 28.10% | $1,438,839,672 | $735.3200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | -4.80% | $3,687,926 | $1.1100 |
| 2 | ake | -4.30% | $5,476,576 | $0.0083 |
| 3 | shfl | -2.60% | $826,295 | $0.2913 |
| 4 | hash | -2.00% | $8,434 | $0.0078 |
| 5 | xmr | -1.60% | $130,809,476 | $408.4000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $115,223,644,880 | $0.9998 |
| 2 | btc | 7.70% | $69,798,330,958 | $77,792.0000 |
| 3 | eth | 8.60% | $31,066,766,393 | $2,508.6200 |
| 4 | usdc | 0.00% | $29,682,011,767 | $0.9999 |
| 5 | xrp | 15.80% | $9,686,180,274 | $1.4500 |


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
