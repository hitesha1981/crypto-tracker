# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-26 01:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | 0g | 30.86% | $298,318,080 | $1.1400 |
| 2 | qrl | 12.14% | $116,107 | $3.1500 |
| 3 | 2z | 8.12% | $43,251,160 | $0.1211 |
| 4 | syrup | 7.80% | $25,003,618 | $0.3328 |
| 5 | pippin | 6.28% | $41,664,362 | $0.5109 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | -12.97% | $38,650,361 | $0.0070 |
| 2 | s | -8.38% | $33,416,384 | $0.0713 |
| 3 | m | -7.27% | $10,640,041 | $1.3200 |
| 4 | btse | -6.54% | $9,370,825 | $1.5000 |
| 5 | eeth | -6.32% | $24,759 | $2,903.0600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $42,740,307,012 | $0.9995 |
| 2 | btc | -0.40% | $23,694,078,130 | $87,219.0000 |
| 3 | eth | -1.15% | $12,515,194,497 | $2,907.1900 |
| 4 | usdc | -0.02% | $6,650,786,847 | $0.9998 |
| 5 | sol | -1.57% | $2,623,315,095 | $120.2300 |


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
