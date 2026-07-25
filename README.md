# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-25 01:58 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | 92.92% | $532,825,311 | $3.7500 |
| 2 | velvet | 51.86% | $20,811,551 | $0.4652 |
| 3 | soso | 17.96% | $5,583,080 | $0.3295 |
| 4 | grx | 17.06% | $633,159 | $15.3000 |
| 5 | bank | 9.78% | $144,456,896 | $0.2975 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stx | -16.22% | $40,909,318 | $0.1366 |
| 2 | wld | -9.07% | $162,790,054 | $0.3474 |
| 3 | xec | -7.85% | $10,777,576 | $0.0000 |
| 4 | lit | -7.52% | $28,800,049 | $1.9900 |
| 5 | grass | -7.39% | $19,574,006 | $0.3342 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $42,697,331,545 | $0.9991 |
| 2 | btc | -1.54% | $24,990,550,627 | $64,028.0000 |
| 3 | usdc | 0.01% | $12,080,924,127 | $0.9999 |
| 4 | eth | -0.69% | $7,394,488,947 | $1,858.8100 |
| 5 | sol | -2.18% | $1,521,518,530 | $74.0800 |


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
