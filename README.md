# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-02 02:04 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | 151.76% | $97,879,531 | $0.3246 |
| 2 | ub | 69.67% | $182,026,213 | $0.1256 |
| 3 | 9bit | 30.08% | $5,743,326 | $0.0300 |
| 4 | zec | 11.01% | $742,006,329 | $383.2000 |
| 5 | mon | 10.98% | $104,741,552 | $0.0307 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | asteroid | -17.47% | $15,563,624 | $0.0003 |
| 2 | wlfi | -10.77% | $112,805,167 | $0.0540 |
| 3 | btse | -8.52% | $6,310,836 | $1.0440 |
| 4 | m | -7.54% | $13,106,414 | $2.9700 |
| 5 | mega | -6.93% | $195,520,809 | $0.1571 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $58,349,334,949 | $0.9998 |
| 2 | btc | 2.24% | $39,193,896,393 | $78,322.0000 |
| 3 | eth | 1.45% | $12,121,674,543 | $2,297.9600 |
| 4 | usdc | 0.02% | $11,029,361,243 | $0.9998 |
| 5 | sol | 0.58% | $2,658,216,426 | $84.0600 |


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
