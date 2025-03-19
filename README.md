# Fillout Templates Scraper

一个用于自动化抓取 [Fillout.com](https://www.fillout.com/templates) 模板数据的 Python 爬虫项目。该项目使用现代网页自动化技术，能够获取包括模板标题、描述和链接在内的完整数据集。

## 功能特点

- 🚀 自动化抓取 400+ 个表单模板
- 📊 支持多种数据导出格式（JSON/CSV）
- 🎯 精确定位和提取模板信息
- 🛡️ 内置错误处理和恢复机制
- 📝 详细的进度反馈
- 🔄 自动处理动态加载内容

## 技术栈

- **Python 3.x**
- **Playwright**: 现代网页自动化工具，用于处理动态内容
- **BeautifulSoup4**: HTML 解析
- **JSON/CSV**: 数据序列化和存储

## 环境要求

- Python 3.8+
- MacOS/Linux/Windows

## 安装步骤

1. **克隆项目**（如果适用）：
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **创建虚拟环境**：
   ```bash
   python3 -m venv venv
   ```

3. **激活虚拟环境**：
   ```bash
   # MacOS/Linux
   source venv/bin/activate
   
   # Windows
   .\venv\Scripts\activate
   ```

4. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

5. **安装 Playwright 浏览器**：
   ```bash
   playwright install chromium
   ```

## 使用方法

1. **确保虚拟环境已激活**：
   ```bash
   source venv/bin/activate  # MacOS/Linux
   ```

2. **运行爬虫**：
   ```bash
   python scrape_templates.py
   ```

3. **查看结果**：
   - 程序会生成两个文件：
     - `templates_data_[timestamp].json`: JSON 格式的完整数据
     - `templates_data_[timestamp].csv`: CSV 格式的表格数据（可用 Excel 打开）

## 数据格式

爬取的数据包含以下字段：
```json
{
    "title": "模板标题",
    "description": "模板描述",
    "link": "模板链接"
}
```

## 实现细节

1. **自动化流程**：
   - 访问目标网页
   - 等待页面加载
   - 自动点击 "Show more" 按钮
   - 等待所有内容加载完成
   - 解析和提取数据

2. **错误处理**：
   - 网络请求异常处理
   - 内容解析异常处理
   - 超时处理
   - 中断处理（支持 Ctrl+C）

3. **数据去重**：
   - 自动过滤重复模板
   - 确保数据完整性

## 注意事项

- 请遵守网站的爬虫政策
- 建议适度控制爬取频率
- 确保网络连接稳定
- 首次运行时需要下载 Chromium 浏览器

## 可能的改进

- [ ] 添加命令行参数支持
- [ ] 实现多线程爬取
- [ ] 添加数据验证机制
- [ ] 支持更多导出格式
- [ ] 添加日志记录功能
- [ ] 实现断点续爬功能

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

MIT License

## 作者

[Your Name]

## 更新日志

- 2024-02-xx: 初始版本发布
  - 实现基础爬虫功能
  - 支持 JSON/CSV 导出
  - 添加错误处理机制

