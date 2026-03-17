# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-17 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | drv | 30.84% | $1,455,950 | $0.1197 |
| 2 | fartcoin | 27.00% | $100,769,896 | $0.2114 |
| 3 | b | 24.02% | $16,673,573 | $0.2243 |
| 4 | grass | 20.55% | $22,826,754 | $0.4507 |
| 5 | zec | 19.88% | $632,162,906 | $275.7100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -48.60% | $57,326,918 | $0.1908 |
| 2 | river | -15.00% | $58,341,679 | $19.3600 |
| 3 | siren | -13.88% | $27,508,426 | $0.5194 |
| 4 | adi | -9.14% | $3,222,699 | $3.4100 |
| 5 | trump | -6.99% | $439,300,344 | $3.8700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $110,552,182,145 | $1.0000 |
| 2 | btc | 4.29% | $60,665,032,741 | $75,777.0000 |
| 3 | eth | 8.34% | $40,308,045,486 | $2,362.2500 |
| 4 | sol | 3.86% | $6,669,509,601 | $95.5400 |
| 5 | usdc | 0.00% | $5,972,012,078 | $1.0000 |


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
