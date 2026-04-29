# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-29 02:13 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skyai | 36.22% | $34,360,195 | $0.2251 |
| 2 | h | 25.74% | $73,890,554 | $0.1761 |
| 3 | bsb | 19.00% | $35,852,863 | $0.8381 |
| 4 | ub | 17.08% | $12,294,514 | $0.0570 |
| 5 | lit | 9.79% | $31,852,826 | $0.9352 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zbcn | -13.93% | $11,456,276 | $0.0033 |
| 2 | dexe | -12.18% | $39,103,045 | $12.5400 |
| 3 | chip | -11.85% | $323,970,720 | $0.0678 |
| 4 | b | -10.41% | $6,241,549 | $0.1222 |
| 5 | chz | -6.62% | $81,604,691 | $0.0466 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $55,212,749,855 | $0.9998 |
| 2 | btc | -0.74% | $33,197,605,909 | $76,560.0000 |
| 3 | usdc | -0.01% | $12,848,853,407 | $0.9998 |
| 4 | eth | -0.22% | $12,120,977,972 | $2,293.0800 |
| 5 | sol | -0.34% | $2,549,524,559 | $84.1400 |


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
