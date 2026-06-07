# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-07 02:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | allo | 122.05% | $376,413,423 | $0.4701 |
| 2 | skyai | 84.51% | $76,942,571 | $0.3594 |
| 3 | lab | 60.05% | $136,415,063 | $14.7200 |
| 4 | gwei | 41.79% | $6,084,710 | $0.1490 |
| 5 | beat | 33.76% | $34,774,679 | $2.3500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qait | -17.73% | $19,191,057 | $0.0281 |
| 2 | kau | -13.27% | $26,631 | $123.8100 |
| 3 | vvv | -11.00% | $68,504,412 | $16.0700 |
| 4 | apxusd | -7.73% | $6,716,081 | $0.9211 |
| 5 | wld | -6.48% | $753,748,133 | $0.4472 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $55,774,792,167 | $0.9995 |
| 2 | btc | 0.64% | $32,055,070,206 | $61,448.0000 |
| 3 | eth | 0.50% | $18,807,964,843 | $1,590.8300 |
| 4 | usdc | -0.01% | $12,654,179,346 | $0.9997 |
| 5 | sol | -0.36% | $3,758,238,364 | $63.4000 |


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
