# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-05 03:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | akt | 19.64% | $35,067,987 | $0.8148 |
| 2 | fet | 17.63% | $266,566,853 | $0.2610 |
| 3 | btw | 17.54% | $29,001,478 | $1.0990 |
| 4 | ada | 11.09% | $796,368,352 | $0.2701 |
| 5 | strk | 10.39% | $164,302,772 | $0.0578 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | -15.95% | $12,074,228 | $0.0114 |
| 2 | br | -13.47% | $4,163,495 | $0.4343 |
| 3 | night | -7.69% | $35,148,309 | $0.0455 |
| 4 | qnt | -6.39% | $205,279,976 | $250.6400 |
| 5 | edge | -6.27% | $2,289,353 | $0.4592 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $35,608,892,394 | $0.9998 |
| 2 | btc | 1.83% | $20,328,699,525 | $86,361.0000 |
| 3 | usdc | -0.01% | $8,506,104,268 | $0.9999 |
| 4 | eth | 1.12% | $7,192,893,789 | $2,723.4600 |
| 5 | sol | 0.48% | $2,178,848,460 | $120.8900 |


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
