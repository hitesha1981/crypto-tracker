# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-19 01:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sos | 137.31% | $649,402 | $0.0015 |
| 2 | siren | 17.74% | $30,231,541 | $0.8861 |
| 3 | river | 17.66% | $58,296,877 | $26.3300 |
| 4 | akt | 14.60% | $70,347,499 | $0.5511 |
| 5 | hash | 11.40% | $115,940 | $0.0144 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bard | -39.52% | $331,984,895 | $0.6505 |
| 2 | bera | -16.51% | $30,033,177 | $0.5456 |
| 3 | grass | -11.81% | $28,299,000 | $0.3660 |
| 4 | h | -11.48% | $19,569,446 | $0.1008 |
| 5 | zro | -10.92% | $81,772,140 | $2.1000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $79,248,989,983 | $1.0000 |
| 2 | btc | -4.06% | $47,173,137,841 | $71,041.0000 |
| 3 | eth | -5.96% | $24,514,362,539 | $2,192.0100 |
| 4 | usdc | 0.01% | $4,429,859,511 | $1.0000 |
| 5 | sol | -4.91% | $4,075,039,477 | $90.0800 |


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
