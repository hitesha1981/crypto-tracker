# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-15 01:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | drv | 20.76% | $25,474,180 | $0.1415 |
| 2 | kaito | 17.71% | $58,209,970 | $0.7738 |
| 3 | zec | 10.79% | $496,842,626 | $554.7800 |
| 4 | spx | 10.22% | $9,477,410 | $0.3787 |
| 5 | grass | 10.20% | $23,121,175 | $0.3932 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xec | -14.73% | $18,317,466 | $0.0000 |
| 2 | rif | -10.43% | $9,634,396 | $0.1203 |
| 3 | kite | -10.29% | $29,740,568 | $0.1188 |
| 4 | cashcat | -8.01% | $64,065,770 | $0.1504 |
| 5 | ultima | -7.49% | $8,358,443 | $2,281.3600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $48,232,103,206 | $0.9992 |
| 2 | btc | 3.52% | $29,416,133,571 | $64,632.0000 |
| 3 | usdc | -0.00% | $13,703,897,709 | $0.9998 |
| 4 | eth | 4.82% | $13,400,805,215 | $1,868.2700 |
| 5 | sol | 3.19% | $1,946,480,748 | $77.5700 |


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
