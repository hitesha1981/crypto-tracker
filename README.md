# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.


<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-16 16:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 26.45% | $79,573,032 | $0.4690 |
| 2 | hash | 11.64% | $78,977 | $0.0306 |
| 3 | xdc | 6.59% | $44,104,661 | $0.0501 |
| 4 | apepe | 5.63% | $17,918,787 | $0.0000 |
| 5 | cc | 3.10% | $14,128,004 | $0.0736 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | merl | -15.36% | $41,296,318 | $0.4019 |
| 2 | tel | -11.32% | $5,791,299 | $0.0041 |
| 3 | night | -10.87% | $1,326,762,890 | $0.0564 |
| 4 | aster | -10.60% | $655,388,468 | $0.8189 |
| 5 | ultima | -10.36% | $14,450,187 | $5,474.0600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $87,407,342,507 | $0.9999 |
| 2 | btc | -3.27% | $53,081,768,629 | $86,916.0000 |
| 3 | eth | -6.70% | $29,838,748,900 | $2,945.5800 |
| 4 | usdc | 0.01% | $13,063,814,657 | $1.0000 |
| 5 | sol | -3.22% | $5,851,460,173 | $128.2100 |


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
