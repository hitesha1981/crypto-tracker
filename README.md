# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-19 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | asteroid | 486.32% | $139,127,825 | $0.0003 |
| 2 | pieverse | 29.13% | $33,272,408 | $0.6154 |
| 3 | gwei | 22.03% | $28,586,192 | $0.1014 |
| 4 | dexe | 14.46% | $42,986,566 | $14.7900 |
| 5 | cfg | 12.87% | $54,470,675 | $0.2528 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | -90.93% | $460,946,936 | $2.4200 |
| 2 | h | -18.56% | $43,110,326 | $0.1076 |
| 3 | river | -17.21% | $18,994,349 | $6.3300 |
| 4 | xpl | -16.81% | $88,537,470 | $0.1065 |
| 5 | m | -16.49% | $23,860,925 | $3.6200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $74,554,704,487 | $1.0000 |
| 2 | btc | -2.02% | $51,386,168,052 | $75,642.0000 |
| 3 | eth | -2.97% | $13,057,070,554 | $2,348.5800 |
| 4 | usdc | 0.01% | $8,605,653,072 | $0.9999 |
| 5 | sol | -3.43% | $2,766,032,370 | $85.7800 |


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
