# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-22 02:42 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | aioz | 43.09% | $42,982,221 | $0.1289 |
| 2 | form | 33.30% | $63,440,253 | $0.3480 |
| 3 | hood | 26.24% | $68,746 | $0.1510 |
| 4 | pepe | 25.34% | $1,239,885,175 | $0.0000 |
| 5 | wif | 23.87% | $150,351,859 | $0.2490 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ai | -12.18% | $24,449,552 | $0.2391 |
| 2 | br | -12.08% | $18,214,073 | $1.1100 |
| 3 | strk | -9.87% | $79,773,048 | $0.0435 |
| 4 | pendle | -6.67% | $88,901,792 | $2.5000 |
| 5 | h | -5.81% | $5,860,359 | $0.0671 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $103,700,329,776 | $0.9998 |
| 2 | btc | 5.53% | $60,720,535,064 | $85,764.0000 |
| 3 | usdc | 0.02% | $27,388,177,667 | $0.9999 |
| 4 | eth | 3.20% | $25,340,741,790 | $2,745.1500 |
| 5 | sol | 5.90% | $6,630,975,995 | $117.9300 |


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
