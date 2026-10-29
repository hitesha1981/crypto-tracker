# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-29 03:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | 20.81% | $152,266,974 | $0.0645 |
| 2 | apepe | 13.90% | $29,571,594 | $0.0000 |
| 3 | pearl | 4.84% | $11,990,804 | $1.7400 |
| 4 | strcx | 4.48% | $66,229 | $109.4800 |
| 5 | awe | 4.48% | $4,328,742 | $0.0681 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grass | -14.50% | $24,750,954 | $0.6457 |
| 2 | jasmy | -11.11% | $18,454,864 | $0.0038 |
| 3 | rail | -9.02% | $250,251 | $2.2400 |
| 4 | stx | -8.78% | $19,544,094 | $0.2779 |
| 5 | vvv | -8.59% | $37,153,538 | $23.1200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $46,287,735,073 | $0.9990 |
| 2 | btc | -1.60% | $26,479,385,927 | $79,796.0000 |
| 3 | usdc | 0.01% | $13,195,024,466 | $0.9995 |
| 4 | eth | -2.41% | $10,433,285,880 | $2,305.7600 |
| 5 | sol | -2.50% | $2,825,498,073 | $99.5900 |


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
