#!/usr/bin/env python3
"""
CrewAI Vercel 一键部署链接生成器
"""

def generate_deploy_link(github_username, repo_name="crewai-vercel-deploy"):
    """
    生成Vercel一键部署链接
    
    Args:
        github_username (str): GitHub用户名
        repo_name (str): 仓库名称，默认为 "crewai-vercel-deploy"
    
    Returns:
        str: Vercel一键部署链接
    """
    base_url = "https://vercel.com/new/clone"
    repo_url = f"https://github.com/{github_username}/{repo_name}"
    deploy_link = f"{base_url}?repository-url={repo_url}"
    
    return deploy_link

def generate_deploy_button(github_username, repo_name="crewai-vercel-deploy"):
    """
    生成Vercel部署按钮的Markdown代码
    
    Args:
        github_username (str): GitHub用户名
        repo_name (str): 仓库名称
    
    Returns:
        str: Markdown格式的部署按钮
    """
    deploy_link = generate_deploy_link(github_username, repo_name)
    button_markdown = f"[![Deploy with Vercel](https://vercel.com/button)]({deploy_link})"
    
    return button_markdown

def main():
    """主函数"""
    print("🚀 CrewAI Vercel 一键部署链接生成器")
    print("=" * 50)
    
    # 获取用户输入
    github_username = input("请输入您的GitHub用户名: ").strip()
    
    if not github_username:
        print("❌ GitHub用户名不能为空！")
        return
    
    repo_name = input("请输入仓库名称 (默认: crewai-vercel-deploy): ").strip()
    if not repo_name:
        repo_name = "crewai-vercel-deploy"
    
    # 生成链接
    deploy_link = generate_deploy_link(github_username, repo_name)
    button_markdown = generate_deploy_button(github_username, repo_name)
    
    # 显示结果
    print("\n✅ 生成成功！")
    print("=" * 50)
    print(f"📋 一键部署链接:")
    print(f"   {deploy_link}")
    print(f"\n📋 Markdown按钮代码:")
    print(f"   {button_markdown}")
    print(f"\n📋 HTML按钮代码:")
    print(f'   <a href="{deploy_link}" target="_blank">')
    print(f'     <img src="https://vercel.com/button" alt="Deploy with Vercel"/>')
    print(f'   </a>')
    
    print("\n📝 使用说明:")
    print("1. 将项目文件上传到您的GitHub仓库")
    print("2. 点击上面的部署链接")
    print("3. 在Vercel中授权并部署")
    print("4. 等待部署完成，获得您的应用URL")
    
    print("\n🎉 祝您部署成功！")

if __name__ == "__main__":
    main()

