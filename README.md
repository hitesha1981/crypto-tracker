# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-23 01:59 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | chip | 131.23% | $2,010,070,660 | $0.1342 |
| 2 | ub | 30.72% | $54,563,138 | $0.0597 |
| 3 | pieverse | 20.87% | $228,339,129 | $1.0360 |
| 4 | strk | 18.94% | $125,875,796 | $0.0461 |
| 5 | asteroid | 18.12% | $56,324,504 | $0.0004 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | -38.02% | $124,563,077 | $0.9047 |
| 2 | 币安人生 | -29.23% | $94,902,230 | $0.3365 |
| 3 | gwei | -10.39% | $13,517,424 | $0.1003 |
| 4 | hash | -9.73% | $30,610 | $0.0103 |
| 5 | sent | -5.36% | $18,024,738 | $0.0174 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $83,355,137,155 | $1.0000 |
| 2 | btc | 2.66% | $52,464,886,316 | $78,356.0000 |
| 3 | eth | 1.85% | $23,201,365,627 | $2,366.7200 |
| 4 | usdc | 0.00% | $18,556,891,253 | $0.9998 |
| 5 | sol | 0.16% | $4,422,536,082 | $86.4000 |


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
