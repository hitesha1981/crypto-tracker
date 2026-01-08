# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-08 01:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | 4.89% | $27,240,910 | $5.1000 |
| 2 | glm | 4.83% | $18,905,553 | $0.2717 |
| 3 | xcn | 3.23% | $100,450,538 | $0.0097 |
| 4 | cc | 2.77% | $24,034,111 | $0.1391 |
| 5 | leo | 2.72% | $683,885 | $9.1900 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -15.09% | $34,536,963 | $0.2844 |
| 2 | river | -11.66% | $39,953,454 | $16.4800 |
| 3 | xpl | -11.38% | $160,234,950 | $0.1790 |
| 4 | jasmy | -10.44% | $102,639,617 | $0.0085 |
| 5 | pump | -9.40% | $122,878,907 | $0.0024 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $74,286,635,493 | $0.9991 |
| 2 | btc | -1.61% | $45,800,723,102 | $91,271.0000 |
| 3 | eth | -2.97% | $24,149,395,107 | $3,168.6100 |
| 4 | usdc | -0.00% | $12,445,715,183 | $0.9998 |
| 5 | sol | -2.50% | $4,174,660,717 | $136.7500 |


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
