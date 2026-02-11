# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-11 01:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 37.45% | $56,623,695 | $0.3912 |
| 2 | river | 32.22% | $85,728,960 | $17.9100 |
| 3 | zro | 17.00% | $409,717,660 | $2.2000 |
| 4 | hash | 10.35% | $12,390 | $0.0202 |
| 5 | mon | 7.39% | $162,328,775 | $0.0195 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hnt | -10.95% | $6,248,081 | $0.8171 |
| 2 | uds | -10.69% | $365,885 | $1.9700 |
| 3 | myx | -10.69% | $20,029,569 | $5.5300 |
| 4 | dcr | -9.73% | $5,811,788 | $24.0000 |
| 5 | 2z | -9.52% | $20,697,905 | $0.0755 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $74,032,809,540 | $0.9995 |
| 2 | btc | -1.96% | $43,762,156,326 | $69,002.0000 |
| 3 | eth | -4.45% | $23,868,320,780 | $2,024.5800 |
| 4 | usdc | 0.00% | $5,498,645,288 | $0.9999 |
| 5 | sol | -4.21% | $3,599,529,591 | $83.5700 |


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
