# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-27 03:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | 281.56% | $225,684,545 | $0.2082 |
| 2 | beam | 10.15% | $36,190,357 | $0.0033 |
| 3 | hash | 9.65% | $53,699 | $0.0074 |
| 4 | night | 8.07% | $16,654,373 | $0.0396 |
| 5 | xdc | 7.76% | $22,115,729 | $0.0334 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -25.89% | $31,179,466 | $1.2500 |
| 2 | cap | -19.46% | $120,618,213 | $0.0934 |
| 3 | rain | -14.86% | $18,111,294 | $0.0072 |
| 4 | useless | -9.01% | $13,325,011 | $0.1502 |
| 5 | zro | -5.82% | $71,499,088 | $1.6100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $44,773,812,101 | $0.9987 |
| 2 | btc | -0.03% | $27,382,343,616 | $79,646.0000 |
| 3 | usdc | -0.04% | $11,682,828,733 | $0.9994 |
| 4 | eth | -0.16% | $9,201,951,283 | $2,308.2300 |
| 5 | sol | -0.96% | $2,342,599,735 | $99.9800 |


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
