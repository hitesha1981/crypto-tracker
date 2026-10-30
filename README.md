# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-30 03:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hype | 18.07% | $3,501,201,443 | $92.4600 |
| 2 | kntq | 11.62% | $15,634,801 | $0.4912 |
| 3 | rune | 10.33% | $65,686,687 | $0.6678 |
| 4 | cap | 9.88% | $21,946,235 | $0.0798 |
| 5 | trx | 6.56% | $1,674,688,079 | $0.3521 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -22.84% | $148,404,255 | $0.0495 |
| 2 | cvx | -18.18% | $20,673,021 | $1.7900 |
| 3 | btw | -17.34% | $9,945,505 | $1.4600 |
| 4 | ake | -16.32% | $8,247,089 | $0.0185 |
| 5 | useless | -16.18% | $27,179,675 | $0.1276 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $89,656,783,329 | $0.9984 |
| 2 | btc | -2.30% | $49,870,201,487 | $77,960.0000 |
| 3 | eth | -3.25% | $22,664,901,530 | $2,230.3300 |
| 4 | usdc | -0.03% | $22,164,517,270 | $0.9991 |
| 5 | sol | -2.68% | $5,475,295,580 | $96.9200 |


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
