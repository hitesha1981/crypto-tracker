# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-21 01:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | axs | 19.67% | $880,882,111 | $2.1300 |
| 2 | river | 15.14% | $65,523,714 | $35.3100 |
| 3 | ip | 14.12% | $141,418,512 | $2.6700 |
| 4 | cc | 10.95% | $26,960,135 | $0.1299 |
| 5 | hash | 6.93% | $94,256 | $0.0264 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xmr | -16.95% | $357,071,164 | $505.6100 |
| 2 | zbcn | -11.42% | $15,867,853 | $0.0029 |
| 3 | dcr | -10.42% | $5,982,338 | $21.2800 |
| 4 | khype | -9.76% | $17,855,527 | $21.5200 |
| 5 | hype | -9.50% | $332,848,726 | $21.3200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $105,126,059,155 | $0.9989 |
| 2 | btc | -3.89% | $62,283,396,784 | $88,938.0000 |
| 3 | eth | -6.83% | $34,778,473,685 | $2,962.5200 |
| 4 | usdc | 0.01% | $8,175,379,524 | $0.9998 |
| 5 | sol | -4.71% | $6,106,161,542 | $127.2400 |


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
