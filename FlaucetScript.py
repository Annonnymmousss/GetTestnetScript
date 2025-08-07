import asyncio
from datetime import datetime, timedelta
from playwright.async_api import async_playwright

# CONFIGURATION
FAUCET_URL = "https://cloud.google.com/application/web3/faucet/ethereum/sepolia"
WALLET_ADDRESS = "0x9A5A1F42f6a790A0423C19B7FC1Dd5F4Fef4A529"
TRIGGER_TIME = "00:54"

async def claim_sepolia_eth():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(FAUCET_URL)

        print("🌐 Faucet page opened")

        # Wait for input field (Try a more flexible selector)
        try:
            await page.wait_for_selector("input[placeholder*='Wallet address']", timeout=15000)
        except Exception as e:
            print("❌ Wallet input field not found, retrying with broader selector...")
            await page.wait_for_selector("input", timeout=10000)

        # Fill the wallet address
        await page.fill("input", WALLET_ADDRESS)
        print("✅ Wallet address filled")

        # Click the receive button
        await page.wait_for_selector("button:has-text('Receive 0.05 Sepolia ETH')", timeout=10000)
        await page.click("button:has-text('Receive 0.05 Sepolia ETH')")
        print("🚀 Receive button clicked")

        # Wait for any confirmation or page processing
        await page.wait_for_timeout(5000)
        await browser.close()

async def wait_until_trigger_time():
    while True:
        now = datetime.now()
        target_time = datetime.strptime(TRIGGER_TIME, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        if now > target_time:
            target_time += timedelta(days=1)

        wait_seconds = (target_time - now).total_seconds()
        print(f"⏳ Waiting for {int(wait_seconds)} seconds until next claim at {target_time.time()}")
        await asyncio.sleep(wait_seconds)

        try:
            await claim_sepolia_eth()
        except Exception as e:
            print("❌ Failed to claim faucet:", e)

        print("✅ Claim done. Sleeping for 24 hours.")
        await asyncio.sleep(24 * 60 * 60)

if __name__ == "__main__":
    asyncio.run(wait_until_trigger_time())
