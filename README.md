# 🤖 LLM Agents with AutoGen

A hands-on tutorial series for building multi-agent systems using Microsoft's AutoGen framework.

## 📚 Description

This repository contains a comprehensive tutorial series on building and orchestrating multi-agent systems using AutoGen. Through six progressive lessons, you'll learn how to create, configure, and coordinate multiple AI agents to perform complex tasks, from simple conversations to advanced financial analysis and report generation.

AutoGen is a framework that enables the development of LLM-powered applications using multiple agents that can converse with each other, use tools, and work together to accomplish tasks. This tutorial series provides practical examples and hands-on exercises to help you master the framework.

## 🔧 Prerequisites

- Python 3.10+
- OpenAI API key (stored in a `.env` file)
- Basic understanding of Python programming
- Familiarity with Jupyter notebooks

## 🚀 Features

The tutorial series covers the following topics:

1. **Multi-Agent Conversation** - Create basic conversational agents and manage their interactions
2. **Sequential Chats** - Implement a customer onboarding process using sequential agent interactions
3. **Reflection and Content Creation** - Use nested chats and reflection for collaborative content creation
4. **Tool Use** - Implement and use tools with agents, demonstrated through a conversational chess game
5. **Code Generation and Financial Analysis** - Generate and execute code for financial data analysis
6. **Planning and Report Generation** - Orchestrate multiple specialized agents in a group chat to plan and generate reports

## 🛠️ Setup Guide

1. Clone this repository:
   ```bash
   git clone https://github.com/corticalstack/llm-agents-autogen.git
   cd llm-agents-autogen
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Navigate to any lesson folder (l1-l6) and open the corresponding notebook.

## 📂 Repository Structure

```
llm-agents-autogen/
├── .gitignore
├── requirements.txt
├── l1/
│   ├── L1_Multi-Agent_Conversation_and_Stand-up_Comedy.ipynb
│   └── utils.py
├── l2/
│   ├── L2_Sequential_Chats_and_Customer_Onboarding.ipynb
│   └── utils.py
├── l3/
│   ├── L3_Reflection_and_Blogpost_Writing.ipynb
│   └── utils.py
├── l4/
│   ├── L4_Tool_Use_and_Conversational_Chess.ipynb
│   └── utils.py
├── l5/
│   ├── L5_Coding_and_Financial_Analysis.ipynb
│   ├── utils.py
│   └── coding/
│       ├── functions.py
│       ├── plot_ytd_stock_gains.py
│       ├── stock_data_plot.py
│       └── stock_prices_YTD_plot.png
└── l6/
    ├── L6-Planning_and_Stock_Report_Generation.ipynb
    └── utils.py
```

## 🔍 Resources

- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)

## 📝 License

This project is licensed under the terms of the MIT license.
