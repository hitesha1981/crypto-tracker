# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-31 01:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 24.61% | $29,643,514 | $17.1900 |
| 2 | 2z | 10.49% | $15,144,498 | $0.0760 |
| 3 | dexe | 9.25% | $27,203,584 | $7.9600 |
| 4 | gekko | 7.89% | $76,275 | $0.0000 |
| 5 | kag | 6.68% | $305,588 | $73.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | night | -9.17% | $504,420,010 | $0.0442 |
| 2 | ab | -7.16% | $4,133,533 | $0.0018 |
| 3 | rain | -7.16% | $33,923,551 | $0.0077 |
| 4 | zro | -5.67% | $35,143,720 | $1.8900 |
| 5 | siren | -5.34% | $20,898,191 | $1.6700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $64,084,342,535 | $0.9992 |
| 2 | btc | 1.62% | $41,061,948,419 | $67,813.0000 |
| 3 | eth | 2.87% | $18,282,514,062 | $2,070.2000 |
| 4 | usdc | -0.01% | $7,344,618,671 | $0.9996 |
| 5 | sol | 1.44% | $3,544,010,416 | $83.8000 |


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
