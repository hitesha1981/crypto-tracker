# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-28 02:54 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | shfl | 74.97% | $6,730,488 | $0.6911 |
| 2 | qnt | 60.81% | $1,432,219,418 | $271.5300 |
| 3 | grt | 25.27% | $111,939,073 | $0.0341 |
| 4 | btw | 20.86% | $27,345,843 | $1.2500 |
| 5 | pump | 17.56% | $355,767,167 | $0.0052 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -16.53% | $57,779,907 | $0.0292 |
| 2 | ai | -13.28% | $13,517,423 | $0.2103 |
| 3 | ake | -13.26% | $10,770,907 | $0.0298 |
| 4 | pons | -12.75% | $40,656,980 | $0.5556 |
| 5 | cashcat | -11.86% | $10,759,669 | $0.1624 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $47,687,238,764 | $0.9998 |
| 2 | btc | -1.21% | $25,357,247,632 | $83,416.0000 |
| 3 | sand | 2.16% | $21,621,481,532 | $0.0454 |
| 4 | usdc | -0.00% | $10,991,828,708 | $0.9998 |
| 5 | eth | -1.74% | $10,159,415,939 | $2,650.9300 |


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
