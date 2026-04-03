# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-03 01:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | 13.15% | $57,211,773 | $0.7633 |
| 2 | xpl | 12.00% | $387,725,780 | $0.1172 |
| 3 | lit | 8.95% | $39,235,652 | $0.9424 |
| 4 | algo | 8.41% | $131,927,511 | $0.1094 |
| 5 | mon | 7.32% | $496,934,956 | $0.0251 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -23.59% | $30,445,270 | $0.1833 |
| 2 | kite | -16.40% | $53,709,712 | $0.1252 |
| 3 | river | -15.03% | $28,057,721 | $12.8500 |
| 4 | uni | -9.12% | $474,568,288 | $3.1700 |
| 5 | ath | -8.81% | $16,697,737 | $0.0063 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $70,601,964,980 | $0.9999 |
| 2 | btc | -0.87% | $45,448,592,060 | $66,563.0000 |
| 3 | eth | -2.26% | $16,448,121,041 | $2,047.8400 |
| 4 | usdc | 0.02% | $10,847,532,237 | $1.0000 |
| 5 | sol | -0.08% | $3,337,855,334 | $79.1700 |


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
