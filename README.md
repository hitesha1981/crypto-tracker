# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-08 01:57 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 200.58% | $352,526,437 | $0.2733 |
| 2 | m | 12.65% | $8,753,863 | $1.8700 |
| 3 | zbcn | 10.71% | $10,492,912 | $0.0023 |
| 4 | egld | 9.02% | $20,553,896 | $4.9000 |
| 5 | beam | 6.81% | $14,545,525 | $0.0026 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | -17.64% | $33,133,825 | $0.0231 |
| 2 | qrl | -16.63% | $1,108,740 | $2.0900 |
| 3 | b | -10.14% | $7,309,439 | $0.1386 |
| 4 | whitewhale | -7.74% | $12,825,355 | $0.1327 |
| 5 | zk | -7.43% | $49,953,598 | $0.0218 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $111,730,745,680 | $0.9995 |
| 2 | btc | -1.56% | $66,152,423,009 | $69,373.0000 |
| 3 | eth | 1.48% | $39,800,589,811 | $2,093.8900 |
| 4 | usdc | -0.01% | $12,652,865,930 | $0.9998 |
| 5 | sol | 0.77% | $5,184,721,711 | $87.8500 |


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
