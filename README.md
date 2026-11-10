# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-10 05:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | 27.26% | $83,030,923 | $2.0400 |
| 2 | hash | 22.78% | $126,344 | $0.0074 |
| 3 | edge | 18.50% | $18,345,249 | $0.3960 |
| 4 | br | 14.64% | $5,495,504 | $0.4884 |
| 5 | cards | 13.54% | $12,052,467 | $0.2403 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -10.34% | $4,674,049 | $1.0020 |
| 2 | rain | -7.25% | $15,990,673 | $0.0046 |
| 3 | q | -6.58% | $6,595,465 | $0.0250 |
| 4 | zec | -5.92% | $975,519,965 | $1,151.3100 |
| 5 | zro | -5.70% | $70,364,325 | $1.4700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $47,871,625,712 | $0.9990 |
| 2 | btc | 0.33% | $28,141,040,298 | $74,733.0000 |
| 3 | usdc | 0.01% | $12,373,754,543 | $0.9995 |
| 4 | eth | -0.51% | $12,071,454,958 | $2,120.9600 |
| 5 | xrp | -0.69% | $2,242,575,190 | $1.0950 |


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
