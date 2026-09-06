# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-06 02:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | arb | 48.88% | $708,534,047 | $0.1947 |
| 2 | pons | 43.30% | $205,277,166 | $0.9467 |
| 3 | 牛来 | 41.54% | $42,052,616 | $0.1194 |
| 4 | uai | 36.84% | $31,648,352 | $0.6153 |
| 5 | marscoin | 36.18% | $196,605,558 | $0.2463 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dcr | -10.26% | $11,991,465 | $16.1200 |
| 2 | cards | -8.83% | $4,161,996 | $0.1304 |
| 3 | rlb | -7.90% | $414,896 | $0.0756 |
| 4 | hash | -7.70% | $1,947 | $0.0074 |
| 5 | h | -7.65% | $2,795,203 | $0.0757 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $40,253,250,030 | $1.0000 |
| 2 | btc | 0.49% | $18,908,960,257 | $79,974.0000 |
| 3 | usdc | 0.00% | $8,891,371,336 | $1.0000 |
| 4 | eth | 2.23% | $7,489,304,488 | $2,507.3800 |
| 5 | sol | 2.27% | $2,510,110,022 | $104.1700 |


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
