# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-14 01:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 18.23% | $22,664,778 | $0.6120 |
| 2 | bill | 17.05% | $35,109,709 | $0.0606 |
| 3 | hash | 16.12% | $53,341 | $0.0095 |
| 4 | xec | 16.11% | $103,302,018 | $0.0000 |
| 5 | bdx | 14.91% | $11,287,757 | $0.0964 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pi | -18.31% | $33,819,230 | $0.0732 |
| 2 | dexe | -11.89% | $93,054,730 | $42.7600 |
| 3 | grass | -11.40% | $21,764,991 | $0.3570 |
| 4 | lit | -9.32% | $82,513,603 | $2.4100 |
| 5 | ethfi | -9.05% | $32,830,578 | $0.3838 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $44,698,267,304 | $0.9988 |
| 2 | btc | -1.80% | $29,772,754,504 | $62,425.0000 |
| 3 | usdc | 0.01% | $12,483,535,855 | $0.9998 |
| 4 | eth | -1.64% | $10,163,324,304 | $1,782.9500 |
| 5 | sol | -2.12% | $1,690,312,258 | $75.1900 |


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
