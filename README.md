# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-21 02:57 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 35.54% | $99,070,831 | $0.1354 |
| 2 | re | 19.63% | $475,290,017 | $1.0350 |
| 3 | bp | 16.63% | $4,891,615 | $0.6891 |
| 4 | lab | 15.97% | $28,490,778 | $12.9900 |
| 5 | sand | 14.46% | $143,780,010 | $0.0609 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | o | -17.52% | $37,631,986 | $0.7046 |
| 2 | dexe | -8.92% | $10,527,357 | $14.8500 |
| 3 | kag | -8.02% | $191,729 | $57.2600 |
| 4 | rail | -6.83% | $159,899 | $2.3200 |
| 5 | h | -6.77% | $18,497,431 | $0.1986 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $31,485,343,388 | $0.9988 |
| 2 | btc | 1.39% | $16,815,434,524 | $64,188.0000 |
| 3 | eth | 1.80% | $7,556,199,892 | $1,734.9100 |
| 4 | usdc | 0.00% | $6,061,072,352 | $0.9999 |
| 5 | sol | 5.18% | $2,229,978,580 | $73.2200 |


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
