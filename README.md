# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-25 02:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bp | 34.51% | $26,666,441 | $1.1500 |
| 2 | qnt | 26.58% | $42,742,109 | $89.8900 |
| 3 | ondo | 26.49% | $1,155,610,063 | $0.5276 |
| 4 | xpl | 24.43% | $190,585,811 | $0.1122 |
| 5 | dbr | 13.75% | $13,762,957 | $0.0236 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -17.40% | $40,927,715 | $0.0348 |
| 2 | meta | -13.31% | $19,823,101 | $5.8600 |
| 3 | br | -10.66% | $18,816,684 | $0.9593 |
| 4 | lit | -9.14% | $121,924,909 | $4.9400 |
| 5 | useless | -8.80% | $45,842,580 | $0.2788 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $68,260,111,048 | $0.9997 |
| 2 | btc | -0.03% | $37,703,086,857 | $84,321.0000 |
| 3 | usdc | -0.01% | $19,371,398,646 | $0.9998 |
| 4 | eth | -0.28% | $14,726,217,561 | $2,679.5800 |
| 5 | xrp | 1.51% | $4,514,938,871 | $1.5300 |


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
