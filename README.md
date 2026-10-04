# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-04 03:39 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | 34.29% | $15,806,922 | $0.0134 |
| 2 | strk | 21.07% | $159,646,031 | $0.0524 |
| 3 | zama | 15.88% | $20,804,128 | $0.0885 |
| 4 | pump | 15.83% | $345,300,811 | $0.0064 |
| 5 | zro | 15.75% | $237,362,968 | $2.0100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -33.43% | $28,758,083 | $0.9326 |
| 2 | br | -20.64% | $6,132,340 | $0.4986 |
| 3 | stonk | -15.76% | $13,350,708 | $0.1944 |
| 4 | sand | -6.87% | $373,166,342 | $0.0766 |
| 5 | cards | -6.41% | $8,183,109 | $0.2609 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $28,659,353,357 | $0.9999 |
| 2 | btc | 0.26% | $14,626,719,050 | $84,830.0000 |
| 3 | usdc | 0.01% | $6,351,510,490 | $1.0000 |
| 4 | eth | 0.53% | $4,897,183,731 | $2,693.7800 |
| 5 | sol | 1.41% | $1,602,938,666 | $120.8300 |


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
