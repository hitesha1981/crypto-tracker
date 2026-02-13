# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-13 01:43 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 29.60% | $39,292,211 | $21.9600 |
| 2 | kite | 16.88% | $100,671,926 | $0.1925 |
| 3 | lpt | 12.37% | $79,652,046 | $2.6800 |
| 4 | h | 10.83% | $33,684,614 | $0.1675 |
| 5 | adi | 9.39% | $4,869,479 | $3.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bera | -22.22% | $438,191,213 | $0.7030 |
| 2 | skr | -15.70% | $18,427,089 | $0.0229 |
| 3 | uds | -12.27% | $325,381 | $1.5700 |
| 4 | kag | -8.48% | $1,945,977 | $76.3600 |
| 5 | sent | -8.46% | $26,529,474 | $0.0237 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $75,397,101,030 | $0.9994 |
| 2 | btc | -2.13% | $48,314,734,231 | $66,421.0000 |
| 3 | eth | -1.29% | $18,821,514,097 | $1,946.7200 |
| 4 | usdc | 0.00% | $10,290,720,210 | $0.9999 |
| 5 | sol | -2.62% | $3,833,762,243 | $78.4000 |


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
