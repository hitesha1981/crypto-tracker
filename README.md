# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-26 02:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | aero | 28.88% | $167,337,657 | $0.8908 |
| 2 | cashcat | 23.18% | $21,160,784 | $0.1975 |
| 3 | h | 21.44% | $8,959,652 | $0.0775 |
| 4 | sei | 17.53% | $210,171,263 | $0.0741 |
| 5 | sent | 17.14% | $13,956,352 | $0.0245 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | -12.92% | $17,575,675 | $0.0104 |
| 2 | hash | -11.63% | $3,161 | $0.0066 |
| 3 | stonk | -9.88% | $36,107,325 | $0.3120 |
| 4 | dbr | -6.82% | $7,481,668 | $0.0223 |
| 5 | trac | -5.64% | $5,299,735 | $0.3745 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $67,092,466,177 | $0.9998 |
| 2 | btc | -0.27% | $34,686,263,578 | $84,032.0000 |
| 3 | usdc | 0.01% | $18,898,097,030 | $0.9999 |
| 4 | eth | 0.58% | $13,818,378,820 | $2,691.7500 |
| 5 | xrp | 2.58% | $6,362,465,886 | $1.5700 |


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
