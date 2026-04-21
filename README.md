# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-21 01:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 94.76% | $273,430,168 | $1.0310 |
| 2 | chz | 12.53% | $187,657,131 | $0.0474 |
| 3 | shfl | 12.52% | $861,490 | $0.3250 |
| 4 | bat | 11.07% | $29,690,290 | $0.1097 |
| 5 | 币安人生 | 10.43% | $112,577,970 | $0.4665 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | genius | -15.37% | $17,595,747 | $0.5557 |
| 2 | koge | -12.85% | $19,065,961 | $41.8500 |
| 3 | pieverse | -10.52% | $646,779,770 | $0.9637 |
| 4 | skyai | -9.76% | $108,565,914 | $0.1607 |
| 5 | cfg | -6.34% | $60,507,405 | $0.2565 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $71,193,726,855 | $1.0000 |
| 2 | btc | 1.73% | $41,344,930,737 | $75,912.0000 |
| 3 | eth | 1.25% | $19,717,109,239 | $2,315.7800 |
| 4 | usdc | 0.01% | $17,422,142,778 | $1.0000 |
| 5 | sol | 1.15% | $3,455,896,487 | $85.4700 |


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
