# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-23 05:01 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dgai | 19.47% | $39,262,581 | $0.9952 |
| 2 | br | 17.07% | $5,527,656 | $0.4640 |
| 3 | mwc | 15.55% | $21,655 | $8.5900 |
| 4 | night | 12.38% | $34,809,009 | $0.0499 |
| 5 | pump | 9.65% | $87,694,117 | $0.0026 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | geod | -15.16% | $5,226,147 | $0.1863 |
| 2 | mon | -7.30% | $13,279,630 | $0.0121 |
| 3 | sky | -7.03% | $13,139,594 | $0.0411 |
| 4 | fluid | -5.23% | $2,139,511 | $1.5100 |
| 5 | nft | -4.79% | $4,391,403 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $40,351,742,577 | $0.9988 |
| 2 | btc | 3.34% | $28,761,525,280 | $61,167.0000 |
| 3 | usdc | 0.02% | $9,882,920,441 | $0.9994 |
| 4 | eth | 3.84% | $8,545,023,300 | $1,724.9900 |
| 5 | sol | 2.78% | $1,907,279,704 | $71.2600 |


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
