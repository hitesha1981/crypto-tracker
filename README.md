# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-23 01:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | 61.39% | $344,591,771 | $0.0453 |
| 2 | river | 42.51% | $49,952,533 | $66.3700 |
| 3 | zro | 16.56% | $179,728,829 | $2.2300 |
| 4 | axs | 12.24% | $696,145,247 | $2.8200 |
| 5 | rain | 11.27% | $41,670,026 | $0.0101 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | shmeegus | -34.90% | $2,122,577 | $0.3435 |
| 2 | spx | -8.32% | $22,878,550 | $0.4106 |
| 3 | strk | -7.37% | $48,463,558 | $0.0741 |
| 4 | pump | -6.33% | $140,051,527 | $0.0025 |
| 5 | xcn | -5.81% | $13,438,377 | $0.0069 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $68,105,866,102 | $0.9990 |
| 2 | btc | -0.38% | $38,374,174,953 | $89,532.0000 |
| 3 | eth | -1.98% | $21,817,378,536 | $2,953.4400 |
| 4 | usdc | -0.01% | $7,051,687,046 | $0.9997 |
| 5 | sol | -1.24% | $3,410,110,039 | $128.3400 |


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
