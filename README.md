# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-12 05:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qfi | 76835.14% | $18,834 | $999.1500 |
| 2 | ozo | 67.01% | $306,324 | $0.2177 |
| 3 | hash | 11.06% | $4,159 | $0.0077 |
| 4 | yellow | 9.40% | $3,465,282 | $0.1059 |
| 5 | q | 8.36% | $15,530,917 | $0.0269 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pepe | -13.35% | $578,981,366 | $0.0000 |
| 2 | btw | -12.97% | $8,260,736 | $1.0280 |
| 3 | sn51 | -11.05% | $5,483,116 | $23.8900 |
| 4 | inj | -9.11% | $93,286,473 | $7.5000 |
| 5 | edge | -8.97% | $2,723,524 | $0.3388 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $40,776,928,611 | $0.9991 |
| 2 | btc | -0.05% | $25,587,828,621 | $73,581.0000 |
| 3 | usdc | -0.00% | $11,075,270,876 | $0.9995 |
| 4 | eth | -0.73% | $9,041,389,960 | $2,045.7200 |
| 5 | sol | 0.36% | $2,090,596,687 | $82.9000 |


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
