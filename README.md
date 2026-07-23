# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-23 02:04 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | 11.32% | $15,706,537 | $0.1148 |
| 2 | us | 8.12% | $10,759,993 | $0.0455 |
| 3 | rail | 7.35% | $203,191 | $1.8600 |
| 4 | kite | 7.18% | $128,719,322 | $0.1258 |
| 5 | bc | 6.57% | $202,328 | $0.0196 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | -27.23% | $123,366,407 | $4.3500 |
| 2 | b | -11.91% | $10,530,009 | $0.2101 |
| 3 | night | -8.39% | $43,422,097 | $0.0213 |
| 4 | wlfi | -7.52% | $49,101,805 | $0.0528 |
| 5 | pump | -7.45% | $59,818,420 | $0.0019 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $44,642,422,120 | $0.9994 |
| 2 | btc | -0.93% | $28,136,716,119 | $65,741.0000 |
| 3 | usdc | 0.01% | $10,908,911,377 | $1.0000 |
| 4 | eth | -0.30% | $9,370,623,985 | $1,925.6100 |
| 5 | sol | -0.54% | $1,632,851,423 | $77.8300 |


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
