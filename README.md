# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-02 02:36 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 57.09% | $22,284,153 | $1.2400 |
| 2 | rif | 32.61% | $31,465,087 | $0.1218 |
| 3 | b | 13.24% | $7,566,113 | $0.2373 |
| 4 | morpho | 12.61% | $44,781,567 | $2.1400 |
| 5 | pendle | 11.07% | $39,233,140 | $1.4800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | tac | -40.21% | $22,460,307 | $0.0374 |
| 2 | lab | -26.83% | $28,878,115 | $9.2300 |
| 3 | dydx | -25.01% | $88,743,673 | $0.1361 |
| 4 | h | -15.91% | $27,097,892 | $0.0720 |
| 5 | coco | -11.31% | $329,182 | $0.1926 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $57,977,468,664 | $0.9988 |
| 2 | btc | 2.11% | $37,945,685,263 | $60,203.0000 |
| 3 | usdc | 0.01% | $13,628,120,914 | $0.9997 |
| 4 | eth | 2.16% | $10,542,272,239 | $1,618.5700 |
| 5 | sol | 5.00% | $3,578,592,667 | $78.1800 |


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
