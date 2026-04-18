# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-18 01:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | om | 480.43% | $6,696 | $0.0673 |
| 2 | rave | 53.87% | $324,181,272 | $25.7400 |
| 3 | 币安人生 | 27.34% | $188,060,666 | $0.4372 |
| 4 | m | 17.12% | $24,851,012 | $4.4100 |
| 5 | skyai | 16.88% | $48,114,924 | $0.1869 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -55.44% | $96,707,311 | $0.7256 |
| 2 | ordi | -31.96% | $562,378,335 | $6.1900 |
| 3 | ip | -13.80% | $178,068,463 | $0.6027 |
| 4 | wld | -11.80% | $242,000,815 | $0.2811 |
| 5 | xpl | -7.91% | $120,522,154 | $0.1281 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $102,861,617,712 | $1.0000 |
| 2 | btc | 3.44% | $65,548,526,901 | $77,257.0000 |
| 3 | eth | 3.84% | $25,170,524,214 | $2,421.8900 |
| 4 | usdc | -0.00% | $21,396,383,917 | $0.9998 |
| 5 | sol | 0.73% | $5,508,695,672 | $88.8700 |


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
