# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-26 02:02 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | 72.94% | $42,689,784 | $0.7463 |
| 2 | axs | 24.36% | $839,795,104 | $1.4400 |
| 3 | b | 22.25% | $7,153,349 | $0.1232 |
| 4 | ray | 20.01% | $115,876,629 | $0.8020 |
| 5 | asteroid | 13.26% | $38,311,803 | $0.0003 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ape | -25.72% | $424,936,507 | $0.1544 |
| 2 | chip | -11.82% | $198,222,015 | $0.0702 |
| 3 | trump | -11.16% | $522,203,367 | $2.5800 |
| 4 | edge | -10.26% | $9,429,997 | $1.3000 |
| 5 | genius | -8.39% | $11,520,768 | $0.5805 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $29,458,473,501 | $1.0000 |
| 2 | btc | -0.09% | $16,796,087,895 | $77,483.0000 |
| 3 | eth | -0.13% | $6,020,681,402 | $2,314.5000 |
| 4 | usdc | 0.00% | $5,058,971,162 | $0.9998 |
| 5 | sol | -0.33% | $1,611,726,798 | $86.0000 |


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
