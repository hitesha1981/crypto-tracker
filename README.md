# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-12 01:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ip | 25.47% | $117,577,216 | $2.5000 |
| 2 | xmr | 23.53% | $272,720,620 | $585.4700 |
| 3 | river | 19.51% | $37,706,039 | $17.3000 |
| 4 | xcn | 18.14% | $56,387,410 | $0.0094 |
| 5 | ultima | 14.92% | $18,841,198 | $6,923.9700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pol | -7.02% | $376,777,451 | $0.1628 |
| 2 | pippin | -5.85% | $34,729,706 | $0.3469 |
| 3 | zbcn | -4.98% | $8,796,907 | $0.0028 |
| 4 | m | -4.59% | $6,960,729 | $1.6400 |
| 5 | bdx | -4.18% | $9,553,776 | $0.0848 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $41,519,339,796 | $0.9986 |
| 2 | btc | 1.00% | $22,285,992,087 | $91,403.0000 |
| 3 | eth | 1.17% | $12,241,653,426 | $3,123.1700 |
| 4 | usdc | -0.04% | $5,758,376,970 | $0.9998 |
| 5 | sol | 3.65% | $4,026,385,369 | $141.1700 |


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
