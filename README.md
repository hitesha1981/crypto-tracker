# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-13 04:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rsr | 28.27% | $248,277,471 | $0.0021 |
| 2 | q | 16.26% | $14,644,478 | $0.0363 |
| 3 | prl | 11.66% | $7,230,902 | $1.5300 |
| 4 | stx | 10.80% | $100,581,694 | $0.4315 |
| 5 | bdx | 10.32% | $3,033,525 | $0.0900 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | w | -32.89% | $285,768,117 | $0.0192 |
| 2 | pons | -20.06% | $58,167,555 | $0.2826 |
| 3 | strk | -16.85% | $383,950,096 | $0.0882 |
| 4 | cards | -15.27% | $9,604,565 | $0.2841 |
| 5 | pump | -14.08% | $240,041,255 | $0.0051 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $62,729,882,366 | $0.9992 |
| 2 | btc | -0.74% | $31,855,685,793 | $83,351.0000 |
| 3 | usdc | 0.01% | $19,039,908,896 | $0.9998 |
| 4 | eth | -1.80% | $16,409,665,396 | $2,513.4500 |
| 5 | sol | -4.32% | $4,037,794,052 | $107.8900 |


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
