# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-24 02:35 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rusd | 233.17% | $312 | $0.9987 |
| 2 | beat | 35.18% | $54,074,749 | $2.2700 |
| 3 | btw | 18.37% | $27,961,738 | $0.0989 |
| 4 | dydx | 14.22% | $26,246,716 | $0.1527 |
| 5 | grass | 6.15% | $31,336,000 | $0.4379 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -25.63% | $40,065,960 | $0.0728 |
| 2 | lab | -15.69% | $44,774,431 | $14.3000 |
| 3 | wld | -14.38% | $343,799,505 | $0.5243 |
| 4 | vvv | -11.06% | $29,119,560 | $13.5100 |
| 5 | eigen | -10.29% | $38,533,321 | $0.2467 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $48,138,106,290 | $0.9988 |
| 2 | btc | -2.27% | $30,728,648,457 | $62,664.0000 |
| 3 | usdc | 0.01% | $11,464,610,255 | $0.9998 |
| 4 | eth | -3.71% | $10,955,154,088 | $1,665.1600 |
| 5 | sol | -3.11% | $2,233,668,547 | $69.6100 |


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
