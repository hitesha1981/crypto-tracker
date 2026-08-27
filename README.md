# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-27 06:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | up | 69.08% | $3,191,974 | $0.3361 |
| 2 | kag | 40.66% | $182,903 | $68.8300 |
| 3 | npc | 28.43% | $9,407,709 | $0.0164 |
| 4 | ansem | 26.91% | $26,604,796 | $0.3693 |
| 5 | drv | 20.62% | $35,671,002 | $0.1767 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pol | -13.66% | $115,879,179 | $0.1048 |
| 2 | pyth | -11.79% | $216,350,273 | $0.0467 |
| 3 | h | -9.34% | $3,869,232 | $0.0722 |
| 4 | fluid | -9.21% | $13,156,758 | $1.3700 |
| 5 | ake | -8.99% | $20,331,367 | $0.0079 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $51,463,849,721 | $0.9999 |
| 2 | btc | -0.34% | $27,297,969,868 | $78,655.0000 |
| 3 | usdc | 0.00% | $15,319,209,962 | $0.9999 |
| 4 | eth | 1.15% | $12,280,756,701 | $2,485.2800 |
| 5 | sol | 4.38% | $4,012,538,921 | $101.0400 |


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
