# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-03 04:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | 11.09% | $15,279,835 | $0.0063 |
| 2 | pieverse | 10.21% | $9,177,733 | $1.1700 |
| 3 | rune | 10.21% | $18,641,352 | $0.5529 |
| 4 | cards | 6.24% | $7,547,953 | $0.2326 |
| 5 | cap | 3.86% | $21,536,207 | $0.0742 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | -26.47% | $14,930,934 | $0.0051 |
| 2 | beam | -20.06% | $49,557,989 | $0.0043 |
| 3 | pons | -13.86% | $21,176,883 | $0.2064 |
| 4 | kntq | -13.03% | $6,471,681 | $0.4373 |
| 5 | sn51 | -12.86% | $8,171,567 | $25.5900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $45,252,767,457 | $0.9986 |
| 2 | btc | -1.95% | $26,685,924,839 | $76,897.0000 |
| 3 | usdc | -0.03% | $13,763,677,210 | $0.9993 |
| 4 | eth | -2.01% | $9,985,906,706 | $2,254.2700 |
| 5 | sol | -3.04% | $2,571,945,576 | $92.2600 |


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
