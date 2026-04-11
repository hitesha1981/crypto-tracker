# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-11 01:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 78.60% | $349,445,912 | $1.8400 |
| 2 | ff | 38.27% | $222,469,545 | $0.0983 |
| 3 | 币安人生 | 35.03% | $70,986,552 | $0.1137 |
| 4 | dash | 21.09% | $392,639,209 | $44.9500 |
| 5 | h | 20.04% | $35,852,608 | $0.1027 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -16.31% | $41,815,457 | $8.8800 |
| 2 | tao | -12.78% | $1,004,748,240 | $255.4300 |
| 3 | wlfi | -6.77% | $222,620,712 | $0.0800 |
| 4 | cfg | -5.58% | $97,526,292 | $0.1998 |
| 5 | vvv | -5.53% | $20,180,817 | $7.5200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $58,892,093,927 | $1.0000 |
| 2 | btc | 0.72% | $36,580,316,547 | $72,886.0000 |
| 3 | eth | 1.81% | $16,307,311,505 | $2,242.0500 |
| 4 | usdc | -0.01% | $11,946,361,085 | $0.9999 |
| 5 | sol | 1.24% | $2,974,736,007 | $84.5300 |


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
