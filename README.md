# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-06 02:30 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grx | 29.85% | $2,446,004 | $12.8500 |
| 2 | cx | 19.30% | $1,633,195 | $0.0809 |
| 3 | lit | 16.29% | $86,624,484 | $2.5400 |
| 4 | tibbir | 15.00% | $1,649,495 | $0.1289 |
| 5 | ub | 10.98% | $12,060,890 | $0.1079 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | -14.20% | $19,918,446 | $0.4939 |
| 2 | h | -13.12% | $11,204,695 | $0.0712 |
| 3 | nex | -9.29% | $10,501,993 | $0.0000 |
| 4 | trump | -5.83% | $90,210,080 | $1.6900 |
| 5 | bp | -4.08% | $2,095,741 | $0.5191 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $35,558,108,358 | $0.9990 |
| 2 | btc | 1.25% | $19,675,477,888 | $63,505.0000 |
| 3 | eth | 1.21% | $10,864,020,970 | $1,784.9100 |
| 4 | usdc | -0.01% | $6,492,044,790 | $0.9997 |
| 5 | sol | 1.23% | $1,616,596,488 | $81.4700 |


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
