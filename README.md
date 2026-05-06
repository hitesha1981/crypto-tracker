# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-06 02:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 57.98% | $105,840,678 | $2.7200 |
| 2 | m | 28.94% | $20,738,879 | $3.4600 |
| 3 | skyai | 26.26% | $143,968,845 | $0.7899 |
| 4 | gwei | 24.84% | $14,218,472 | $0.1354 |
| 5 | riv | 23.62% | $1,940,382 | $0.0351 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | -9.81% | $56,780,885 | $0.6878 |
| 2 | crclon | -8.14% | $1,087,257 | $115.0000 |
| 3 | 币安人生 | -6.19% | $23,260,758 | $0.3691 |
| 4 | genius | -6.18% | $13,725,138 | $0.5153 |
| 5 | zbcn | -3.22% | $7,869,292 | $0.0033 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $69,950,652,688 | $0.9998 |
| 2 | btc | 1.03% | $42,644,095,369 | $81,260.0000 |
| 3 | eth | 0.05% | $16,819,060,327 | $2,369.1900 |
| 4 | usdc | -0.02% | $15,894,764,309 | $0.9998 |
| 5 | sol | 2.64% | $3,676,902,863 | $86.7000 |


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
