# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-27 01:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | power | 112.11% | $39,584,117 | $1.9400 |
| 2 | zano | 45.18% | $1,828,616 | $7.7000 |
| 3 | river | 17.93% | $43,184,144 | $10.9300 |
| 4 | dcr | 17.46% | $12,035,811 | $34.0500 |
| 5 | stable | 17.40% | $69,366,003 | $0.0381 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kite | -13.39% | $175,573,856 | $0.2487 |
| 2 | siren | -11.82% | $45,136,364 | $0.3139 |
| 3 | cvx | -11.25% | $15,539,553 | $1.7100 |
| 4 | glm | -9.97% | $20,739,565 | $0.1351 |
| 5 | bat | -7.56% | $25,791,788 | $0.1139 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $72,123,713,149 | $1.0000 |
| 2 | btc | -2.13% | $44,026,668,310 | $67,056.0000 |
| 3 | eth | -2.61% | $22,785,395,795 | $2,007.5500 |
| 4 | usdc | -0.01% | $4,158,145,646 | $0.9999 |
| 5 | sol | -3.88% | $4,152,015,641 | $85.4900 |


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
