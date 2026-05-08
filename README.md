# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-08 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jto | 42.50% | $390,335,772 | $0.5830 |
| 2 | siren | 26.74% | $62,819,765 | $1.0350 |
| 3 | dydx | 26.05% | $55,282,404 | $0.1844 |
| 4 | b | 14.56% | $41,540,229 | $0.3626 |
| 5 | strk | 12.33% | $84,067,414 | $0.0450 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | -24.53% | $103,236,805 | $0.5682 |
| 2 | ub | -10.01% | $17,588,446 | $0.1250 |
| 3 | hash | -7.94% | $16,534 | $0.0105 |
| 4 | asteroid | -7.87% | $22,050,211 | $0.0003 |
| 5 | beat | -6.81% | $3,314,834 | $0.5045 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $70,136,742,108 | $0.9999 |
| 2 | btc | -1.74% | $37,299,808,576 | $79,482.0000 |
| 3 | eth | -1.83% | $20,935,501,282 | $2,274.5400 |
| 4 | usdc | -0.01% | $14,259,877,460 | $0.9997 |
| 5 | sol | -0.13% | $3,730,934,054 | $87.7900 |


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
