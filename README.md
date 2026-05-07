# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-07 02:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 64.66% | $215,141,262 | $4.4900 |
| 2 | bill | 63.80% | $351,581,438 | $0.0693 |
| 3 | kaio | 38.61% | $26,768,572 | $0.2190 |
| 4 | ton | 31.27% | $1,362,350,714 | $2.6400 |
| 5 | vvv | 19.24% | $56,187,073 | $12.1000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -32.19% | $77,262,376 | $0.3091 |
| 2 | lunc | -21.59% | $168,311,496 | $0.0001 |
| 3 | asteroid | -10.43% | $26,463,876 | $0.0004 |
| 4 | rave | -8.72% | $24,003,026 | $0.6282 |
| 5 | tibbir | -7.60% | $2,112,450 | $0.1464 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $78,153,072,405 | $0.9999 |
| 2 | btc | -0.25% | $42,459,280,539 | $81,078.0000 |
| 3 | eth | -2.07% | $21,932,130,388 | $2,321.1400 |
| 4 | usdc | -0.00% | $15,837,589,815 | $0.9998 |
| 5 | sol | 1.61% | $4,761,990,919 | $88.1300 |


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
