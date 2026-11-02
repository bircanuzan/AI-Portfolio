"""OPTIONAL browser test on synthetic inline HTML, NOT against any real employer app.
Requires: pip install playwright; python -m playwright install chromium.
"""
from playwright.sync_api import sync_playwright

HTML = """
<html><body>
<form id="case-form"><label>Campaign ID <input id="id" required></label>
<button type="submit">Create case</button></form>
<p id="status" role="status"></p>
<script>
document.querySelector("form").addEventListener("submit", e => {
  e.preventDefault();
  document.querySelector("#status").textContent =
    document.querySelector("#id").value.trim() ? "Draft created" : "Missing ID";
});
</script></body></html>
"""

def run():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        try:
            page=browser.new_page()
            page.set_content(HTML)
            page.get_by_label("Campaign ID").fill("SYN-001")
            page.get_by_role("button",name="Create case").click()
            assert page.get_by_role("status").inner_text()=="Draft created"
            print("Optional synthetic browser smoke passed")
        finally:
            browser.close()

if __name__=="__main__":run()
