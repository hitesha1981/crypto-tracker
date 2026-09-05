# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-05 02:19 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | marscoin | 43.09% | $190,750,852 | $0.1800 |
| 2 | dash | 37.85% | $531,957,948 | $66.5400 |
| 3 | q | 33.79% | $14,218,045 | $0.0287 |
| 4 | ake | 29.51% | $52,967,705 | $0.0187 |
| 5 | dcr | 27.39% | $8,477,080 | $18.1200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | -17.03% | $51,088,233 | $0.2296 |
| 2 | ai | -13.15% | $64,744,253 | $0.2259 |
| 3 | cards | -13.09% | $8,832,290 | $0.1430 |
| 4 | hnt | -11.97% | $36,853,619 | $0.6230 |
| 5 | zro | -9.45% | $48,663,786 | $1.0330 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $64,860,067,196 | $1.0000 |
| 2 | btc | -1.53% | $34,008,965,963 | $79,578.0000 |
| 3 | usdc | 0.00% | $17,596,084,969 | $1.0000 |
| 4 | eth | -2.02% | $15,561,190,596 | $2,452.4700 |
| 5 | sol | -1.70% | $3,235,899,908 | $101.8600 |


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
