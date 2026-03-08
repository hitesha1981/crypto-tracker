# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-08 01:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | akt | 21.60% | $50,314,087 | $0.4220 |
| 2 | kite | 10.73% | $203,261,132 | $0.2788 |
| 3 | 9bit | 9.55% | $5,169,300 | $0.0221 |
| 4 | okb | 7.16% | $74,441,157 | $103.2300 |
| 5 | kau | 5.51% | $18,559 | $180.5200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | om | -43.26% | $81,281 | $0.0380 |
| 2 | skr | -14.24% | $40,492,490 | $0.0240 |
| 3 | siren | -12.57% | $14,404,327 | $0.4091 |
| 4 | bard | -10.71% | $30,858,257 | $1.0890 |
| 5 | wif | -6.40% | $54,077,358 | $0.1765 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $38,692,718,647 | $1.0000 |
| 2 | btc | -1.36% | $24,266,199,723 | $67,281.0000 |
| 3 | eth | -0.39% | $9,793,588,760 | $1,970.2200 |
| 4 | usdc | -0.00% | $2,011,966,420 | $1.0000 |
| 5 | sol | -1.84% | $1,869,354,397 | $83.1400 |


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
