# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-27 01:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xcn | 5.29% | $17,601,126 | $0.0055 |
| 2 | ondo | 3.32% | $113,133,381 | $0.2797 |
| 3 | night | 2.72% | $1,131,608,826 | $0.0460 |
| 4 | b | 2.63% | $3,369,250 | $0.2119 |
| 5 | pieverse | 2.17% | $3,130,506 | $0.5336 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -27.66% | $38,092,272 | $1.6000 |
| 2 | river | -26.41% | $34,767,136 | $15.9700 |
| 3 | kite | -15.69% | $146,107,097 | $0.2113 |
| 4 | lit | -11.01% | $21,454,388 | $0.8825 |
| 5 | ena | -10.97% | $143,776,863 | $0.0969 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $79,659,855,494 | $0.9994 |
| 2 | btc | -3.33% | $52,722,455,711 | $68,853.0000 |
| 3 | eth | -4.38% | $17,526,719,146 | $2,069.4500 |
| 4 | sol | -5.61% | $4,164,056,406 | $86.6500 |
| 5 | usdc | -0.00% | $3,649,511,668 | $0.9998 |


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
