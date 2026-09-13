# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-13 02:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lsk | 195.36% | $230,915,143 | $0.5512 |
| 2 | 龙虾 | 59.86% | $65,748,690 | $0.1497 |
| 3 | nock | 31.23% | $5,568,385 | $0.0529 |
| 4 | ai | 14.29% | $31,045,254 | $0.2980 |
| 5 | ake | 14.14% | $28,734,763 | $0.0159 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | apepe | -14.75% | $17,870,572 | $0.0000 |
| 2 | ray | -12.46% | $85,771,394 | $1.4900 |
| 3 | uai | -10.72% | $15,900,460 | $0.5903 |
| 4 | prl | -10.25% | $862,754 | $0.5287 |
| 5 | stonk | -9.10% | $57,739,952 | $0.2672 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $29,741,797,466 | $0.9998 |
| 2 | btc | -0.04% | $15,370,653,411 | $77,268.0000 |
| 3 | eth | 0.33% | $7,792,126,225 | $2,522.4400 |
| 4 | usdc | 0.00% | $5,585,576,714 | $0.9999 |
| 5 | sol | 0.10% | $1,846,150,199 | $101.9000 |


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
