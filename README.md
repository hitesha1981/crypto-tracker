# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-12 01:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bera | 11.79% | $39,291,118 | $0.6047 |
| 2 | ar | 8.69% | $36,980,726 | $1.7900 |
| 3 | qrl | 8.61% | $79,189 | $1.5700 |
| 4 | icp | 8.52% | $390,979,463 | $2.6100 |
| 5 | beam | 7.98% | $20,796,208 | $0.0022 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -14.83% | $4,667,880 | $0.1755 |
| 2 | night | -10.32% | $111,872,581 | $0.0472 |
| 3 | bsv | -10.10% | $28,815,395 | $14.9000 |
| 4 | kite | -8.41% | $70,734,995 | $0.2518 |
| 5 | akt | -8.03% | $13,337,469 | $0.4244 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $71,929,954,650 | $1.0000 |
| 2 | btc | -0.18% | $47,197,423,404 | $69,972.0000 |
| 3 | eth | 0.59% | $18,253,582,665 | $2,049.3900 |
| 4 | usdc | 0.00% | $8,129,328,871 | $1.0000 |
| 5 | sol | 0.24% | $3,925,962,496 | $86.3400 |


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
