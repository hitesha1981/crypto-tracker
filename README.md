# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-14 01:13 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dash | 44.93% | $970,695,749 | $58.5000 |
| 2 | ip | 31.11% | $689,335,048 | $3.9000 |
| 3 | op | 18.00% | $211,733,726 | $0.3672 |
| 4 | dcr | 17.65% | $19,804,459 | $19.1900 |
| 5 | pepe | 16.58% | $1,079,821,800 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | -6.29% | $15,380,511 | $1.5800 |
| 2 | h | -5.10% | $32,696,877 | $0.1651 |
| 3 | merl | -2.99% | $17,566,513 | $0.2463 |
| 4 | hash | -1.93% | $20,542 | $0.0242 |
| 5 | bch | -1.69% | $768,174,978 | $612.6800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.05% | $116,156,134,356 | $0.9994 |
| 2 | btc | 4.44% | $68,514,294,689 | $95,391.0000 |
| 3 | eth | 7.14% | $36,478,675,425 | $3,329.9700 |
| 4 | usdc | -0.01% | $21,599,346,469 | $0.9997 |
| 5 | sol | 4.44% | $8,286,081,832 | $145.4800 |


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
