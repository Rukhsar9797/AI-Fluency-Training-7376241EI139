# Analysis — Direct Prompting vs Chain-of-Thought vs ReAct

## 1. Scenario

The scenario chosen for this task is a Smart Energy and Equipment Monitoring Assistant.

The assistant is designed to answer basic industrial energy and equipment-monitoring questions.

The scenario includes energy calculations, temperature analysis, sensor-limit checking and retrieval of motor specifications.

The three approaches compared are Direct Prompting, Chain-of-Thought prompting and a ReAct agent.

---

## 2. Direct Prompting

Direct prompting sends the user's question directly to the language model and asks for an answer.

No external tools are provided and no reasoning steps are requested in the output.

For example, the assistant can calculate the daily energy cost of a 5 kW motor operating for 6 hours at ₹8 per kWh.

However, direct prompting cannot retrieve current or application-specific motor specifications because it has no tool access.

Its main advantage is speed and simplicity.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to solve a problem step by step before producing the final answer.

This approach is useful for multi-step calculations and logical reasoning.

For example, the motor energy-cost question requires multiplying power by operating hours and then multiplying the energy consumption by the electricity tariff.

However, Chain-of-Thought does not automatically provide external information. If a motor's rated power is stored in an external system, the model cannot retrieve it unless a tool or data source is provided.

---

## 4. ReAct Agent

The ReAct approach combines reasoning with actions and observations.

The agent can determine that it needs motor specifications, call the appropriate tool, observe the returned information and then continue reasoning.

For this scenario, the agent uses the `get_motor_spec` tool to retrieve the rated power, rated voltage and normal temperature limit.

The cycle can be represented as:

Question → Thought → Action → Observation → Thought → Final Answer

This allows the agent to combine language understanding with external information retrieval.

---

## 5. Comparison

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Basic | Step-by-step | Multi-step with actions |
| Tool usage | None | None | Uses tools |
| Reliability on multi-step questions | Moderate | Higher for structured reasoning | Depends on reasoning and tools |
| Transparency | Final answer only | Steps can be displayed | Actions and observations can be displayed |
| Speed / cost | Fastest | More processing | Usually more processing because of tool calls |
| Consistency | Generally high at temperature 0 | High at temperature 0 | Depends on model and tool decisions |

---

## 6. Self-Consistency Observation

The energy-cost calculation was run five times using a non-zero temperature.

The correct calculation is:

5 kW × 6 hours = 30 kWh

30 kWh × ₹8 = ₹240

Therefore, the correct daily operating cost is ₹240.

The repeated runs were compared to observe whether the model produced the same answer.

At temperature 0, the response was more deterministic and repeated runs are expected to be more consistent.

---

## 7. Suitability Analysis

For this scenario, the ReAct approach is useful when the assistant needs to retrieve equipment specifications from an external source before answering.

Chain-of-Thought is useful for calculations and logical questions where all required information is already available in the question.

Direct prompting is suitable for simple questions where no external information or complex reasoning is required.

The self-consistency experiment also shows how changing the temperature can affect the consistency of model responses.

---

## 8. Conclusion

Direct prompting is appropriate for simple questions and straightforward response generation.

Chain-of-Thought is useful for problems involving multiple reasoning or calculation steps when the required information is already available.

ReAct is appropriate when a problem requires both reasoning and interaction with external tools or information sources.

Therefore, the choice of approach depends on whether the task requires simple generation, deeper reasoning or external actions and observations.