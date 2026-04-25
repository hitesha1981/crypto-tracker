# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-25 01:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ape | 114.30% | $1,072,287,519 | $0.2182 |
| 2 | ohm | 16.24% | $2,607,857 | $20.2000 |
| 3 | gala | 15.40% | $87,355,083 | $0.0037 |
| 4 | dydx | 14.52% | $32,484,090 | $0.1700 |
| 5 | river | 10.95% | $39,384,706 | $6.5100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stable | -23.09% | $49,002,749 | $0.0318 |
| 2 | grass | -20.00% | $31,695,295 | $0.3713 |
| 3 | chip | -18.92% | $896,609,168 | $0.0810 |
| 4 | rave | -17.77% | $65,378,441 | $0.8917 |
| 5 | pieverse | -10.74% | $27,914,929 | $0.7696 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $55,033,923,173 | $1.0000 |
| 2 | btc | -0.77% | $33,121,460,803 | $77,604.0000 |
| 3 | usdc | 0.00% | $12,368,654,427 | $0.9999 |
| 4 | eth | -0.31% | $11,837,933,518 | $2,320.8100 |
| 5 | sol | 0.42% | $2,876,018,364 | $86.3400 |


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
