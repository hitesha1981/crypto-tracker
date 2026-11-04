# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-04 04:14 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | a7a5 | 580.98% | $8,360 | $0.0120 |
| 2 | yellow | 29.59% | $3,441,819 | $0.1705 |
| 3 | fluid | 14.58% | $3,578,913 | $2.0700 |
| 4 | kntq | 13.92% | $8,800,928 | $0.4928 |
| 5 | rune | 12.03% | $168,678,857 | $0.6277 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beam | -11.71% | $33,555,906 | $0.0038 |
| 2 | trump | -4.81% | $106,985,511 | $1.5100 |
| 3 | sent | -4.77% | $3,627,161 | $0.0187 |
| 4 | hash | -4.37% | $2,605 | $0.0062 |
| 5 | cvx | -3.95% | $5,229,638 | $1.8400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $44,052,125,675 | $0.9988 |
| 2 | btc | 0.12% | $27,251,381,828 | $76,882.0000 |
| 3 | usdc | 0.01% | $12,497,090,375 | $0.9995 |
| 4 | eth | 0.69% | $9,208,151,476 | $2,265.1900 |
| 5 | sol | -0.21% | $2,358,984,850 | $91.8800 |


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
