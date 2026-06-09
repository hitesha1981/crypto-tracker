# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-09 02:30 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | gwei | 31.45% | $32,346,870 | $0.1683 |
| 2 | velvet | 24.31% | $32,014,910 | $0.3222 |
| 3 | beat | 23.07% | $63,352,058 | $4.3200 |
| 4 | btw | 14.70% | $22,140,871 | $0.0586 |
| 5 | eurs | 10.57% | $3,693 | $1.2200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -83.04% | $590,116,019 | $0.1213 |
| 2 | ff | -11.91% | $13,526,018 | $0.0820 |
| 3 | trac | -11.88% | $9,748,947 | $0.3449 |
| 4 | edge | -11.26% | $10,001,433 | $0.4114 |
| 5 | 币安人生 | -10.67% | $50,460,451 | $0.7352 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $58,487,863,151 | $0.9995 |
| 2 | btc | -0.45% | $35,122,800,484 | $62,717.0000 |
| 3 | eth | -1.03% | $16,278,402,021 | $1,663.6700 |
| 4 | usdc | -0.01% | $15,058,452,187 | $0.9996 |
| 5 | sol | -1.02% | $3,233,513,175 | $65.7800 |


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
