# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-13 04:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | shfl | 5.25% | $601,313 | $0.3960 |
| 2 | bdx | 3.34% | $11,819,928 | $0.0729 |
| 3 | googlb | 1.55% | $29,710,310 | $299.8200 |
| 4 | sn51 | 1.32% | $14,402,447 | $24.2600 |
| 5 | nvdab | 1.07% | $283,290,341 | $163.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -20.11% | $6,444,462 | $0.8399 |
| 2 | hash | -15.13% | $36,572 | $0.0065 |
| 3 | anvl | -12.25% | $411,077 | $0.0020 |
| 4 | gt | -11.76% | $8,633,718 | $8.6800 |
| 5 | stx | -9.76% | $14,667,521 | $0.2755 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $52,690,118,738 | $0.9992 |
| 2 | btc | -6.67% | $35,452,334,221 | $68,782.0000 |
| 3 | usdc | 0.01% | $15,074,459,973 | $0.9996 |
| 4 | eth | -6.08% | $12,735,558,784 | $1,927.8700 |
| 5 | sol | -5.82% | $2,722,307,496 | $78.2400 |


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
