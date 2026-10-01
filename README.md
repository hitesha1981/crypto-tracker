# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-01 03:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bp | 27.13% | $21,867,510 | $1.5600 |
| 2 | trac | 25.60% | $50,651,118 | $0.4856 |
| 3 | night | 24.30% | $89,405,015 | $0.0404 |
| 4 | stx | 22.37% | $101,748,356 | $0.3820 |
| 5 | mon | 21.74% | $115,785,626 | $0.0324 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stonk | -18.05% | $35,108,668 | $0.2466 |
| 2 | ai | -15.90% | $21,310,499 | $0.1512 |
| 3 | br | -14.20% | $5,401,033 | $0.6866 |
| 4 | 2z | -11.31% | $13,759,034 | $0.0584 |
| 5 | hash | -8.81% | $13,289 | $0.0065 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $64,869,696,984 | $0.9995 |
| 2 | btc | 0.21% | $35,597,193,791 | $83,403.0000 |
| 3 | usdc | -0.00% | $18,523,369,399 | $0.9998 |
| 4 | eth | 0.56% | $13,866,701,933 | $2,684.7100 |
| 5 | sol | -1.12% | $4,228,369,937 | $117.9400 |


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
