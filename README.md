# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-14 01:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | vvv | 68.59% | $24,698,391 | $3.0700 |
| 2 | comp | 35.60% | $245,914,412 | $21.7700 |
| 3 | h | 35.08% | $139,852,925 | $0.2260 |
| 4 | tibbir | 29.37% | $9,082,128 | $0.1395 |
| 5 | tao | 18.58% | $143,934,054 | $183.5300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -14.87% | $22,088,746 | $18.1600 |
| 2 | myx | -10.04% | $19,176,129 | $2.8700 |
| 3 | lpt | -8.92% | $39,202,766 | $2.4700 |
| 4 | zro | -5.18% | $140,364,042 | $1.8300 |
| 5 | b | -3.55% | $3,803,941 | $0.1445 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $69,754,838,585 | $0.9997 |
| 2 | btc | 4.29% | $42,944,522,379 | $69,034.0000 |
| 3 | eth | 5.80% | $20,444,258,857 | $2,053.9000 |
| 4 | usdc | 0.02% | $12,266,281,029 | $1.0000 |
| 5 | sol | 8.29% | $3,920,284,928 | $85.0100 |


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
