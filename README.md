# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-02 01:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | vvv | 24.84% | $41,368,321 | $6.6400 |
| 2 | river | 12.02% | $30,281,529 | $14.1000 |
| 3 | b | 11.16% | $6,094,178 | $0.1913 |
| 4 | ath | 8.05% | $60,361,964 | $0.0064 |
| 5 | jup | 7.43% | $53,321,742 | $0.1716 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | tibbir | -13.55% | $7,954,373 | $0.1543 |
| 2 | power | -9.73% | $105,772,258 | $1.7700 |
| 3 | qrl | -7.04% | $100,819 | $1.4500 |
| 4 | siren | -7.03% | $12,838,659 | $0.2573 |
| 5 | skr | -4.64% | $24,263,656 | $0.0219 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $75,481,698,648 | $1.0000 |
| 2 | btc | 0.73% | $45,078,469,413 | $66,693.0000 |
| 3 | eth | 0.92% | $24,508,804,596 | $1,973.7400 |
| 4 | sol | 1.01% | $5,151,144,369 | $85.3100 |
| 5 | usdc | 0.01% | $4,402,783,389 | $1.0000 |


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
