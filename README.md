# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-25 01:18 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fluid | 45.21% | $79,806,753 | $3.5900 |
| 2 | river | 40.50% | $85,288,207 | $58.9300 |
| 3 | kaia | 29.11% | $166,529,599 | $0.0937 |
| 4 | myx | 19.59% | $28,496,310 | $6.9000 |
| 5 | pump | 15.97% | $185,470,362 | $0.0028 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | axs | -17.02% | $465,410,839 | $2.4300 |
| 2 | zro | -15.09% | $86,698,729 | $1.9400 |
| 3 | dcr | -7.80% | $2,985,515 | $17.7200 |
| 4 | sand | -6.04% | $67,407,213 | $0.1461 |
| 5 | mana | -5.81% | $24,535,704 | $0.1536 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $33,457,953,779 | $0.9986 |
| 2 | btc | -0.36% | $16,078,857,436 | $89,119.0000 |
| 3 | eth | 0.02% | $8,984,603,811 | $2,952.8200 |
| 4 | usd1 | -0.04% | $2,077,187,934 | $0.9998 |
| 5 | usdc | 0.01% | $2,006,083,293 | $0.9997 |


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
