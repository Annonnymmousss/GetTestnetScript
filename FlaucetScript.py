import asyncio
from datetime import datetime, timedelta
from playwright.async_api import async_playwright

# CONFIGURATION
FAUCET_URL = "..."
WALLET_ADDRESS = "0xYourSepoliaWalletAddress"  # Replace this with your real address
TRIGGER_TIME = "23:51"  # 11:51 PM, just after 11:50 PM limit

async def claim_sepolia_eth():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False shows the browser
        page = await browser.new_page()
        await page.goto(FAUCET_URL)
        
        print("🌐 Faucet page opened")

        # Wait until input field is ready
        await page.wait_for_selector("input[type='text']")

        # Fill the wallet address
        await page.fill("input[type='text']", WALLET_ADDRESS)
        print("✅ Wallet address filled")

        # Click the 'Receive' button (may vary slightly based on exact text)
        await page.click("button:has-text('Receive')")
        print("🚀 Receive button clicked")

        # Optional: Wait to see confirmation
        await page.wait_for_timeout(5000)
        await browser.close()

async def wait_until_trigger_time():
    while True:
        now = datetime.now()
        target_time = datetime.strptime(TRIGGER_TIME, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        if now > target_time:
            target_time += timedelta(days=1)  # Schedule for the next day if time passed

        wait_seconds = (target_time - now).total_seconds()
        print(f"⏳ Waiting for {int(wait_seconds)} seconds until next claim at {target_time.time()}")
        await asyncio.sleep(wait_seconds)

        try:
            await claim_sepolia_eth()
        except Exception as e:
            print("❌ Failed to claim faucet:", e)

        print("✅ Claim done. Sleeping for 24 hours.")
        await asyncio.sleep(24 * 60 * 60)  # Wait 24 hours for next claim

if __name__ == "__main__":
    asyncio.run(wait_until_trigger_time())
