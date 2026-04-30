# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-30 02:13 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | 36.31% | $101,416,076 | $0.3004 |
| 2 | ub | 15.69% | $19,550,915 | $0.0657 |
| 3 | b | 9.44% | $5,828,219 | $0.1337 |
| 4 | lunc | 7.91% | $85,690,257 | $0.0001 |
| 5 | doge | 7.11% | $4,682,657,070 | $0.1070 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | genius | -17.13% | $17,206,383 | $0.4484 |
| 2 | umxm | -16.86% | $13,412,038 | $1.5500 |
| 3 | hash | -14.41% | $33,346 | $0.0106 |
| 4 | wlfi | -12.34% | $106,390,865 | $0.0641 |
| 5 | chz | -9.99% | $102,453,435 | $0.0420 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $74,871,773,959 | $0.9996 |
| 2 | btc | -0.30% | $43,042,403,596 | $76,301.0000 |
| 3 | eth | -0.92% | $19,751,070,154 | $2,271.1200 |
| 4 | usdc | 0.00% | $15,582,469,465 | $0.9998 |
| 5 | doge | 7.11% | $4,682,657,070 | $0.1070 |


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
