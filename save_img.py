from playwright.sync_api import sync_playwright, expect

def test_button_click():
    """测试点击HTML页面中的按钮"""
    with sync_playwright() as p:
        # 启动浏览器（无头模式适合CI环境）
        browser = p.chromium.launch(headless=True, downloads_path=".")  # 设置默认下载目录)
        context = browser.new_context(
            accept_downloads=True  # 必须启用
        )
        page = context.new_page()
        #page = browser.new_page()

        try:
            # 访问本地HTML文件
            print("🌐 正在打开页面...")
            page.goto("http://localhost:8000", wait_until="networkidle")

            # 方式1：通过ID定位并点击按钮
            page.wait_for_selector(".save-btn", state="visible")

                    # 重要：使用 expect_download() 监听下载
            with page.expect_download() as download_info:
                page.click(".save-btn")  # 触发下载的按钮

            download = download_info.value

            # 保存到指定路径（可选）
            download.save_as("./output.png")


            print("✅ 按钮已找到，正在点击...")

            # 验证点击结果（可选）
            # result = page.locator("#result")

            # 使用expect断言，Playwright会自动等待
            # expect(result).to_be_visible(timeout=3000)

            # 获取结果文本
            # result_text = result.text_content()
            # print(f"🎉 测试成功: {result_text}")

        finally:
            browser.close()

if __name__ == "__main__":
    test_button_click()
