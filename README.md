# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-14 04:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 371.88% | $594,172,109 | $0.0124 |
| 2 | pearl | 13.59% | $19,492,960 | $1.5200 |
| 3 | ozo | 9.45% | $394,852 | $0.2360 |
| 4 | inj | 9.37% | $161,304,656 | $7.9400 |
| 5 | night | 6.87% | $25,682,436 | $0.0463 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -12.90% | $9,873,641 | $0.7299 |
| 2 | bat | -11.68% | $18,644,880 | $0.1043 |
| 3 | drv | -10.64% | $8,203,781 | $0.2679 |
| 4 | tia | -9.95% | $42,364,780 | $0.3704 |
| 5 | useless | -9.49% | $14,602,114 | $0.1158 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $58,413,872,700 | $0.9992 |
| 2 | btc | -2.90% | $39,048,123,031 | $66,833.0000 |
| 3 | usdc | 0.00% | $16,452,872,956 | $0.9996 |
| 4 | eth | -2.02% | $13,684,253,425 | $1,892.5600 |
| 5 | sol | -3.84% | $3,557,124,223 | $75.4000 |


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
