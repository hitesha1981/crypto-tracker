# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-14 02:54 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 31.99% | $68,340,196 | $0.2896 |
| 2 | skyai | 28.90% | $41,339,988 | $0.3673 |
| 3 | tao | 27.56% | $592,837,894 | $273.9700 |
| 4 | akt | 26.88% | $17,075,015 | $0.7760 |
| 5 | btw | 14.09% | $12,951,170 | $0.0903 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | -12.75% | $19,763,426 | $0.3861 |
| 2 | velvet | -11.16% | $46,887,614 | $0.4168 |
| 3 | trump | -10.28% | $445,244,954 | $2.0800 |
| 4 | night | -6.61% | $79,493,557 | $0.0328 |
| 5 | kag | -6.55% | $212,954 | $63.4000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $30,413,172,264 | $0.9995 |
| 2 | btc | 1.44% | $17,768,143,739 | $64,464.0000 |
| 3 | usdc | -0.00% | $5,598,215,338 | $0.9998 |
| 4 | eth | 0.97% | $5,474,240,652 | $1,681.6300 |
| 5 | sol | 2.87% | $1,602,629,021 | $68.8300 |


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
