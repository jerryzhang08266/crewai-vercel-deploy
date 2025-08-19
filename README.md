# CrewAI Vercel 一键部署

🚀 **一键部署CrewAI到Vercel平台**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/crewai-vercel-deploy)

## 📋 项目简介

这是一个可以一键部署到Vercel的CrewAI项目模板。CrewAI是一个强大的Python框架，用于创建和协调多个自主AI智能体，让它们像真实团队一样协作完成复杂任务。

## ✨ 功能特性

- 🤖 **多智能体协作**: 不同角色的AI智能体协同工作
- 🎭 **角色扮演**: 每个智能体都有明确的角色定位
- ⚡ **快速部署**: 一键部署到Vercel，无需复杂配置
- 🌐 **Web界面**: 友好的Web界面，支持移动端
- 🔧 **易于扩展**: 可以轻松添加新的智能体和任务

## 🚀 一键部署

### 方法一：使用Vercel按钮（推荐）

1. 点击上方的 "Deploy with Vercel" 按钮
2. 登录您的Vercel账户
3. 选择从GitHub导入项目
4. 等待部署完成
5. 访问生成的URL即可使用

### 方法二：手动部署

1. **Fork此仓库**
   ```bash
   # 或者克隆到本地
   git clone https://github.com/your-username/crewai-vercel-deploy.git
   cd crewai-vercel-deploy
   ```

2. **推送到您的GitHub仓库**
   ```bash
   git remote set-url origin https://github.com/your-username/crewai-vercel-deploy.git
   git push -u origin main
   ```

3. **在Vercel中导入项目**
   - 访问 [Vercel Dashboard](https://vercel.com/dashboard)
   - 点击 "New Project"
   - 选择您的GitHub仓库
   - 点击 "Deploy"

## 🛠️ 本地开发

### 环境要求

- Python 3.8+
- pip

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行项目

```bash
python api/index.py
```

访问 `http://localhost:5000` 查看项目。

## 📁 项目结构

```
crewai-vercel-deploy/
├── api/
│   └── index.py          # 主要的Flask应用
├── templates/
│   └── index.html        # 前端页面
├── static/               # 静态文件目录
├── requirements.txt      # Python依赖
├── vercel.json          # Vercel配置
└── README.md            # 项目说明
```

## 🔧 配置说明

### 环境变量

如果您需要使用真实的OpenAI API，请在Vercel项目设置中添加以下环境变量：

- `OPENAI_API_KEY`: 您的OpenAI API密钥

### 自定义智能体

您可以在 `api/index.py` 中修改智能体的配置：

```python
# 创建自定义智能体
custom_agent = MockAgent(
    role="您的角色",
    goal="您的目标", 
    backstory="您的背景故事"
)
```

## 🎯 使用示例

### API端点

- `GET /`: 主页面
- `GET /api/health`: 健康检查
- `GET /api/agents`: 获取智能体列表
- `POST /api/demo`: 运行CrewAI演示

### 示例请求

```bash
# 健康检查
curl https://your-app.vercel.app/api/health

# 获取智能体列表
curl https://your-app.vercel.app/api/agents

# 运行演示
curl -X POST https://your-app.vercel.app/api/demo \
  -H "Content-Type: application/json" \
  -d '{"tasks": ["研究AI趋势", "撰写报告", "审核内容"]}'
```

## 🔄 升级到真实CrewAI

当前版本使用模拟的CrewAI功能以确保在Vercel上的兼容性。要使用真实的CrewAI功能：

1. 替换 `MockAgent` 和 `MockCrew` 为真实的CrewAI类
2. 添加必要的API密钥配置
3. 根据需要调整超时设置

```python
from crewai import Agent, Task, Crew

# 真实的CrewAI实现
agent = Agent(
    role="研究员",
    goal="收集和分析信息",
    backstory="您是一个经验丰富的研究员...",
    verbose=True
)
```

## 🐛 故障排除

### 常见问题

1. **部署失败**: 检查 `requirements.txt` 中的依赖版本
2. **超时错误**: 调整 `vercel.json` 中的 `maxDuration` 设置
3. **API错误**: 确保环境变量正确配置

### 调试技巧

- 查看Vercel部署日志
- 使用 `vercel dev` 本地测试
- 检查浏览器控制台错误

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 支持

如果您遇到问题，请：

1. 查看[常见问题](#故障排除)
2. 提交[Issue](https://github.com/your-username/crewai-vercel-deploy/issues)
3. 参考[CrewAI官方文档](https://docs.crewai.com/)

---

⭐ 如果这个项目对您有帮助，请给个Star！

