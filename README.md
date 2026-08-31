# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-31 02:44 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | 173.41% | $331,981,916 | $0.0327 |
| 2 | hnt | 56.07% | $216,454,556 | $0.7167 |
| 3 | 牛来 | 24.95% | $108,562,985 | $0.1100 |
| 4 | cys | 10.43% | $23,583,442 | $0.8396 |
| 5 | mnt | 7.43% | $39,364,111 | $0.5559 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cards | -20.44% | $6,719,172 | $0.1970 |
| 2 | prom | -18.63% | $94,883,547 | $6.3900 |
| 3 | pump | -13.42% | $180,647,438 | $0.0044 |
| 4 | ansem | -12.31% | $10,316,417 | $0.3083 |
| 5 | trump | -11.49% | $333,133,660 | $2.3500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $40,367,615,812 | $0.9998 |
| 2 | btc | -0.49% | $20,815,559,898 | $77,726.0000 |
| 3 | eth | -1.75% | $11,980,608,072 | $2,412.9800 |
| 4 | usdc | -0.02% | $9,924,084,964 | $0.9998 |
| 5 | sol | -3.28% | $3,113,273,645 | $101.9100 |


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
