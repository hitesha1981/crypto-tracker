# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-16 01:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dcr | 12.11% | $34,208,389 | $25.1400 |
| 2 | river | 11.55% | $42,682,642 | $25.8900 |
| 3 | hash | 10.23% | $16,613 | $0.0263 |
| 4 | h | 8.15% | $82,358,047 | $0.1976 |
| 5 | zbcn | 6.48% | $15,671,641 | $0.0030 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ip | -23.08% | $216,352,327 | $2.6000 |
| 2 | xpl | -11.07% | $111,343,624 | $0.1439 |
| 3 | glm | -10.92% | $17,421,079 | $0.2830 |
| 4 | lit | -10.71% | $204,640,331 | $1.8900 |
| 5 | icp | -9.03% | $470,943,171 | $4.3400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $92,892,917,948 | $0.9997 |
| 2 | btc | -1.45% | $57,954,735,443 | $95,493.0000 |
| 3 | eth | -0.98% | $27,886,897,968 | $3,307.0000 |
| 4 | usdc | -0.02% | $14,424,993,338 | $0.9996 |
| 5 | sol | -2.76% | $4,886,113,699 | $142.2300 |


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
