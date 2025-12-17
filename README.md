# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-17 06:04 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zora | 13.87% | $42,923,465 | $0.0524 |
| 2 | morpho | 7.66% | $23,021,693 | $1.1800 |
| 3 | zbcn | 6.77% | $9,088,833 | $0.0026 |
| 4 | kag | 6.42% | $1,068,414 | $66.4600 |
| 5 | tel | 5.44% | $2,620,084 | $0.0042 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -31.13% | $116,530,267 | $1.9600 |
| 2 | pippin | -13.14% | $111,362,925 | $0.3903 |
| 3 | uds | -12.35% | $842,874 | $2.3100 |
| 4 | stable | -7.15% | $167,136,161 | $0.0140 |
| 5 | aster | -7.13% | $334,685,758 | $0.7701 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $69,905,621,602 | $0.9998 |
| 2 | btc | 0.90% | $45,475,265,218 | $86,808.0000 |
| 3 | eth | 0.23% | $21,615,897,184 | $2,937.6000 |
| 4 | usdc | -0.01% | $10,811,840,829 | $0.9998 |
| 5 | sol | 1.01% | $4,315,395,057 | $127.7200 |


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
