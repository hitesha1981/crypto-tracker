# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-16 11:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 30.14% | $77,944,302 | $0.4859 |
| 2 | hash | 14.07% | $78,220 | $0.0310 |
| 3 | apepe | 5.11% | $17,397,127 | $0.0000 |
| 4 | xdc | 4.26% | $44,223,508 | $0.0492 |
| 5 | cc | 3.27% | $10,864,261 | $0.0737 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | merl | -16.19% | $37,603,438 | $0.4012 |
| 2 | beat | -15.92% | $85,595,602 | $2.3800 |
| 3 | mwc | -10.84% | $144,958 | $22.9200 |
| 4 | night | -10.83% | $1,301,571,530 | $0.0558 |
| 5 | aster | -10.81% | $646,181,951 | $0.8130 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $88,275,914,936 | $0.9999 |
| 2 | btc | -2.95% | $53,402,545,126 | $87,094.0000 |
| 3 | eth | -6.26% | $30,070,890,161 | $2,953.1800 |
| 4 | usdc | 0.02% | $13,324,455,554 | $1.0000 |
| 5 | sol | -3.20% | $5,930,169,359 | $128.1600 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key
[coingecko-api-key-docs]: https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key

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
