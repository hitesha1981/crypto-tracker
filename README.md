# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-20 02:43 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | blorb | 88.73% | $18,086,986 | $0.2323 |
| 2 | ake | 57.66% | $144,882,848 | $0.0659 |
| 3 | br | 28.31% | $28,019,375 | $1.0970 |
| 4 | zama | 27.98% | $156,800,671 | $0.0788 |
| 5 | m | 20.52% | $2,476,441 | $1.5700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | -21.16% | $14,506,134 | $0.1783 |
| 2 | useless | -15.91% | $27,236,910 | $0.2522 |
| 3 | pons | -14.86% | $76,494,060 | $0.5860 |
| 4 | ai | -14.68% | $20,809,349 | $0.2675 |
| 5 | meta | -10.18% | $28,888,614 | $5.9000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $47,757,117,115 | $0.9995 |
| 2 | btc | -0.56% | $22,704,343,115 | $80,838.0000 |
| 3 | usdc | -0.01% | $11,735,527,826 | $0.9997 |
| 4 | eth | -0.52% | $10,317,029,605 | $2,605.0200 |
| 5 | xrp | -2.37% | $2,946,621,952 | $1.3900 |


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
