<template>
  <div class="page-container w-full min-h-full bg-[#fffefe] px-3 lg:px-[24px] pt-3 lg:pt-[16px] pb-4 lg:pb-[24px] text-[#1f2937]">
    <div class="min-h-screen">
      <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">
        <main class="lg:flex-1">
        <div class="text-[11px] lg:text-[12px] text-[#94a3b8] mb-3 lg:mb-[16px]">首页 <span class="mx-2 lg:mx-[8px]">|</span> 文章 <span class="mx-2 lg:mx-[8px]">|</span> 深入理解 Agent</div>

        <div class="inline-flex items-center px-2 lg:px-[10px] py-1 lg:py-[4px] rounded-full bg-[#eff6ff] text-[#2563eb] text-[11px] lg:text-[12px] font-semibold mb-2 lg:mb-[12px]">技术文章</div>
        <h1 class="text-lg lg:text-[26px] leading-[1.2] font-extrabold tracking-[-0.02em] text-[#0f172a]">深入理解 Agent：从原理到实践</h1>
        <p class="mt-2 lg:mt-[8px] text-xs lg:text-[13px] leading-[1.75] text-[#64748b] max-w-[760px]">系统介绍 Agent 的核心概念、设计模式与实现路径，并通过一个完整示例带你构建属于自己的 Agent。</p>

        <div class="flex items-center justify-between gap-3 lg:gap-[16px] mt-3 lg:mt-[20px] lg:flex-row flex-col lg:items-center items-start">
          <div class="flex items-center gap-2 lg:gap-[12px]">
            <img class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80" alt="avatar" />
            <div>
              <div class="text-xs lg:text-[14px] font-semibold text-[#1e293b]">Lin</div>
              <div class="flex gap-2 lg:gap-[14px] mt-1 lg:mt-[4px] text-[10px] lg:text-[12px] text-[#64748b] flex-wrap">
                <span><img src="/icons/time.svg" alt="时间" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />2024-05-20</span>
                <span><img src="/icons/folder.svg" alt="分类" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />Agent</span>
                <span><img src="/icons/eye.svg" alt="阅读" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />阅读 1.2k</span>
                <span><img src="/icons/reading.svg" alt="阅读时长" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />12 分钟</span>
              </div>
            </div>
          </div>
          <div class="flex gap-2 lg:gap-[12px] flex-wrap lg:w-auto w-full">
            <button @click="countAction('收藏')" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/flag-grey.svg" alt="收藏" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" />收藏 <span>128</span></button>
            <button @click="countAction('点赞')" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" /><span>256</span></button>
            <button @click="countAction('分享')" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/share-grey.svg" alt="分享" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" />分享</button>
          </div>
        </div>

        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] overflow-hidden mt-3 lg:mt-[20px]">
          <div class="h-[140px] lg:h-[225px] relative bg-gradient-to-br from-[#06153d] via-[#0b2c74] to-[#0b3d9b]">
            <div class="absolute inset-0 opacity-50 hero-grid-overlay"></div>
            <div class="absolute left-3 lg:left-[32px] top-3 lg:top-[44px] text-white text-2xl lg:text-[44px] font-bold tracking-[0.08em]">AGENT</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] left-[44px] top-[93px] w-[64px] h-[64px] rounded-full text-[24px]">AI</div>
            <div class="absolute flex items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(30,64,175,.28)] left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[40px] h-[40px] lg:w-[64px] lg:h-[64px] rounded-[12px] lg:rounded-[20px] text-xl lg:text-[30px] border-2">🤖</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] right-[64px] top-[48px] w-[48px] h-[48px] rounded-full text-[20px]">⚙️</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] right-[40px] bottom-[48px] w-[56px] h-[56px] rounded-full text-[24px]">💬</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] w-[48px] h-[48px] rounded-[14px] text-[18px] left-[32%] top-[24%]">🧠</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] w-[48px] h-[48px] rounded-[14px] text-[18px] right-[34%] top-[28%]">🔍</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] w-[48px] h-[48px] rounded-[14px] text-[18px] left-[35%] bottom-[26%]">👤</div>
            <div class="hidden lg:flex absolute items-center justify-center text-white border border-[rgba(96,165,250,.55)] bg-[rgba(15,23,42,.18)] w-[48px] h-[48px] rounded-[14px] text-[18px] right-[38%] bottom-[23%]">📊</div>
            <div class="hidden lg:block absolute h-[1px] bg-[rgba(147,197,253,.5)] left-[46%] top-[36%] right-[24%]"></div>
            <div class="hidden lg:block absolute h-[1px] bg-[rgba(147,197,253,.5)] left-[31%] top-[43%] w-[18%] -rotate-[18deg]"></div>
            <div class="hidden lg:block absolute h-[1px] bg-[rgba(147,197,253,.5)] left-[45%] top-[52%] w-[28%] rotate-[14deg]"></div>
            <div class="hidden lg:block absolute left-[28px] bottom-[18px]">
              <div class="w-[112px] h-[8px] rounded-[4px] bg-[rgba(191,219,254,.18)] mb-[8px]"></div>
              <div class="w-[80px] h-[8px] rounded-[4px] bg-[rgba(191,219,254,.18)] mb-[8px]"></div>
              <div class="w-[96px] h-[8px] rounded-[4px] bg-[rgba(191,219,254,.18)]"></div>
            </div>
          </div>
        </div>

        <section id="section-1" class="mt-3 lg:mt-[26px]">
          <h2 class="text-base lg:text-[18px] font-bold text-[#0f172a] mb-2 lg:mb-[14px]">1. 什么是 Agent?</h2>
          <p class="text-xs lg:text-[14px] leading-5 lg:leading-2 text-[#334155]">Agent（智能体）是一种能够感知环境、进行自主决策并采取行动以实现特定目标的人工智能系统。在 AI 领域，Agent 通常结合了大语言模型（LLM）的强大推理能力和工具使用（Tool Use）的执行能力，从而能够完成复杂的、多步骤的任务。</p>
          <p class="text-xs lg:text-[14px] leading-5 lg:leading-2 text-[#334155] mt-2 lg:mt-[12px]">与传统的单次问答系统不同，Agent 具备持续学习和自适应能力。它能够在多轮交互中自主规划任务路径、调用外部工具获取信息、记忆对话上下文，并根据执行反馈不断调整策略，最终达成预设目标。</p>
          <p class="text-xs lg:text-[14px] leading-5 lg:leading-2 text-[#334155] mt-2 lg:mt-[12px]">Agent 的核心价值在于其"闭环能力"——从接收任务到分析问题、制定计划、执行操作，再到评估结果，形成完整的决策与执行闭环。这种能力使得 Agent 能够处理需要多步骤推理和外部信息获取的复杂任务。</p>
          <div class="mt-2 lg:mt-[16px] border border-[#bfdbfe] bg-[rgba(239,246,255,.7)] rounded-[8px] lg:rounded-[10px] px-3 lg:px-[16px] py-2 lg:py-[14px] flex gap-2 lg:gap-[12px] items-start text-[#2563eb] text-[11px] lg:text-[13px]">
            <div class="text-lg lg:text-[20px]">💡</div>
            <div>简单来说，Agent 是"能思考 + 能行动"的 AI 系统。它不仅能够理解问题，还能主动采取行动来解决问题。</div>
          </div>
        </section>

        <section id="section-2" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">2. Agent 的核心组成</h2>
          <p class="text-[14px] leading-2 text-[#334155] mb-4">一个完整的 Agent 系统通常由以下几个核心组件构成，它们协同工作以实现智能决策和行动：</p>
          
          <div id="section-2-1" class="rounded-[14px] bg-[#f7fbff] border border-[#bfdbfe] p-[16px] mt-[12px]">
            <div class="text-[14px] font-bold text-[#2563eb]">2.1 大语言模型（LLM）</div>
            <div class="text-[13px] text-[#64748b] mt-[4px]">作为 Agent 的"大脑"，LLM 负责理解自然语言输入、生成推理过程和决策结果。它能够分析问题、理解上下文，并生成合理的响应。</div>
            <div class="text-[13px] text-[#64748b] mt-[8px]">主流的 LLM 包括 OpenAI 的 GPT 系列、Anthropic 的 Claude、Meta 的 Llama 以及国内的 Qwen 等。选择合适的模型取决于任务复杂度、成本预算和部署需求。</div>
          </div>

          <div id="section-2-2" class="rounded-[14px] bg-[#f7fbff] border border-[#bfdbfe] p-[16px] mt-[12px]">
            <div class="text-[14px] font-bold text-[#2563eb]">2.2 记忆模块（Memory）</div>
            <div class="text-[13px] text-[#64748b] mt-[4px]">记忆模块使 Agent 能够存储和检索历史对话、中间结果和长期知识。它分为短期记忆（处理当前对话上下文）和长期记忆（存储持久化知识）。</div>
            <div class="text-[13px] text-[#64748b] mt-[8px]">常见的记忆实现方式包括向量数据库（如 Pinecone、Milvus）、文档检索系统和结构化知识库。有效的记忆管理是 Agent 能够进行复杂推理的关键。</div>
          </div>

          <div id="section-2-3" class="rounded-[14px] bg-[#f7fbff] border border-[#bfdbfe] p-[16px] mt-[12px]">
            <div class="text-[14px] font-bold text-[#2563eb]">2.3 工具集（Tools）</div>
            <div class="text-[13px] text-[#64748b] mt-[4px]">工具集是 Agent 与外部世界交互的接口，包括 API 调用、数据库查询、文件操作、网页浏览等能力。通过调用工具，Agent 能够获取实时信息、执行计算任务和操作外部系统。</div>
            <div class="text-[13px] text-[#64748b] mt-[8px]">工具调用的关键在于"工具选择"——Agent 需要根据当前任务判断应该调用哪个或哪些工具，并正确解析工具返回的结果。</div>
          </div>

          <div id="section-2-4" class="rounded-[14px] bg-[#f7fbff] border border-[#bfdbfe] p-[16px] mt-[12px]">
            <div class="text-[14px] font-bold text-[#2563eb]">2.4 规划模块（Planning）</div>
            <div class="text-[13px] text-[#64748b] mt-[4px]">规划模块负责将复杂任务分解为一系列可执行的步骤，并制定执行计划。它需要分析任务目标、评估可用资源、预测执行结果，并在必要时进行回溯和调整。</div>
            <div class="text-[13px] text-[#64748b] mt-[8px]">常见的规划策略包括链式思考（Chain of Thought）、树状搜索（Tree of Thoughts）和反思机制（Reflection），这些方法能够帮助 Agent 处理需要深度推理的问题。</div>
          </div>
        </section>

        <section id="section-3" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">3. Agent 的工作流程</h2>
          <p class="text-[14px] leading-2 text-[#334155]">Agent 的工作流程通常包含以下几个阶段，形成一个完整的决策闭环：</p>
          
          <div class="mt-[16px] space-y-[12px]">
            <div class="flex items-start gap-[12px]">
              <div class="w-[28px] h-[28px] rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-[13px] font-bold flex-shrink-0">1</div>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">任务理解</div>
                <div class="text-[13px] text-[#64748b] mt-[4px]">Agent 首先接收用户的任务请求，通过 LLM 理解任务目标和需求。</div>
              </div>
            </div>
            
            <div class="flex items-start gap-[12px]">
              <div class="w-[28px] h-[28px] rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-[13px] font-bold flex-shrink-0">2</div>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">规划阶段</div>
                <div class="text-[13px] text-[#64748b] mt-[4px]">根据任务理解，Agent 制定执行计划，将复杂任务分解为多个子任务。</div>
              </div>
            </div>
            
            <div class="flex items-start gap-[12px]">
              <div class="w-[28px] h-[28px] rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-[13px] font-bold flex-shrink-0">3</div>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">工具调用</div>
                <div class="text-[13px] text-[#64748b] mt-[4px]">根据计划，Agent 调用必要的工具获取信息或执行操作。</div>
              </div>
            </div>
            
            <div class="flex items-start gap-[12px]">
              <div class="w-[28px] h-[28px] rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-[13px] font-bold flex-shrink-0">4</div>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">结果评估</div>
                <div class="text-[13px] text-[#64748b] mt-[4px]">Agent 评估工具执行结果，判断是否达成目标或需要调整策略。</div>
              </div>
            </div>
            
            <div class="flex items-start gap-[12px]">
              <div class="w-[28px] h-[28px] rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-[13px] font-bold flex-shrink-0">5</div>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">总结输出</div>
                <div class="text-[13px] text-[#64748b] mt-[4px]">完成任务后，Agent 总结执行过程和结果，以自然语言形式呈现给用户。</div>
              </div>
            </div>
          </div>
        </section>

        <section id="section-4" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">4. 设计模式</h2>
          <p class="text-[14px] leading-2 text-[#334155]">在构建 Agent 系统时，有几种经典的设计模式值得参考：</p>
          
          <div class="mt-[16px] space-y-[12px]">
            <div class="bg-[#f8fafc] rounded-[12px] p-[14px]">
              <div class="text-[14px] font-semibold text-[#1e293b]">🤝 ReAct 模式</div>
              <div class="text-[13px] text-[#64748b] mt-[6px]">将"推理"（Reasoning）和"行动"（Action）交替进行，每一步先思考再行动，使决策过程更加透明和可控。</div>
            </div>
            
            <div class="bg-[#f8fafc] rounded-[12px] p-[14px]">
              <div class="text-[14px] font-semibold text-[#1e293b]">🧠 Chain of Thought</div>
              <div class="text-[13px] text-[#64748b] mt-[6px]">通过引导 LLM 生成中间推理步骤，而不是直接给出答案，提高复杂推理任务的准确性。</div>
            </div>
            
            <div class="bg-[#f8fafc] rounded-[12px] p-[14px]">
              <div class="text-[14px] font-semibold text-[#1e293b]">🌳 Tree of Thoughts</div>
              <div class="text-[13px] text-[#64748b] mt-[6px]">探索多种推理路径，通过树状搜索找到最优解决方案，适用于需要深度探索的问题。</div>
            </div>
            
            <div class="bg-[#f8fafc] rounded-[12px] p-[14px]">
              <div class="text-[14px] font-semibold text-[#1e293b]">🔄 Reflection 反思模式</div>
              <div class="text-[13px] text-[#64748b] mt-[6px]">让 Agent 回顾自己的执行过程，识别错误并进行自我修正，提高任务完成质量。</div>
            </div>
          </div>
        </section>

        <section id="section-5" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">5. 实践：构建一个简单的 Agent</h2>
          <p class="text-[14px] leading-2 text-[#334155]">接下来，让我们通过一个实际示例来构建一个简单的 Agent。我们将使用 Python 和 OpenAI API 来实现。</p>
          
          <div class="mt-[16px] bg-[#1e293b] rounded-[12px] p-[16px] overflow-x-auto">
            <pre class="text-[13px] text-[#e2e8f0] leading-[1.6]"><code>from openai import OpenAI
from typing import List, Dict

class SimpleAgent:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.memory = []
    
    def add_to_memory(self, content: str):
        self.memory.append(content)
        # 保持记忆在合理范围内
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]
    
    def get_memory_summary(self) -> str:
        return "\n".join(self.memory)
    
    def run(self, task: str) -> str:
        # 构建提示词
        memory_str = self.get_memory_summary()
        prompt = f"""
        你是一个智能 Agent，请按照以下步骤完成任务：
        
        历史对话：
        {memory_str}
        
        当前任务：{task}
        
        请分析任务并给出详细的执行步骤和最终结果。
        """
        
        # 调用 LLM
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        result = response.choices[0].message.content
        self.add_to_memory(f"任务: {task}\n结果: {result}")
        
        return result

# 使用示例
agent = SimpleAgent(api_key="your-api-key")
result = agent.run("帮我分析一下人工智能的发展趋势")
print(result)</code></pre>
          </div>
          
          <p class="text-[14px] leading-2 text-[#334155] mt-[12px]">这个简单的 Agent 实现了核心功能：任务理解、记忆管理和结果输出。在实际应用中，你还需要添加工具调用能力、错误处理和更完善的规划模块。</p>
        </section>

        <section id="section-6" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">6. 最佳实践</h2>
          <p class="text-[14px] leading-2 text-[#334155]">在构建和部署 Agent 系统时，以下最佳实践可以帮助你提高系统的可靠性和性能：</p>
          
          <ul class="mt-[12px] space-y-[10px]">
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>明确任务边界：</strong>为 Agent 定义清晰的任务范围，避免让它处理超出能力范围的任务。</span>
            </li>
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>实现错误处理：</strong>为工具调用和 LLM 响应添加完善的错误处理机制。</span>
            </li>
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>优化提示词：</strong>精心设计系统提示词，明确 Agent 的角色和行为准则。</span>
            </li>
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>控制成本：</strong>合理选择模型和调用频率，避免不必要的 API 开销。</span>
            </li>
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>监控和日志：</strong>建立完善的监控体系，追踪 Agent 的执行过程和性能指标。</span>
            </li>
            <li class="flex items-start gap-[10px]">
              <span class="text-blue-500">•</span>
              <span class="text-[14px] text-[#334155]"><strong>安全考虑：</strong>对 Agent 的操作权限进行限制，防止恶意使用和数据泄露。</span>
            </li>
          </ul>
        </section>

        <section id="section-7" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">7. 未来展望</h2>
          <p class="text-[14px] leading-2 text-[#334155]">Agent 技术正在快速发展，未来的发展方向包括：</p>
          
          <div class="mt-[12px] grid gap-[12px]">
            <div class="flex items-center gap-[12px] p-[12px] bg-[#f8fafc] rounded-[10px]">
              <span class="text-[20px]">🧬</span>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">多模态 Agent</div>
                <div class="text-[12px] text-[#64748b]">结合文本、图像、语音等多种模态的理解和生成能力</div>
              </div>
            </div>
            
            <div class="flex items-center gap-[12px] p-[12px] bg-[#f8fafc] rounded-[10px]">
              <span class="text-[20px]">👥</span>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">多 Agent 协作</div>
                <div class="text-[12px] text-[#64748b]">多个 Agent 分工协作完成复杂任务</div>
              </div>
            </div>
            
            <div class="flex items-center gap-[12px] p-[12px] bg-[#f8fafc] rounded-[10px]">
              <span class="text-[20px]">⚡</span>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">实时学习能力</div>
                <div class="text-[12px] text-[#64748b]">Agent 能够从执行经验中持续学习和改进</div>
              </div>
            </div>
            
            <div class="flex items-center gap-[12px] p-[12px] bg-[#f8fafc] rounded-[10px]">
              <span class="text-[20px]">🔐</span>
              <div>
                <div class="text-[14px] font-semibold text-[#1e293b]">可信 AI</div>
                <div class="text-[12px] text-[#64748b]">增强 Agent 的可解释性和可信度</div>
              </div>
            </div>
          </div>
        </section>

        <section id="section-8" class="mt-[26px]">
          <h2 class="text-[18px] font-bold text-[#0f172a] mb-[14px]">8. 参考资料</h2>
          <div class="space-y-[10px]">
            <p class="text-[13px] text-[#64748b]">• <a href="#" class="text-blue-600 hover:underline">OpenAI Agent Documentation</a></p>
            <p class="text-[13px] text-[#64748b]">• <a href="#" class="text-blue-600 hover:underline">LangChain Documentation</a></p>
            <p class="text-[13px] text-[#64748b]">• <a href="#" class="text-blue-600 hover:underline">ReAct: Synergizing Reasoning and Acting in Language Models</a></p>
            <p class="text-[13px] text-[#64748b]">• <a href="#" class="text-blue-600 hover:underline">Tree of Thoughts: Deliberate Problem Solving with Large Language Models</a></p>
          </div>
        </section>

        <section class="mt-3 lg:mt-[28px]">
          <div class="flex items-center justify-between mb-2 lg:mb-[12px]">
            <div class="text-sm lg:text-[16px] font-bold text-[#0f172a]">评论 (28)</div>
            <div class="text-[10px] lg:text-[12px] text-[#475569]">最新</div>
          </div>

          <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-2 lg:p-[12px] flex gap-2 lg:gap-[12px] items-start">
            <img class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80" alt="avatar" />
            <div class="flex-1">
              <textarea v-model="draft" placeholder="写下你的评论..." class="w-full h-[50px] lg:h-[64px] resize-none border border-[#e2e8f0] rounded-[8px] lg:rounded-[10px] px-2 lg:px-[12px] py-2 lg:py-[10px] text-[11px] lg:text-[13px] outline-none bg-white text-[#0f172a]"></textarea>
              <div class="flex justify-between items-end mt-2 lg:mt-[10px]">
                <div class="hidden lg:flex">
                  <span class="text-[13px] text-[#94a3b8]">☺</span>
                  <span class="text-[13px] text-[#94a3b8]">🖼️</span>
                  <span class="text-[13px] text-[#94a3b8]">()</span>
                  <span class="text-[13px] text-[#94a3b8]">😊</span>
                  <span class="text-[13px] text-[#94a3b8]">🎞</span>
                  <span class="text-[13px] text-[#94a3b8]">🏷️</span>
                </div>
                <div class="text-right">
                  <button @click="publish" class="bg-[#2563eb] text-white border-none rounded-[8px] lg:rounded-[9px] px-3 lg:px-[14px] py-1.5 lg:py-[8px] text-[10px] lg:text-[12px] font-semibold">发布评论</button>
                  <div class="hidden lg:block text-[12px] text-[#94a3b8] mt-[8px]">0/1000</div>
                </div>
              </div>
            </div>
          </div>

          <div class="flex gap-2 lg:gap-[12px] py-2 lg:py-[12px] border-b border-[#eef2f7]" v-for="c in comments" :key="c.name + c.time">
            <img class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full object-cover flex-shrink-0" :src="c.avatar" alt="user" />
            <div class="flex-1">
              <div class="flex justify-between gap-2 lg:gap-[10px] items-center">
                <div class="text-[11px] lg:text-[13px] font-semibold text-[#1e293b]">{{ c.name }} <span v-if="c.badge" class="inline-flex px-1.5 lg:px-[6px] py-0.5 lg:py-[2px] rounded-full bg-[#eff6ff] text-[#2563eb] text-[9px] lg:text-[10px] ml-1 lg:ml-[6px]">{{ c.badge }}</span></div>
                <div class="text-[10px] lg:text-[12px] text-[#94a3b8]">{{ c.time }}</div>
              </div>
              <div class="mt-1 lg:mt-[8px] text-[11px] lg:text-[13px] leading-[1.6] lg:leading-[1.75] text-[#334155]">{{ c.text }}</div>
              <div class="flex gap-3 lg:gap-[12px] items-center mt-1 lg:mt-[8px] text-[10px] lg:text-[12px] text-[#64748b]"><span>👍 {{ c.likes }}</span><span>回复</span></div>
              <div v-if="c.reply" class="mt-2 lg:mt-[10px] rounded-[8px] lg:rounded-[12px] bg-[#f8fbff] p-2 lg:p-[12px]">
                <div class="flex justify-between gap-2 lg:gap-[10px] items-center mb-1 lg:mb-[6px]">
                  <div class="text-[11px] lg:text-[13px] font-semibold text-[#1e293b]">Lin <span class="inline-flex px-1.5 lg:px-[6px] py-0.5 lg:py-[2px] rounded-full bg-[#dbeafe] text-[#2563eb] text-[9px] lg:text-[10px] ml-1 lg:ml-[6px]">作者</span></div>
                  <div class="text-[10px] lg:text-[12px] text-[#94a3b8]">2024-05-20 12:02</div>
                </div>
                <div class="text-[11px] lg:text-[13px] leading-[1.6] lg:leading-[1.7] text-[#334155]">这个要根据具体场景来定：<br>1. 复杂推理任务：推荐 GPT-4 / Claude 3<br>2. 成本敏感场景：可以考虑 GPT-3.5 / 开源模型<br>3. 本地部署需求：建议使用 Llama 3 / Qwen 系列<br>文章第 5 节有更详细的对比，欢迎查看～</div>
                <div class="flex gap-3 lg:gap-[12px] items-center mt-1 lg:mt-[8px] text-[10px] lg:text-[12px] text-[#64748b]"><span>👍 12</span><span>回复</span></div>
              </div>
            </div>
          </div>

          <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] mt-2 lg:mt-[12px] text-center p-2 lg:p-[12px] text-[11px] lg:text-[13px] text-[#2563eb] font-semibold">加载更多评论...</div>
        </section>
      </main>

      <aside class="hidden lg:block lg:w-1/5 space-y-[16px]">
        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-[16px]">
          <div class="flex flex-col items-center mb-4">
            <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
              <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover" />
            </div>
            <h3 class="font-bold text-xl text-gray-900 mb-1">Lin</h3>
            <p class="text-sm text-gray-600">全栈开发?& AI 应用探索。</p>
          </div>
          <div class="w-full space-y-3 mb-4">
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2" />
              中国 · 深圳
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
              lin@example.com
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2" />
              github.com/linxxxx
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/project-black.svg" alt="开发经验" class="w-4 h-4 mr-2" />
              5 年开发经验
            </div>
          </div>
          <button @click="openModal" class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center">
            <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />
            下载简历(PDF)
          </button>
        </div>

        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-[16px]">
          <div class="text-[13px] font-bold text-[#334155] mb-[14px]">文章目录</div>
          <ol class="pl-0 m-0 list-none grid gap-[8px] text-[13px] leading-[1.55] text-[#475569]">
            <li @click="scrollToSection('section-1')" class="text-[#2563eb] font-semibold cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">1. 什么是 Agent?</li>
            <li @click="scrollToSection('section-2')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">2. Agent 的核心组成</li>
            <li @click="scrollToSection('section-2-1')" class="pl-4 text-[#64748b] cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">2.1 大语言模型（LLM）</li>
            <li @click="scrollToSection('section-2-2')" class="pl-4 text-[#64748b] cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">2.2 记忆模块（Memory）</li>
            <li @click="scrollToSection('section-2-3')" class="pl-4 text-[#64748b] cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">2.3 工具集（Tools）</li>
            <li @click="scrollToSection('section-2-4')" class="pl-4 text-[#64748b] cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">2.4 规划模块（Planning）</li>
            <li @click="scrollToSection('section-3')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">3. Agent 的工作流程</li>
            <li @click="scrollToSection('section-4')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">4. 设计模式</li>
            <li @click="scrollToSection('section-5')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">5. 实践：构建一个简单的 Agent</li>
            <li @click="scrollToSection('section-6')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">6. 最佳实践</li>
            <li @click="scrollToSection('section-7')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">7. 未来展望</li>
            <li @click="scrollToSection('section-8')" class="cursor-pointer hover:bg-blue-50 px-2 py-1 rounded transition-colors">8. 参考资料</li>
          </ol>
        </div>

        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-[16px]">
          <div class="text-[13px] font-bold text-[#334155] mb-[14px]">文章信息</div>
          <div class="flex justify-between gap-[10px] text-[13px] text-[#475569] mb-[12px]"><span>发布时间</span><span>2024-05-20 10:30</span></div>
          <div class="flex justify-between gap-[10px] text-[13px] text-[#475569] mb-[12px]"><span>最后更新</span><span>2024-05-21 14:22</span></div>
          <div class="flex justify-between gap-[10px] text-[13px] text-[#475569] mb-[12px]"><span>文章字数</span><span>约3,856</span></div>
          <div class="flex justify-between gap-[10px] text-[13px] text-[#475569] mb-[12px]"><span>阅读时长</span><span>12 分钟</span></div>
          <div class="flex flex-wrap gap-[8px]">
            <span class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">Agent</span>
            <span class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">LLM</span>
            <span class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">AI</span>
            <span class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">LangChain</span>
            <span class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">Python</span>
          </div>
        </div>

        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-[16px]">
          <div class="text-[13px] font-bold text-[#334155] mb-[14px]">相关文章</div>
          <div class="flex gap-[12px] items-center mb-[12px]" v-for="r in related" :key="r.title">
            <img :src="r.img" alt="rel" class="w-[64px] h-[40px] rounded-[6px] object-cover" />
            <div>
              <div class="text-[13px] font-medium text-[#334155] whitespace-nowrap overflow-hidden text-ellipsis max-w-[180px]">{{ r.title }}</div>
              <div class="text-[12px] text-[#94a3b8] mt-[4px]">{{ r.sub }}</div>
            </div>
          </div>
          <div class="text-[#2563eb] text-[13px] font-semibold mt-[2px]">查看更多 →</div>
        </div>

        <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-[16px]">
          <div class="text-[13px] font-bold text-[#334155] mb-[14px]">文章导航</div>
          <div class="mb-[14px] text-[13px] text-[#334155]"><div class="text-[#94a3b8] mb-[4px]">← 上一篇</div><div>Next.js 14 新特性解析</div></div>
          <div class="mb-[14px] text-[13px] text-[#334155]"><div class="text-[#94a3b8] mb-[4px]">下一篇 →</div><div>构建高可用的 AI 应用架构</div></div>
        </div>
      </aside>
    </div>
  </div>
</div>  
</template>

<script setup>
import { ref } from 'vue'
import { usePdfModal } from '../composables/usePdfModal'

const { openModal } = usePdfModal()

const draft = ref('')
const comments = ref([
  { name: '张三', badge: '置顶', time: '2024-05-20 11:20', text: '这篇文章写得非常详细👍，特别是关于 Agent 核心组件的拆解，对我理解整个工作流程帮助很大', likes: 18, avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80' },
  { name: '李四', time: '2024-05-20 11:45', text: '请问在实际项目中，如何选择合适的 LLM 模型呢？不同模型在 Agent 中的表现差异大吗？', likes: 5, avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=80', reply: true },
  { name: '王五', time: '2024-05-20 13:15', text: '能否分享一下你在开发过程中遇到的坑？比如记忆管理那块，我感觉很难设计', likes: 3, avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=120&q=80' },
])

const related = [
  { title: 'ChatFlow - 智能对话工作流平台', sub: '阅读 980 · 2024-05-18', img: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=200&q=80' },
  { title: '使用 LangChain 构建你的第一个应用', sub: '阅读 1.5k · 2024-05-15', img: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=200&q=80' },
  { title: 'LLM 应用开发最佳实践', sub: '阅读 2.1k · 2024-05-10', img: 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=200&q=80' },
]

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest' })
  }
}

const countAction = (name) => alert(`${name}成功`)
const publish = () => alert(draft.value ? `发布?${draft.value}` : '请输入评论内容')
const follow = () => alert('已关注')
</script>

<style scoped>
.hero-grid-overlay {
  background-image: 
    linear-gradient(rgba(120, 160, 255, 0.18) 1px, transparent 1px),
    linear-gradient(90deg, rgba(120, 160, 255, 0.18) 1px, transparent 1px);
  background-size: 34px 34px;
}
</style>