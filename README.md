# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-07 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jasmy | 26.79% | $222,643,638 | $0.0095 |
| 2 | river | 13.42% | $39,584,759 | $18.6500 |
| 3 | rain | 12.30% | $62,453,976 | $0.0091 |
| 4 | kag | 7.93% | $1,993,325 | $82.7500 |
| 5 | fartcoin | 7.38% | $235,098,107 | $0.4545 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | night | -9.26% | $49,111,931 | $0.0781 |
| 2 | btt | -7.83% | $24,360,114 | $0.0000 |
| 3 | pepe | -6.15% | $921,124,219 | $0.0000 |
| 4 | xlm | -5.09% | $343,333,179 | $0.2401 |
| 5 | pippin | -4.77% | $26,732,541 | $0.3340 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $97,242,742,889 | $0.9996 |
| 2 | btc | -1.13% | $58,289,848,801 | $92,779.0000 |
| 3 | eth | 1.46% | $29,737,789,900 | $3,267.7800 |
| 4 | usdc | 0.03% | $15,118,914,890 | $1.0000 |
| 5 | xrp | -3.92% | $8,094,315,067 | $2.2900 |


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
