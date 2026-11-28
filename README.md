# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-28 05:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 30.81% | $18,062,251 | $1.2600 |
| 2 | sent | 8.62% | $18,240,237 | $0.0247 |
| 3 | soso | 7.84% | $5,244,914 | $0.3344 |
| 4 | sky | 7.76% | $35,422,866 | $0.0504 |
| 5 | apepe | 4.31% | $18,516,334 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | wlfi | -56.05% | $201,230,898 | $0.0184 |
| 2 | pearl | -14.44% | $16,676,588 | $1.6100 |
| 3 | trump | -12.21% | $76,844,547 | $0.7723 |
| 4 | xmr | -8.53% | $140,063,206 | $420.3800 |
| 5 | met | -8.09% | $7,993,259 | $0.1908 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $41,085,245,272 | $0.9993 |
| 2 | btc | -3.27% | $26,418,466,717 | $59,684.0000 |
| 3 | usdc | 0.03% | $12,320,082,281 | $0.9998 |
| 4 | eth | -5.06% | $9,669,533,471 | $1,653.7700 |
| 5 | sol | -2.68% | $2,362,701,351 | $71.1600 |


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
