# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-24 07:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | 23.97% | $51,485 | $0.0075 |
| 2 | nvdab | 21.45% | $315,911,486 | $163.5200 |
| 3 | nvdax | 21.24% | $82,731,572 | $163.4000 |
| 4 | soxlb | 20.52% | $87,365,001 | $42.8300 |
| 5 | dbr | 12.78% | $3,938,874 | $0.0153 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | -13.50% | $80,955,817 | $3.1900 |
| 2 | drv | -9.16% | $10,337,999 | $0.3291 |
| 3 | syrup | -7.86% | $7,232,042 | $0.0805 |
| 4 | strcx | -7.22% | $249,361 | $97.7400 |
| 5 | rain | -7.15% | $7,871,732 | $0.0030 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $60,619,836,111 | $0.9991 |
| 2 | btc | -1.70% | $38,975,637,142 | $60,387.0000 |
| 3 | usdc | 0.02% | $16,897,165,137 | $0.9996 |
| 4 | eth | -1.25% | $15,089,319,043 | $1,698.6000 |
| 5 | sol | -0.63% | $3,694,648,529 | $71.5000 |


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
