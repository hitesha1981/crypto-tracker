# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-30 01:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 13.63% | $33,765,924 | $1.7700 |
| 2 | sent | 12.80% | $103,558,112 | $0.0183 |
| 3 | vvv | 6.18% | $10,015,074 | $6.1300 |
| 4 | wemix | 5.64% | $1,162,711 | $0.2600 |
| 5 | shfl | 5.02% | $1,207,814 | $0.3031 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | -21.71% | $13,700 | $0.0108 |
| 2 | kau | -9.05% | $31,153 | $143.4100 |
| 3 | kite | -6.59% | $71,331,369 | $0.1606 |
| 4 | kas | -6.55% | $26,945,881 | $0.0326 |
| 5 | bch | -5.97% | $416,721,585 | $454.3800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $41,763,452,708 | $0.9991 |
| 2 | btc | 0.24% | $27,456,661,692 | $66,685.0000 |
| 3 | eth | 0.43% | $10,729,546,297 | $2,011.4900 |
| 4 | usdc | 0.00% | $5,000,554,083 | $0.9998 |
| 5 | sol | 0.36% | $2,275,259,987 | $82.6100 |


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
