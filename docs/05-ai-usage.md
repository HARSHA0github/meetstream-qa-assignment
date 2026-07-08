# AI Usage & Verification Log

In alignment with MeetStream AI's engineering principles, I utilized generative AI tools to accelerate my workflows, treat documentation as code, and brainstorm edge cases. Below is an honest breakdown of how these tools were integrated and verified.

## 1. Tools Used
* **Large Language Models (LLMs):** Used for initial structural scaffolding of the markdown documentation and generating the boilerplate for Python's Page Object Model setup.

## 2. Practical Contributions
* **Test Case Expansion:** I used AI to expand my initial core test list, prompting it to think of obscure edge cases. It helped surface the concurrent registration race condition (TC-14).
* **Boilerplate Reduction:** Instead of manually typing out repetitive element definitions across the three Page Objects, I provided the DOM patterns for SauceDemo and let the AI write the properties.

## 3. Verification & Course Correction
AI-generated output can look completely correct while being subtly broken or fragile. I applied a strict verification protocol:
* **Static Analysis:** All Python code was passed through local syntax and linter checks to ensure imports and type hints were perfectly accurate.
* **DOM Pattern Audits:** I manually checked the real SauceDemo site HTML to guarantee the selectors used were realistic and resilient.

### Concrete Example of Modifying an AI Suggestion
* **The AI's original suggestion:** For the automated cart flow, the AI initially generated code that relied heavily on generic CSS class selectors like `.btn_primary.btn_inventory` and suggested using `time.sleep(2)` to handle the sidebar animation during logout.
* **My modification:** I completely rejected that approach. Relying on visual class names makes UI tests incredibly brittle if the frontend team updates the styling. I refactored the locators to use robust, explicit attributes like `[data-test='username']` and `[data-test='add-to-cart-sauce-labs-backpack']`. Additionally, I removed the hard-coded sleeps and replaced them with Playwright's native locator actions, which automatically wait for elements to be visible and actionable before interacting.