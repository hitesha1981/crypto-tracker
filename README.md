# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-18 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | axs | 51.45% | $1,252,278,008 | $2.1500 |
| 2 | sand | 19.85% | $371,793,721 | $0.1572 |
| 3 | mana | 12.60% | $161,315,398 | $0.1693 |
| 4 | theta | 12.21% | $58,756,702 | $0.3581 |
| 5 | qrl | 11.87% | $151,278 | $3.2600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dcr | -14.15% | $5,818,528 | $22.5400 |
| 2 | dash | -13.80% | $485,526,518 | $72.5800 |
| 3 | river | -12.73% | $54,636,794 | $20.4100 |
| 4 | vsn | -11.28% | $19,410,712 | $0.0762 |
| 5 | fartcoin | -9.22% | $52,353,438 | $0.3428 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $35,348,129,723 | $0.9996 |
| 2 | btc | -0.55% | $17,556,292,563 | $94,898.0000 |
| 3 | eth | 0.24% | $11,274,647,687 | $3,300.2600 |
| 4 | usdc | 0.78% | $7,009,690,931 | $1.0080 |
| 5 | sol | -1.23% | $2,121,104,560 | $142.6700 |


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
