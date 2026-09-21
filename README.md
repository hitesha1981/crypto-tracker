# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-21 02:40 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stonk | 32.57% | $47,116,137 | $0.3563 |
| 2 | bp | 31.10% | $25,790,213 | $0.8720 |
| 3 | btw | 25.27% | $21,905,862 | $0.7515 |
| 4 | kmno | 22.01% | $34,240,719 | $0.0344 |
| 5 | vvv | 21.16% | $120,835,701 | $32.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -20.86% | $84,546,764 | $0.0523 |
| 2 | prl | -13.81% | $2,259,500 | $0.9467 |
| 3 | ub | -13.59% | $28,664,772 | $0.1316 |
| 4 | h | -10.45% | $3,630,519 | $0.0714 |
| 5 | meta | -8.40% | $638,819 | $5.3900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $54,346,810,906 | $0.9997 |
| 2 | btc | 0.43% | $26,632,155,065 | $81,247.0000 |
| 3 | eth | 2.03% | $14,584,501,944 | $2,659.4300 |
| 4 | usdc | 0.01% | $13,755,028,019 | $0.9997 |
| 5 | sol | 1.82% | $3,588,796,034 | $111.3400 |


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
