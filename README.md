# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-03 02:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 28.02% | $23,456,738 | $1.6300 |
| 2 | lab | 23.25% | $41,427,752 | $11.2200 |
| 3 | fartcoin | 20.76% | $35,350,303 | $0.1680 |
| 4 | wld | 18.02% | $363,088,337 | $0.4334 |
| 5 | re | 17.44% | $299,983,785 | $0.7070 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | -69.70% | $47,445,652 | $0.4499 |
| 2 | kaito | -9.93% | $30,369,816 | $0.5763 |
| 3 | tac | -7.06% | $17,587,245 | $0.0352 |
| 4 | hash | -5.73% | $1,843 | $0.0085 |
| 5 | shfl | -5.70% | $790,832 | $0.2613 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $59,867,957,873 | $0.9987 |
| 2 | btc | 2.50% | $39,217,950,702 | $61,562.0000 |
| 3 | eth | 5.90% | $13,713,032,378 | $1,711.1800 |
| 4 | usdc | 0.01% | $13,106,857,352 | $0.9997 |
| 5 | sol | 4.52% | $3,763,489,688 | $81.4300 |


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
