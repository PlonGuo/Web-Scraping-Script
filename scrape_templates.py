import json
import csv
import time
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup

class TemplateScraper:
    def __init__(self):
        self.base_url = 'https://www.fillout.com/templates'
        self.all_results = []

    def scrape_all_templates(self):
        """使用 Playwright 爬取所有模板数据"""
        with sync_playwright() as p:
            # 启动浏览器
            browser = p.chromium.launch(headless=True)  # headless=False 可以看到浏览器操作过程
            page = browser.new_page()
            
            try:
                print("正在访问页面...")
                page.goto(self.base_url)
                
                # 等待页面初始加载
                page.wait_for_selector('a[href^="/templates/"]')
                
                # 查找并点击 "Show more" 按钮
                print("查找 'Show more' 按钮...")
                show_more_button = page.get_by_text("Show 414 more")
                
                if show_more_button:
                    print("点击 'Show more' 按钮加载更多内容...")
                    show_more_button.click()
                    
                    # 等待新内容加载完成
                    print("等待所有内容加载...")
                    
                    # 等待页面完全加载（等待一个在加载完成后才会出现的元素）
                    try:
                        # 使用更长的超时时间，确保所有内容都加载完成
                        page.wait_for_load_state('networkidle', timeout=30000)
                        # 额外等待一下确保 JavaScript 渲染完成
                        time.sleep(3)
                    except PlaywrightTimeoutError:
                        print("等待超时，但继续处理已加载的内容...")
                
                # 获取页面内容
                print("正在解析页面内容...")
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')
                
                # 解析所有模板
                templates = soup.select('a[href^="/templates/"]')
                total_templates = len(templates)
                print(f"找到 {total_templates} 个模板")
                
                if total_templates < 400:
                    print("警告：找到的模板数量少于预期（应该有400多个）")
                
                for idx, template in enumerate(templates, 1):
                    try:
                        title_element = template.find('h6')
                        description_element = template.find('p')
                        
                        # 只有同时存在标题和描述的才是有效的模板
                        if title_element and description_element:
                            title = title_element.text.strip()
                            description = description_element.text.strip()
                            link = f"{self.base_url}{template['href'].lstrip('/')}"
                            
                            template_data = {
                                'title': title,
                                'description': description,
                                'link': link
                            }
                            
                            # 避免重复
                            if not any(r['link'] == link for r in self.all_results):
                                self.all_results.append(template_data)
                                
                            # 打印进度
                            if idx % 50 == 0:
                                print(f"已处理 {idx}/{total_templates} 个模板...")
                            
                    except Exception as e:
                        print(f"解析模板时出错: {str(e)}")
                        continue
                
                print(f"成功解析了 {len(self.all_results)} 个有效模板")
                
            except Exception as e:
                print(f"爬取过程中出现错误: {str(e)}")
            finally:
                browser.close()

    def save_results(self):
        """保存结果到JSON和CSV文件"""
        if not self.all_results:
            print("没有数据可保存")
            return
            
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 保存为JSON
        json_filename = f'templates_data_{timestamp}.json'
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_results, f, ensure_ascii=False, indent=2)

        # 保存为CSV
        csv_filename = f'templates_data_{timestamp}.csv'
        with open(csv_filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'description', 'link'])
            writer.writeheader()
            writer.writerows(self.all_results)

        print(f"\n总共保存了 {len(self.all_results)} 个模板")
        print(f"数据已保存到:")
        print(f"- JSON文件: {json_filename}")
        print(f"- CSV文件: {csv_filename}")

def main():
    try:
        scraper = TemplateScraper()
        scraper.scrape_all_templates()
        scraper.save_results()
    except KeyboardInterrupt:
        print("\n检测到用户中断...")
        scraper.save_results()
    except Exception as e:
        print(f"发生错误: {str(e)}")
        scraper.save_results()

if __name__ == "__main__":
    main() 