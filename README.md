# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-27 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | axs | 34.36% | $905,376,060 | $2.6500 |
| 2 | dcr | 14.12% | $14,241,244 | $20.1200 |
| 3 | hype | 13.27% | $348,408,992 | $25.2000 |
| 4 | khype | 13.04% | $8,918,336 | $25.4200 |
| 5 | hash | 12.41% | $109,249 | $0.0254 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sun | -8.32% | $38,108,449 | $0.0189 |
| 2 | wlfi | -7.39% | $210,743,453 | $0.1574 |
| 3 | pippin | -4.82% | $29,944,380 | $0.3016 |
| 4 | ip | -4.03% | $106,651,301 | $2.2100 |
| 5 | myx | -3.75% | $17,501,377 | $5.7600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $83,758,326,989 | $0.9989 |
| 2 | btc | 1.02% | $47,784,771,801 | $88,155.0000 |
| 3 | eth | 1.54% | $28,615,797,562 | $2,912.7600 |
| 4 | usdc | 0.01% | $7,141,162,699 | $0.9997 |
| 5 | sol | 2.60% | $4,341,384,950 | $123.7700 |


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
