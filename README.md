# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-24 02:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | irys | 273.89% | $1,895,251,128 | $0.1015 |
| 2 | m | 11.84% | $1,493,343 | $0.9544 |
| 3 | kmno | 10.03% | $17,196,568 | $0.0423 |
| 4 | trac | 8.94% | $4,430,830 | $0.4096 |
| 5 | ake | 8.89% | $46,221,197 | $0.0361 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -17.30% | $12,995,625 | $0.0975 |
| 2 | wld | -13.36% | $366,770,370 | $0.4812 |
| 3 | hash | -9.94% | $2,366 | $0.0064 |
| 4 | lit | -9.70% | $75,908,564 | $3.1300 |
| 5 | pump | -9.14% | $146,489,095 | $0.0042 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $41,136,764,230 | $0.9991 |
| 2 | btc | -1.11% | $22,611,484,269 | $80,863.0000 |
| 3 | usdc | 0.03% | $10,485,993,440 | $0.9998 |
| 4 | eth | -1.22% | $9,507,058,514 | $2,379.6900 |
| 5 | sol | -1.91% | $2,173,278,152 | $102.4800 |


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
