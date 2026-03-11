# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-11 01:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | flow | 26.20% | $197,615,418 | $0.0691 |
| 2 | bsv | 26.16% | $50,598,876 | $16.5800 |
| 3 | akt | 20.52% | $43,908,639 | $0.4614 |
| 4 | river | 17.51% | $44,784,525 | $14.0500 |
| 5 | xpl | 10.66% | $101,404,968 | $0.1019 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | -8.64% | $27,805,702 | $4.3000 |
| 2 | fil | -8.25% | $152,623,556 | $0.8651 |
| 3 | kite | -6.25% | $87,704,118 | $0.2749 |
| 4 | night | -6.12% | $9,327,231 | $0.0527 |
| 5 | skr | -5.78% | $10,147,365 | $0.0237 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $86,146,286,586 | $1.0000 |
| 2 | btc | 1.67% | $57,258,655,271 | $70,090.0000 |
| 3 | eth | 1.18% | $23,439,074,022 | $2,037.4600 |
| 4 | usdc | 0.01% | $13,557,459,064 | $1.0000 |
| 5 | sol | 0.63% | $4,459,830,502 | $86.1400 |


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
