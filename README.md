# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-09 03:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | apepe | 7.82% | $12,132,553 | $0.0000 |
| 2 | stable | 7.10% | $7,049,924 | $0.0272 |
| 3 | pieverse | 6.50% | $6,540,502 | $1.4800 |
| 4 | pepe | 4.47% | $413,323,648 | $0.0000 |
| 5 | kite | 3.68% | $8,526,310 | $0.1095 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kntq | -14.93% | $10,709,029 | $0.4102 |
| 2 | rain | -11.91% | $13,300,816 | $0.0049 |
| 3 | btw | -10.30% | $8,445,333 | $1.1100 |
| 4 | xpl | -8.70% | $39,568,886 | $0.0516 |
| 5 | pearl | -7.97% | $9,563,988 | $1.6300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $35,141,902,507 | $0.9991 |
| 2 | btc | -1.20% | $20,115,329,883 | $74,889.0000 |
| 3 | eth | -4.19% | $10,147,479,933 | $2,141.7200 |
| 4 | usdc | -0.01% | $7,741,508,959 | $0.9994 |
| 5 | sol | -1.79% | $2,155,515,856 | $87.5500 |


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
