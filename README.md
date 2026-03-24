# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-24 01:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jto | 24.83% | $101,297,019 | $0.3510 |
| 2 | uds | 20.00% | $366,462 | $1.8000 |
| 3 | sn3 | 15.24% | $6,561,542 | $26.3500 |
| 4 | zro | 13.37% | $101,480,266 | $2.2000 |
| 5 | ar | 12.90% | $42,708,509 | $1.9100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -18.85% | $53,654,573 | $24.1200 |
| 2 | siren | -15.87% | $52,012,219 | $2.0300 |
| 3 | grass | -8.85% | $18,621,135 | $0.3327 |
| 4 | vvv | -8.49% | $16,340,715 | $5.6800 |
| 5 | bard | -6.38% | $45,250,529 | $0.4769 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $89,331,968,275 | $0.9998 |
| 2 | btc | 3.86% | $51,988,327,714 | $70,702.0000 |
| 3 | eth | 4.02% | $28,033,045,283 | $2,143.8100 |
| 4 | usdc | 0.00% | $7,839,429,406 | $0.9999 |
| 5 | sol | 5.08% | $5,346,736,241 | $90.8100 |


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
