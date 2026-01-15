# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-15 01:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dash | 41.29% | $1,360,263,425 | $82.3600 |
| 2 | icp | 33.48% | $641,523,358 | $4.7700 |
| 3 | 币安人生 | 26.11% | $222,909,076 | $0.2586 |
| 4 | dcr | 17.08% | $25,507,938 | $22.4700 |
| 5 | h | 10.43% | $67,313,063 | $0.1830 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ip | -13.63% | $346,100,465 | $3.3800 |
| 2 | cc | -7.83% | $17,373,368 | $0.1344 |
| 3 | pepe | -7.07% | $1,029,662,060 | $0.0000 |
| 4 | fartcoin | -6.70% | $153,739,194 | $0.3904 |
| 5 | virtual | -5.87% | $136,772,076 | $1.0160 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.06% | $113,321,266,618 | $0.9999 |
| 2 | btc | 1.66% | $68,161,164,147 | $96,846.0000 |
| 3 | eth | 0.27% | $33,869,037,977 | $3,338.0000 |
| 4 | usdc | 0.01% | $21,238,738,924 | $0.9998 |
| 5 | sol | 0.75% | $6,632,005,481 | $146.2800 |


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
