# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-21 02:39 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jto | 32.05% | $123,405,561 | $0.5427 |
| 2 | bsb | 27.95% | $127,104,664 | $1.0460 |
| 3 | cheems | 27.46% | $1,783,205 | $0.0000 |
| 4 | bananas31 | 25.06% | $49,000,026 | $0.0141 |
| 5 | nex | 24.75% | $12,214,195 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bill | -23.89% | $87,656,160 | $0.0834 |
| 2 | m | -13.66% | $8,411,613 | $2.9900 |
| 3 | ub | -7.51% | $12,228,987 | $0.1147 |
| 4 | chz | -4.68% | $75,270,421 | $0.0455 |
| 5 | kite | -4.48% | $52,996,839 | $0.2340 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $52,242,491,379 | $0.9990 |
| 2 | btc | 1.80% | $28,922,046,199 | $77,969.0000 |
| 3 | usdc | -0.00% | $13,801,868,853 | $0.9997 |
| 4 | eth | 1.72% | $11,299,266,981 | $2,143.2800 |
| 5 | sol | 3.13% | $2,732,075,174 | $86.6900 |


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
