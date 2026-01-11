# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-11 01:17 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 23.56% | $27,507,545 | $14.4300 |
| 2 | chz | 12.23% | $169,699,017 | $0.0499 |
| 3 | pol | 10.32% | $634,051,648 | $0.1752 |
| 4 | rain | 7.60% | $57,452,927 | $0.0090 |
| 5 | sky | 6.91% | $10,456,675 | $0.0592 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -11.76% | $22,881,685 | $0.3647 |
| 2 | lit | -10.22% | $91,734,842 | $2.5800 |
| 3 | xcn | -10.21% | $18,596,362 | $0.0079 |
| 4 | jst | -8.24% | $21,124,556 | $0.0407 |
| 5 | mon | -6.40% | $88,621,043 | $0.0242 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $27,033,852,813 | $0.9987 |
| 2 | btc | -0.02% | $13,755,880,552 | $90,513.0000 |
| 3 | eth | 0.12% | $6,849,784,238 | $3,087.6100 |
| 4 | usdc | 0.04% | $4,098,078,831 | $1.0000 |
| 5 | sol | 0.25% | $1,733,155,787 | $136.2000 |


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
