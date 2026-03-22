# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-22 01:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 15.47% | $35,961,227 | $25.4900 |
| 2 | dexe | 6.29% | $21,265,926 | $6.4800 |
| 3 | qubic | 6.07% | $1,884,079 | $0.0000 |
| 4 | akt | 5.91% | $47,927,746 | $0.5814 |
| 5 | 9bit | 5.53% | $3,652,909 | $0.0241 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | uds | -10.04% | $209,460 | $1.5200 |
| 2 | bard | -8.91% | $42,361,489 | $0.4986 |
| 3 | fartcoin | -8.46% | $31,570,190 | $0.1827 |
| 4 | zbcn | -7.66% | $7,800,522 | $0.0025 |
| 5 | hnt | -7.30% | $2,957,460 | $1.1900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $41,363,191,008 | $0.9999 |
| 2 | btc | -2.29% | $26,130,707,183 | $69,003.0000 |
| 3 | eth | -2.98% | $10,183,518,362 | $2,090.1000 |
| 4 | usdc | 0.00% | $3,941,015,763 | $0.9999 |
| 5 | sol | -2.92% | $2,065,426,209 | $87.4100 |


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
