# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-21 05:00 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 5.98% | $8,192,513 | $0.6616 |
| 2 | apepe | 5.72% | $37,196,782 | $0.0000 |
| 3 | o | 4.37% | $2,863,146 | $0.5551 |
| 4 | hash | 3.46% | $11,930 | $0.0065 |
| 5 | drv | 3.06% | $10,728,390 | $0.2560 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | a7a5 | -65.55% | $7 | $0.0041 |
| 2 | ake | -50.58% | $180,033,295 | $0.0052 |
| 3 | zec | -17.22% | $1,325,012,291 | $698.5000 |
| 4 | icnt | -15.80% | $16,075,223 | $0.3658 |
| 5 | lit | -15.51% | $51,990,899 | $2.2000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $83,959,514,426 | $0.9990 |
| 2 | btc | -8.49% | $60,472,472,308 | $56,249.0000 |
| 3 | usdc | 0.00% | $22,570,140,311 | $0.9996 |
| 4 | eth | -9.55% | $21,631,619,986 | $1,560.0600 |
| 5 | u | -0.01% | $5,523,649,954 | $0.9993 |


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
