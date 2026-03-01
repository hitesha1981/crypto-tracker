# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-01 01:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | power | 35.43% | $32,746,699 | $1.9900 |
| 2 | grass | 33.32% | $43,760,116 | $0.2802 |
| 3 | bard | 16.94% | $99,241,556 | $1.0050 |
| 4 | vvv | 15.94% | $43,334,365 | $5.3900 |
| 5 | hype | 11.49% | $371,356,256 | $30.4400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -14.34% | $21,400,868 | $0.2917 |
| 2 | pippin | -14.03% | $59,675,276 | $0.5816 |
| 3 | zano | -6.20% | $1,316,961 | $7.3200 |
| 4 | kcs | -6.07% | $9,136,613 | $7.8900 |
| 5 | dcr | -4.09% | $12,316,038 | $33.1100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $77,967,405,430 | $1.0000 |
| 2 | btc | 1.34% | $47,088,643,194 | $66,711.0000 |
| 3 | eth | 2.29% | $21,867,350,703 | $1,970.5000 |
| 4 | sol | 4.16% | $5,035,854,620 | $85.3600 |
| 5 | usdc | 0.00% | $4,817,023,730 | $1.0000 |


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
