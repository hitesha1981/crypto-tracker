# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-19 02:40 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | 10.31% | $7,884 | $0.0073 |
| 2 | vvv | 9.98% | $27,228,934 | $24.5300 |
| 3 | sent | 7.85% | $20,901,191 | $0.0231 |
| 4 | prl | 7.21% | $4,366,102 | $1.9500 |
| 5 | bp | 6.77% | $6,112,542 | $1.1300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -19.69% | $72,335,783 | $0.1101 |
| 2 | a | -17.03% | $17,350,433 | $0.0894 |
| 3 | pons | -8.48% | $32,699,815 | $0.2601 |
| 4 | useless | -6.24% | $13,342,467 | $0.1444 |
| 5 | eigen | -6.13% | $25,677,785 | $0.2339 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $39,896,435,577 | $0.9992 |
| 2 | btc | 0.90% | $21,462,172,338 | $82,388.0000 |
| 3 | usdc | 0.00% | $11,044,888,149 | $0.9998 |
| 4 | eth | 0.39% | $8,802,775,147 | $2,419.0500 |
| 5 | sol | 1.19% | $2,426,655,583 | $104.8900 |


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
