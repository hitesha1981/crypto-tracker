# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-12 02:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | 50.90% | $130,561,507 | $0.6103 |
| 2 | h | 26.96% | $63,122,698 | $0.2743 |
| 3 | bill | 22.72% | $326,199,191 | $0.1406 |
| 4 | tel | 22.14% | $2,396,547 | $0.0027 |
| 5 | bananas31 | 20.80% | $38,487,533 | $0.0146 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | 币安人生 | -14.02% | $31,918,864 | $0.3734 |
| 2 | cfg | -7.77% | $19,435,274 | $0.2869 |
| 3 | jasmy | -7.53% | $25,499,417 | $0.0069 |
| 4 | apepe | -6.81% | $32,797,343 | $0.0000 |
| 5 | mega | -6.73% | $45,649,086 | $0.1166 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $58,590,808,356 | $0.9997 |
| 2 | btc | -0.06% | $32,547,050,879 | $81,167.0000 |
| 3 | usdc | -0.01% | $14,163,788,398 | $0.9998 |
| 4 | eth | -1.64% | $14,110,833,011 | $2,311.5300 |
| 5 | sol | 0.79% | $4,191,624,731 | $96.3300 |


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
