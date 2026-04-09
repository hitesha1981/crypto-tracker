# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-09 01:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lux | 38.55% | $1,122,176 | $0.0013 |
| 2 | aria | 30.84% | $23,828,387 | $0.6767 |
| 3 | uds | 7.49% | $336,810 | $1.7800 |
| 4 | shfl | 7.28% | $780,561 | $0.3133 |
| 5 | syrup | 6.52% | $15,791,137 | $0.2391 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kite | -11.32% | $79,258,604 | $0.1319 |
| 2 | lit | -10.45% | $26,521,147 | $0.9869 |
| 3 | wlfi | -9.76% | $81,783,985 | $0.0893 |
| 4 | edge | -7.54% | $48,486,751 | $1.0060 |
| 5 | 0g | -6.75% | $15,996,606 | $0.5167 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $67,728,178,137 | $1.0000 |
| 2 | btc | -1.24% | $41,204,552,687 | $70,594.0000 |
| 3 | eth | -2.80% | $20,044,306,643 | $2,170.1600 |
| 4 | usdc | 0.03% | $13,798,964,278 | $1.0000 |
| 5 | sol | -3.00% | $3,548,614,884 | $81.9400 |


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
