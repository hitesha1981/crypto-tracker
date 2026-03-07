# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-07 01:19 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sent | 15.28% | $148,799,460 | $0.0251 |
| 2 | skr | 14.45% | $39,443,263 | $0.0276 |
| 3 | pi | 7.88% | $42,626,042 | $0.2153 |
| 4 | ban | 7.69% | $5,847,648 | $0.1218 |
| 5 | kau | 4.48% | $250,879 | $171.1300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bard | -24.99% | $84,196,925 | $1.2200 |
| 2 | xpl | -18.23% | $92,051,405 | $0.0976 |
| 3 | h | -12.47% | $75,419,283 | $0.1560 |
| 4 | wif | -12.06% | $104,624,882 | $0.1886 |
| 5 | river | -11.51% | $42,020,561 | $15.5500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $69,491,658,458 | $1.0000 |
| 2 | btc | -3.72% | $44,448,687,603 | $68,224.0000 |
| 3 | eth | -4.67% | $18,809,603,954 | $1,979.6500 |
| 4 | usdc | 0.00% | $4,397,253,340 | $0.9999 |
| 5 | sol | -4.48% | $3,914,858,955 | $84.7500 |


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
