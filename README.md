# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-13 01:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pi | 31.11% | $125,873,436 | $0.2860 |
| 2 | river | 23.94% | $39,128,293 | $18.6800 |
| 3 | fet | 18.23% | $97,177,415 | $0.1881 |
| 4 | qubic | 14.89% | $2,624,667 | $0.0000 |
| 5 | render | 13.45% | $110,301,138 | $1.7300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | gomining | -5.33% | $13,247,964 | $0.2822 |
| 2 | cvx | -4.84% | $11,330,535 | $2.0500 |
| 3 | hash | -4.82% | $2,554 | $0.0133 |
| 4 | cc | -4.37% | $250,453,498 | $0.1478 |
| 5 | rlb | -3.59% | $379,267 | $0.0651 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $75,710,457,279 | $1.0000 |
| 2 | btc | 2.23% | $46,693,577,697 | $71,534.0000 |
| 3 | eth | 3.49% | $23,756,376,893 | $2,120.9700 |
| 4 | usdc | 0.00% | $7,512,352,573 | $1.0000 |
| 5 | sol | 4.38% | $4,428,068,597 | $90.1100 |


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
