# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-25 02:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | o | 30.13% | $42,741,460 | $0.6990 |
| 2 | aave | 13.97% | $399,806,823 | $81.9900 |
| 3 | gwei | 12.88% | $4,209,719 | $0.1328 |
| 4 | lab | 12.45% | $61,969,841 | $16.1200 |
| 5 | lit | 10.12% | $56,099,466 | $1.6700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | -70.10% | $18,830,756 | $0.8435 |
| 2 | h | -46.63% | $50,912,478 | $0.0596 |
| 3 | beat | -23.44% | $65,385,289 | $1.7300 |
| 4 | skyai | -21.39% | $23,603,496 | $0.2560 |
| 5 | pump | -10.28% | $58,753,516 | $0.0013 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $62,399,985,968 | $0.9985 |
| 2 | btc | -2.87% | $43,084,876,868 | $60,809.0000 |
| 3 | usdc | 0.00% | $15,146,717,494 | $0.9998 |
| 4 | eth | -2.86% | $13,246,343,374 | $1,616.5400 |
| 5 | sol | -2.66% | $3,209,674,047 | $67.7400 |


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
