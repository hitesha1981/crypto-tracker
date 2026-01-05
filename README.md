# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-05 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bonk | 21.29% | $777,339,245 | $0.0000 |
| 2 | pippin | 20.40% | $40,849,565 | $0.5145 |
| 3 | wstx | 17.37% | $931 | $0.3506 |
| 4 | wif | 17.09% | $463,524,375 | $0.4004 |
| 5 | stx | 15.44% | $92,423,520 | $0.3550 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -7.38% | $34,342,030 | $12.9800 |
| 2 | night | -3.89% | $35,335,458 | $0.0899 |
| 3 | merl | -3.46% | $23,172,341 | $0.2535 |
| 4 | cc | -3.37% | $16,443,348 | $0.1510 |
| 5 | leo | -3.25% | $747,229 | $8.9600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $58,027,405,402 | $0.9996 |
| 2 | btc | 1.82% | $33,271,922,078 | $92,895.0000 |
| 3 | eth | 1.11% | $14,928,470,859 | $3,189.1800 |
| 4 | usdc | -0.00% | $6,859,146,004 | $0.9999 |
| 5 | xrp | 4.28% | $3,650,194,521 | $2.1300 |


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
