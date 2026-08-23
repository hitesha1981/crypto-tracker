# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-23 00:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trump | 26.80% | $2,315,526,011 | $2.3700 |
| 2 | pump | 24.50% | $751,269,502 | $0.0049 |
| 3 | melania | 18.60% | $39,731,622 | $0.1084 |
| 4 | stx | 17.70% | $85,861,148 | $0.2211 |
| 5 | zro | 16.00% | $111,348,945 | $1.1700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kag | -15.80% | $2,115 | $52.7100 |
| 2 | pieverse | -14.70% | $11,637,033 | $0.9645 |
| 3 | shib | -11.80% | $235,682,418 | $0.0000 |
| 4 | zbcn | -11.30% | $9,621,917 | $0.0019 |
| 5 | grass | -10.20% | $27,140,277 | $0.3037 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sand | -7.70% | $18,585,982,494,929 | $0.0457 |
| 2 | usdt | 0.00% | $81,861,038,991 | $0.9998 |
| 3 | btc | -1.70% | $36,107,576,212 | $77,283.0000 |
| 4 | eth | -3.90% | $20,135,738,842 | $2,429.2300 |
| 5 | usdc | 0.00% | $19,404,234,957 | $0.9999 |


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
