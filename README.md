# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-22 02:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hoodinu | 136.01% | $27,639,237 | $0.1589 |
| 2 | grx | 30.05% | $2,250,610 | $20.7300 |
| 3 | lit | 11.17% | $156,163,374 | $3.7600 |
| 4 | kntq | 11.04% | $5,248,333 | $0.3957 |
| 5 | pearl | 10.91% | $16,876,825 | $2.3700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -32.02% | $21,644,054 | $0.0226 |
| 2 | br | -27.58% | $13,993,063 | $0.4627 |
| 3 | btw | -18.09% | $27,288,817 | $1.6700 |
| 4 | hash | -13.09% | $106,748 | $0.0065 |
| 5 | anvl | -10.93% | $156,749 | $0.0017 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $56,917,596,154 | $0.9994 |
| 2 | btc | 0.18% | $34,157,416,809 | $82,884.0000 |
| 3 | usdc | -0.00% | $14,814,075,178 | $0.9997 |
| 4 | eth | -0.35% | $14,167,180,087 | $2,439.9800 |
| 5 | sol | -0.61% | $2,606,753,820 | $105.5500 |


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
