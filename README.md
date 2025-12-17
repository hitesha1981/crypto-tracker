# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-17 01:04 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fartcoin | 10.08% | $99,053,638 | $0.3537 |
| 2 | spx | 6.50% | $18,346,566 | $0.5403 |
| 3 | tel | 5.61% | $2,905,909 | $0.0043 |
| 4 | apepe | 5.39% | $17,140,322 | $0.0000 |
| 5 | fbtc | 5.17% | $85,021 | $90,242.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -29.56% | $101,254,951 | $0.3075 |
| 2 | beat | -16.77% | $109,057,954 | $2.3300 |
| 3 | nft | -12.53% | $38,694,382 | $0.0000 |
| 4 | uds | -12.22% | $1,177,019 | $2.3100 |
| 5 | m | -6.59% | $13,837,886 | $1.6500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $73,855,452,672 | $0.9999 |
| 2 | btc | 1.83% | $47,359,394,624 | $87,575.0000 |
| 3 | eth | 0.36% | $23,528,359,423 | $2,952.9800 |
| 4 | usdc | 0.00% | $11,338,082,613 | $1.0000 |
| 5 | sol | 2.09% | $4,399,174,509 | $128.9400 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key
[coingecko-api-key-docs]: https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key

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
