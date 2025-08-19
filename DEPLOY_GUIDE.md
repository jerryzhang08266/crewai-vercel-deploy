# 🚀 CrewAI Vercel 一键部署指南

## 📋 项目概述

这是一个完整的CrewAI项目，可以一键部署到Vercel平台。项目包含：

- ✅ 完整的CrewAI多智能体协作系统
- ✅ 美观的Web界面
- ✅ RESTful API接口
- ✅ Vercel部署配置
- ✅ 响应式设计，支持移动端

## 🎯 一键部署链接

### 方法一：直接部署（推荐）

点击下面的按钮即可一键部署：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/crewai-vercel-deploy)

> **注意**：您需要先将项目上传到您的GitHub仓库，然后替换上面链接中的 `your-username` 为您的GitHub用户名。

### 方法二：手动部署

1. **Fork或下载项目**
   - 下载项目文件到本地
   - 创建新的GitHub仓库
   - 上传所有文件到您的仓库

2. **连接Vercel**
   - 访问 [Vercel Dashboard](https://vercel.com/dashboard)
   - 点击 "New Project"
   - 选择您的GitHub仓库
   - 点击 "Deploy"

## 📁 项目文件结构

```
crewai-vercel-deploy/
├── api/
│   └── index.py          # Flask应用主文件
├── templates/
│   └── index.html        # 前端页面
├── static/               # 静态文件目录
├── requirements.txt      # Python依赖
├── vercel.json          # Vercel配置
├── .gitignore           # Git忽略文件
├── deploy.html          # 部署页面
├── README.md            # 项目说明
└── DEPLOY_GUIDE.md      # 部署指南（本文件）
```

## 🔧 配置说明

### 环境变量（可选）

如果您想使用真实的OpenAI API，可以在Vercel项目设置中添加：

- `OPENAI_API_KEY`: 您的OpenAI API密钥

### 自定义域名（可选）

部署完成后，您可以在Vercel控制台中：
1. 进入项目设置
2. 点击 "Domains"
3. 添加您的自定义域名

## 🎮 功能演示

### 主要功能

1. **智能体团队**：包含研究员、作家、审核员、分析师等角色
2. **任务协作**：输入任务列表，AI团队自动分工协作
3. **实时结果**：查看每个智能体的工作结果
4. **API接口**：提供RESTful API供其他应用调用

### API端点

- `GET /`: 主页面
- `GET /api/health`: 健康检查
- `GET /api/agents`: 获取智能体列表
- `POST /api/demo`: 运行CrewAI演示

### 使用示例

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

当前版本使用模拟的CrewAI功能以确保兼容性。要使用真实的CrewAI：

1. 在 `requirements.txt` 中取消注释真实的CrewAI依赖
2. 在 `api/index.py` 中替换 `MockAgent` 和 `MockCrew`
3. 添加OpenAI API密钥环境变量
4. 重新部署

## 🐛 故障排除

### 常见问题

1. **部署失败**
   - 检查所有文件是否正确上传
   - 确认 `vercel.json` 配置正确

2. **API错误**
   - 检查环境变量配置
   - 查看Vercel部署日志

3. **页面无法访问**
   - 等待部署完成（通常需要1-2分钟）
   - 检查域名配置

### 调试技巧

- 使用 `vercel dev` 本地测试
- 查看Vercel控制台的部署日志
- 检查浏览器开发者工具的网络请求

## 📞 技术支持

如果遇到问题：

1. 检查本指南的故障排除部分
2. 查看项目的 README.md 文件
3. 参考 [Vercel官方文档](https://vercel.com/docs)
4. 参考 [CrewAI官方文档](https://docs.crewai.com/)

## 🎉 部署成功后

部署成功后，您将获得：

- 一个公开的URL地址
- 完整的CrewAI Web应用
- 可用的API接口
- 自动的HTTPS证书
- 全球CDN加速

享受您的CrewAI智能体协作平台吧！🎊

