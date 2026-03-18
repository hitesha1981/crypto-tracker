# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-18 01:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 44.75% | $39,503,703 | $0.7518 |
| 2 | river | 17.21% | $36,576,644 | $22.3300 |
| 3 | m | 12.30% | $11,140,763 | $1.8700 |
| 4 | kas | 10.16% | $34,334,083 | $0.0370 |
| 5 | dexe | 9.03% | $13,214,078 | $5.6600 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -32.30% | $57,541,160 | $0.1292 |
| 2 | ban | -18.13% | $19,342,127 | $0.1189 |
| 3 | qubic | -11.75% | $3,792,834 | $0.0000 |
| 4 | pi | -10.46% | $44,357,615 | $0.1740 |
| 5 | grass | -8.33% | $23,075,812 | $0.4131 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $76,662,032,800 | $1.0000 |
| 2 | btc | -2.55% | $45,297,867,484 | $74,004.0000 |
| 3 | eth | -1.49% | $23,304,021,812 | $2,329.2700 |
| 4 | usdc | -0.00% | $12,150,864,100 | $0.9999 |
| 5 | xrp | -3.07% | $4,120,170,094 | $1.5200 |


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
