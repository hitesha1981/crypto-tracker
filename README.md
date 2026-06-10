# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-10 02:43 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 105.85% | $43,438,973 | $0.1212 |
| 2 | h | 35.12% | $169,087,979 | $0.1671 |
| 3 | sent | 19.80% | $95,640,506 | $0.0171 |
| 4 | velvet | 18.50% | $57,184,571 | $0.3747 |
| 5 | ub | 16.80% | $12,278,977 | $0.1378 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -25.83% | $44,097,345 | $0.8779 |
| 2 | lab | -25.58% | $23,740,547 | $9.0300 |
| 3 | skyai | -24.58% | $41,304,776 | $0.1743 |
| 4 | dexe | -11.26% | $21,788,713 | $19.4100 |
| 5 | hype | -10.04% | $1,026,652,113 | $55.8400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $58,766,261,889 | $0.9993 |
| 2 | btc | -2.03% | $39,191,011,975 | $61,330.0000 |
| 3 | eth | -2.15% | $14,143,658,546 | $1,624.2500 |
| 4 | usdc | 0.02% | $13,522,266,039 | $0.9998 |
| 5 | sol | -1.96% | $2,889,703,889 | $64.3500 |


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
