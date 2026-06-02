# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-02 02:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 73.31% | $247,440,673 | $17.5700 |
| 2 | pieverse | 31.65% | $46,867,634 | $0.9377 |
| 3 | skyai | 22.77% | $33,413,142 | $0.2075 |
| 4 | home | 16.36% | $130,298,367 | $0.0457 |
| 5 | h | 15.16% | $600,675,256 | $0.7470 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | -42.73% | $53,048,272 | $0.7286 |
| 2 | rail | -12.56% | $1,962,174 | $2.4500 |
| 3 | hash | -12.38% | $23,770 | $0.0098 |
| 4 | xlm | -11.97% | $1,130,112,257 | $0.2373 |
| 5 | dydx | -11.59% | $8,677,517 | $0.1720 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $80,420,925,521 | $0.9985 |
| 2 | btc | -4.20% | $53,564,016,678 | $70,619.0000 |
| 3 | eth | -1.10% | $17,037,495,581 | $1,987.4600 |
| 4 | usdc | -0.02% | $16,913,636,676 | $0.9996 |
| 5 | sol | -2.74% | $2,757,609,837 | $80.3100 |


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
