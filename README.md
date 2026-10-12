# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-12 03:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | w | 66.39% | $215,934,226 | $0.0286 |
| 2 | grass | 29.91% | $77,932,022 | $0.8689 |
| 3 | s | 28.59% | $263,905,215 | $0.0602 |
| 4 | plume | 23.71% | $74,249,578 | $0.0230 |
| 5 | rail | 20.53% | $1,044,537 | $3.2500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | apepe | -14.84% | $11,022,309 | $0.0000 |
| 2 | drv | -7.06% | $14,633,369 | $0.4718 |
| 3 | br | -5.95% | $4,321,631 | $0.4696 |
| 4 | kaia | -5.32% | $17,148,092 | $0.0504 |
| 5 | strk | -5.24% | $549,244,254 | $0.1102 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $35,921,695,920 | $0.9992 |
| 2 | btc | 0.79% | $17,101,663,802 | $83,585.0000 |
| 3 | usdc | 0.01% | $9,991,551,330 | $0.9998 |
| 4 | eth | 1.44% | $8,871,430,138 | $2,543.3400 |
| 5 | sol | 1.91% | $2,057,321,272 | $111.7200 |


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
