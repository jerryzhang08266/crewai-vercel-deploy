from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime

# 由于Vercel的限制，我们创建一个模拟的CrewAI功能
# 在实际部署中，用户可以替换为真正的CrewAI实现

app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')
CORS(app)

class MockAgent:
    """模拟CrewAI智能体"""
    def __init__(self, role, goal, backstory):
        self.role = role
        self.goal = goal
        self.backstory = backstory
    
    def execute_task(self, task_description):
        """模拟执行任务"""
        return f"[{self.role}] 正在执行任务: {task_description}"

class MockCrew:
    """模拟CrewAI团队"""
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
    
    def kickoff(self):
        """模拟启动团队协作"""
        results = []
        for i, task in enumerate(self.tasks):
            agent = self.agents[i % len(self.agents)]
            result = agent.execute_task(task)
            results.append({
                'agent': agent.role,
                'task': task,
                'result': result,
                'timestamp': datetime.now().isoformat()
            })
        return results

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/api/demo', methods=['POST'])
def demo_crew():
    """演示CrewAI功能的API端点"""
    try:
        data = request.get_json()
        
        # 创建模拟智能体
        researcher = MockAgent(
            role="研究员",
            goal="收集和分析信息",
            backstory="你是一个经验丰富的研究员，擅长收集和分析各种信息。"
        )
        
        writer = MockAgent(
            role="作家",
            goal="创作高质量的内容",
            backstory="你是一个专业的作家，能够将复杂的信息转化为易懂的内容。"
        )
        
        reviewer = MockAgent(
            role="审核员", 
            goal="确保内容质量",
            backstory="你是一个严格的审核员，确保所有内容都符合高质量标准。"
        )
        
        # 创建任务列表
        tasks = data.get('tasks', [
            "研究人工智能的最新发展趋势",
            "撰写一篇关于AI发展的文章",
            "审核文章内容并提出改进建议"
        ])
        
        # 创建团队并执行任务
        crew = MockCrew(
            agents=[researcher, writer, reviewer],
            tasks=tasks
        )
        
        results = crew.kickoff()
        
        return jsonify({
            'success': True,
            'message': 'CrewAI团队协作完成',
            'results': results
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents', methods=['GET'])
def get_agents():
    """获取可用的智能体列表"""
    agents = [
        {
            'id': 'researcher',
            'role': '研究员',
            'goal': '收集和分析信息',
            'backstory': '经验丰富的研究员，擅长收集和分析各种信息'
        },
        {
            'id': 'writer', 
            'role': '作家',
            'goal': '创作高质量的内容',
            'backstory': '专业的作家，能够将复杂的信息转化为易懂的内容'
        },
        {
            'id': 'reviewer',
            'role': '审核员',
            'goal': '确保内容质量', 
            'backstory': '严格的审核员，确保所有内容都符合高质量标准'
        },
        {
            'id': 'analyst',
            'role': '分析师',
            'goal': '深度分析数据和趋势',
            'backstory': '数据分析专家，能够从复杂数据中提取有价值的洞察'
        }
    ]
    
    return jsonify({
        'success': True,
        'agents': agents
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'healthy',
        'message': 'CrewAI Vercel部署服务正常运行',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

